#!/usr/bin/env python3
"""Run the eval + improve loop until all pass or max iterations reached.

Combines run_eval.py and improve_description.py in a loop, tracking history
and returning the best description found.
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.run_eval import run_eval
from scripts.generate_report import generate_html


def run_loop(eval_set: list[dict], skill_path: Path, max_iterations: int = 5, verbose: bool = False) -> dict:
    """Run the eval + improvement loop."""
    name = ""
    description = ""
    
    # Simple skill parsing
    content = (skill_path / "SKILL.md").read_text()
    for line in content.split('\n'):
        if line.startswith('name:'):
            name = line.split(':', 1)[1].strip()
        elif line.startswith('description:'):
            description = line.split(':', 1)[1].strip()
    
    history = []
    best_score = 0
    best_description = description
    
    for iteration in range(1, max_iterations + 1):
        if verbose:
            print(f"\nIteration {iteration}/{max_iterations}", file=sys.stderr)
            print(f"Description: {description}", file=sys.stderr)
        
        # Run evaluation
        results = run_eval(eval_set, name, description)
        score = results["summary"]["passed"] / results["summary"]["total"]
        
        history.append({
            "iteration": iteration,
            "description": description,
            "score": score,
            "results": results["results"],
        })
        
        if score > best_score:
            best_score = score
            best_description = description
        
        # Check if all passed
        if results["summary"]["failed"] == 0:
            break
    
    return {
        "skill_name": name,
        "original_description": description,
        "best_description": best_description,
        "best_score": best_score,
        "history": history,
    }


def main():
    parser = argparse.ArgumentParser(description="Run eval + improve loop")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON file")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--max-iterations", type=int, default=5, help="Max improvement iterations")
    parser.add_argument("--verbose", action="store_true", help="Print progress")
    parser.add_argument("--report", default=None, help="Output path for HTML report")
    args = parser.parse_args()

    eval_set = json.loads(Path(args.eval_set).read_text())
    skill_path = Path(args.skill_path)

    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        sys.exit(1)

    output = run_loop(
        eval_set=eval_set,
        skill_path=skill_path,
        max_iterations=args.max_iterations,
        verbose=args.verbose,
    )

    print(json.dumps(output, indent=2))

    if args.report:
        html = generate_html(output)
        Path(args.report).write_text(html)
        print(f"\nReport written to {args.report}", file=sys.stderr)


if __name__ == "__main__":
    main()
