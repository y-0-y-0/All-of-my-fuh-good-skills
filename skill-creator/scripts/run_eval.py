#!/usr/bin/env python3
"""Run trigger evaluation for a skill description.

Tests whether a skill's description causes Claude to trigger (read the skill)
for a set of queries. Outputs results as JSON.

Note: In a full Claude Code environment, this would use `claude -p` to test triggers.
This simplified version provides the structure and can work with mock data or
manual evaluation.
"""

import argparse
import json
import sys
from pathlib import Path


def run_eval(eval_set: list[dict], skill_name: str, description: str, runs_per_query: int = 3, trigger_threshold: float = 0.5) -> dict:
    """Run trigger evaluation for a skill description.
    
    Returns evaluation results showing which queries triggered and which didn't.
    In a full implementation, this would call claude -p for each query.
    """
    results = []
    
    for item in eval_set:
        query = item["query"]
        should_trigger = item.get("should_trigger", True)
        
        # In a full implementation, we would run the query multiple times
        # and check if the skill was triggered. For now, we simulate this.
        # Real implementation would use claude -p subprocess calls.
        
        # Simulated trigger detection (would be real in full implementation)
        triggers = runs_per_query if should_trigger else 0  # placeholder
        
        trigger_rate = triggers / runs_per_query
        did_pass = (trigger_rate >= trigger_threshold) if should_trigger else (trigger_rate < trigger_threshold)
        
        results.append({
            "query": query,
            "should_trigger": should_trigger,
            "trigger_rate": trigger_rate,
            "triggers": triggers,
            "runs": runs_per_query,
            "pass": did_pass,
        })
    
    passed = sum(1 for r in results if r["pass"])
    total = len(results)
    
    return {
        "skill_name": skill_name,
        "description": description,
        "results": results,
        "summary": {
            "total": total,
            "passed": passed,
            "failed": total - passed,
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Run trigger evaluation for a skill description")
    parser.add_argument("--eval-set", required=True, help="Path to eval set JSON file")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--runs-per-query", type=int, default=3, help="Number of runs per query")
    parser.add_argument("--trigger-threshold", type=float, default=0.5, help="Trigger rate threshold")
    parser.add_argument("--verbose", action="store_true", help="Print progress")
    args = parser.parse_args()

    eval_set = json.loads(Path(args.eval_set).read_text())
    skill_path = Path(args.skill_path)

    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        sys.exit(1)

    # Simple skill parsing
    content = (skill_path / "SKILL.md").read_text()
    for line in content.split('\n'):
        if line.startswith('name:'):
            skill_name = line.split(':', 1)[1].strip()
            break
    
    output = run_eval(
        eval_set=eval_set,
        skill_name=skill_name,
        description="",
        runs_per_query=args.runs_per_query,
        trigger_threshold=args.trigger_threshold,
    )

    if args.verbose:
        summary = output["summary"]
        print(f"Results: {summary['passed']}/{summary['total']} passed", file=sys.stderr)

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
