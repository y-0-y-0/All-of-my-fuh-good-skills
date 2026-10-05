#!/usr/bin/env python3
"""Generate and serve a review page for eval results.

Reads the workspace directory, discovers runs (directories with outputs/),
embeds all output data into a self-contained HTML page, and serves it via
a tiny HTTP server. Feedback auto-saves to feedback.json in the workspace.

Usage:
    python generate_review.py <workspace-path> [--port PORT] [--skill-name NAME]
    python generate_review.py <workspace-path> --static <output_path>

No dependencies beyond the Python stdlib are required.
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import signal
import subprocess
import sys
import time
import webbrowser
from functools import partial
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Files to exclude from output listings
METADATA_FILES = {"transcript.md", "user_notes.md", "metrics.json"}

# Extensions we render as inline text
TEXT_EXTENSIONS = {
    ".txt", ".md", ".json", ".csv", ".py", ".js", ".ts", ".tsx", ".jsx",
    ".yaml", ".yml", ".xml", ".html", ".css", ".sh", ".rb", ".go", ".rs",
    ".java", ".c", ".cpp", ".h", ".hpp", ".sql", ".r", ".toml",
}

# Extensions we render as inline images
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

# MIME type overrides for common types
MIME_OVERRIDES = {
    ".svg": "image/svg+xml",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
}


def get_mime_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in MIME_OVERRIDES:
        return MIME_OVERRIDES[ext]
    mime, _ = mimetypes.guess_type(str(path))
    return mime or "application/octet-stream"


def find_runs(workspace: Path) -> list[dict]:
    """Recursively find directories that contain an outputs/ subdirectory."""
    runs: list[dict] = []
    _find_runs_recursive(workspace, workspace, runs)
    runs.sort(key=lambda r: (r.get("eval_id", float("inf")), r["id"]))
    return runs


def _find_runs_recursive(root: Path, current: Path, runs: list[dict]) -> None:
    if not current.is_dir():
        return

    outputs_dir = current / "outputs"
    if outputs_dir.is_dir():
        run = build_run(root, current)
        if run:
            runs.append(run)
        return

    skip = {"node_modules", ".git", "__pycache__", "skill", "inputs"}
    for child in sorted(current.iterdir()):
        if child.is_dir() and child.name not in skip:
            _find_runs_recursive(root, child, runs)


def build_run(root: Path, run_dir: Path) -> dict | None:
    """Build a run dict with prompt, outputs, and grading data."""
    prompt = ""
    eval_id = None

    # Try eval_metadata.json
    for candidate in [run_dir / "eval_metadata.json", run_dir.parent / "eval_metadata.json"]:
        if candidate.exists():
            try:
                metadata = json.loads(candidate.read_text())
                prompt = metadata.get("prompt", "")
                eval_id = metadata.get("eval_id")
            except (json.JSONDecodeError, OSError):
                pass
            if prompt:
                break

    # Fall back to transcript.md
    if not prompt:
        for candidate in [run_dir / "transcript.md", run_dir / "outputs" / "transcript.md"]:
            if candidate.exists():
                try:
                    text = candidate.read_text()
                    match = re.search(r"## Eval Prompt\n\n([\s\S]*?)(?=\n##|$)", text)
                    if match:
                        prompt = match.group(1).strip()
                except OSError:
                    pass

    # Collect outputs
    outputs = []
    for f in sorted(outputs_dir.iterdir()):
        if f.name in METADATA_FILES:
            continue
        if f.is_file():
            outputs.append({"name": f.name, "path": str(f.relative_to(root))})
        elif f.is_dir():
            outputs.append({"name": f.name + "/", "path": str(f.relative_to(root))})

    return {
        "id": run_dir.name,
        "outputs_dir": str(outputs_dir.relative_to(root)),
        "prompt": prompt,
        "outputs": outputs,
        "eval_id": eval_id,
    }


# Create static HTML viewer
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Eval Review</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 20px; background: #faf9f5; }
        .run { background: white; margin: 10px 0; padding: 15px; border-radius: 6px; border: 1px solid #e8e6dc; }
        .prompt { white-space: pre-wrap; background: #f5f4f0; padding: 10px; border-radius: 4px; margin: 10px 0; }
        .output { margin: 5px 0; }
        .output a { color: #0066cc; }
    </style>
</head>
<body>
    <h1>Eval Review</h1>
    <p>Skill: {skill_name}</p>
    {runs_html}
</body>
</html>
'''

def generate_html(runs: list[dict], skill_name: str, previous: dict | None = None, benchmark: dict | None = None) -> str:
    """Generate static HTML for review."""
    runs_html = ""
    for run in runs:
        runs_html += f'<div class="run"><h3>{run["id"]}</h3>'
        runs_html += f'<div class="prompt">{run["prompt"] or "(no prompt)"}</div>'
        runs_html += '<div class="outputs">'
        for output in run.get("outputs", []):
            runs_html += f'<div class="output"><a href="{output["path"]}">{output["name"]}</a></div>'
        runs_html += '</div></div>'
    return HTML_TEMPLATE.format(skill_name=skill_name, runs_html=runs_html)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate eval review HTML")
    parser.add_argument("workspace", type=Path, help="Path to workspace directory")
    parser.add_argument("--static", "-s", type=Path, default=None, help="Write standalone HTML to this path instead of starting a server")
    parser.add_argument("--skill-name", "-n", type=str, default=None, help="Skill name for header")
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    if not workspace.is_dir():
        print(f"Error: {workspace} is not a directory", file=sys.stderr)
        sys.exit(1)

    runs = find_runs(workspace)
    if not runs:
        print(f"No runs found in {workspace}", file=sys.stderr)
        sys.exit(1)

    skill_name = args.skill_name or workspace.name.replace("-workspace", "")

    if args.static:
        html = generate_html(runs, skill_name)
        args.static.parent.mkdir(parents=True, exist_ok=True)
        args.static.write_text(html)
        print(f"\n  Static viewer written to: {args.static}\n")
        sys.exit(0)

    print(f"\nRuns found: {len(runs)} in {workspace}")
    print("Use --static <path> to generate static HTML\n")


if __name__ == "__main__":
    main()
