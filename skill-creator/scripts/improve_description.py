#!/usr/bin/env python3
"""Improve a skill description based on eval results.

This script provides a framework for optimizing skill descriptions.
In a full Claude Code or Cowork environment, it would use `claude -p`
to iteratively improve descriptions based on trigger evaluation results.
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.utils import parse_skill_md


def improve_description(skill_name: str, skill_content: str, current_description: str, eval_results: dict, history: list[dict]) -> str:
    """Analyze eval results and suggest description improvements.
    
    In a full implementation, this would call Claude to generate improved descriptions.
    For now, it provides analysis and guidance.
    """
    failed_triggers = [r for r in eval_results.get("results", []) if r.get("should_trigger") and not r.get("pass")]
    false_triggers = [r for r in eval_results.get("results", []) if not r.get("should_trigger") and r.get("pass")]
    
    print(f"\nDescription Optimization Analysis for: {skill_name}")
    print("=" * 50)
    print(f"\nCurrent description: {current_description}")
    print(f"\nScore: {eval_results.get('summary', {}).get('passed', 0)}/{eval_results.get('summary', {}).get('total', 0)}")
    
    if failed_triggers:
        print(f"\nFailed to trigger ({len(failed_triggers)} queries):")
        for r in failed_triggers[:5]:
            print(f"  - {r.get('query', '')[:80]}")
    
    if false_triggers:
        print(f"\nFalse triggers ({len(false_triggers)} queries):")
        for r in false_triggers[:5]:
            print(f"  - {r.get('query', '')[:80]}")
    
    print("\nSuggestions:")
    print("  - Review queries in failed_triggers - add relevant keywords")
    print("  - Review queries in false_triggers - make description more specific")
    print("  - Keep description under 1024 characters")
    print("  - Focus on what the skill DOES, not what it IS")
    
    return current_description


def main():
    parser = argparse.ArgumentParser(description="Improve a skill description based on eval results")
    parser.add_argument("--eval-results", required=True, help="Path to eval results JSON")
    parser.add_argument("--skill-path", required=True, help="Path to skill directory")
    parser.add_argument("--verbose", action="store_true", help="Print details")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    if not (skill_path / "SKILL.md").exists():
        print(f"Error: No SKILL.md found at {skill_path}", file=sys.stderr)
        sys.exit(1)

    eval_results = json.loads(Path(args.eval_results).read_text())
    name, original_description, content = parse_skill_md(skill_path)

    if args.verbose:
        print(f"Current: {original_description}", file=sys.stderr)

    new_description = improve_description(
        skill_name=name,
        skill_content=content,
        current_description=original_description,
        eval_results=eval_results,
        history=[],
    )

    output = {
        "description": original_description,
        "analysis": {
            "failed_triggers": len([r for r in eval_results.get("results", []) if r.get("should_trigger") and not r.get("pass")]),
            "false_triggers": len([r for r in eval_results.get("results", []) if not r.get("should_trigger") and r.get("pass")]),
            "total": eval_results.get("summary", {}).get("total", 0),
        }
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
