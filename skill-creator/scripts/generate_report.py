#!/usr/bin/env python3
"""Generate an HTML report from run_loop.py output.

Takes the JSON output from run_loop.py and generates a visual HTML report
showing each description attempt with check/x for each test case.
"""

import argparse
import html
import json
import sys
from pathlib import Path


def generate_html(data: dict, auto_refresh: bool = False, skill_name: str = "") -> str:
    """Generate HTML report from loop output data."""
    history = data.get("history", [])
    title_prefix = html.escape(skill_name + " — ") if skill_name else ""

    refresh_tag = '    <meta http-equiv="refresh" content="5">\n' if auto_refresh else ""

    html_parts = ["""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
""" + refresh_tag + """    <title>""" + title_prefix + """Skill Description Optimization</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 100%;
            margin: 0 auto;
            padding: 20px;
            background: #faf9f5;
            color: #141413;
        }
        h1 { font-family: 'Poppins', sans-serif; color: #141413; }
        .summary {
            background: white;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 20px;
            border: 1px solid #e8e6dc;
        }
        table {
            border-collapse: collapse;
            background: white;
            border: 1px solid #e8e6dc;
            border-radius: 6px;
            font-size: 12px;
            min-width: 100%;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #e8e6dc;
        }
        .pass { color: #788c5d; }
        .fail { color: #c44; }
        .best-row { background: #eef2e8; }
    </style>
</head>
<body>
    <h1>""" + title_prefix + """Skill Description Optimization Report</h1>
"""]

    if history:
        best_iter = max(range(len(history)), key=lambda i: history[i].get("score", 0))
        scores = [h.get("score", 0) for h in history]
        
        html_parts.append(f'<div class="summary">')
        html_parts.append(f'<p>Iterations: {len(history)}</p>')
        html_parts.append(f'<p>Best Score: {scores[best_iter]*100:.0f}% (iteration {best_iter + 1})</p>')
        html_parts.append(f'</div>')
        
        html_parts.append('<table>')
        html_parts.append('<thead><tr><th>Iter</th><th>Score</th><th>Description</th></tr></thead>')
        html_parts.append('<tbody>')
        
        for i, h in enumerate(history):
            row_class = "best-row" if i == best_iter else ""
            html_parts.append(f'<tr class="{row_class}">')
            html_parts.append(f'<td>{i + 1}</td>')
            html_parts.append(f'<td>{"PASS" if h["score"] >= 0.8 else "PARTIAL" if h["score"] >= 0.5 else "FAIL"}</td>')
            html_parts.append(f'<td>{html.escape(h.get("description", ""))}</td>')
            html_parts.append('</tr>')
        
        html_parts.append('</tbody></table>')

    html_parts.append("""
</body>
</html>
""")

    return "".join(html_parts)


def main():
    parser = argparse.ArgumentParser(description="Generate HTML report from run_loop output")
    parser.add_argument("input", help="Path to JSON output from run_loop.py (or - for stdin)")
    parser.add_argument("-o", "--output", default=None, help="Output HTML file (default: stdout)")
    parser.add_argument("--skill-name", default="", help="Skill name to include in the report title")
    args = parser.parse_args()

    if args.input == "-":
        data = json.load(sys.stdin)
    else:
        data = json.loads(Path(args.input).read_text())

    html_output = generate_html(data, skill_name=args.skill_name)

    if args.output:
        Path(args.output).write_text(html_output)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(html_output)


if __name__ == "__main__":
    main()
