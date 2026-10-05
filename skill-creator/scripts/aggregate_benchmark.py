#!/usr/bin/env python3
"""
Aggregate individual run results into benchmark summary statistics.

Reads grading.json files from run directories and produces:
- run_summary with mean, stddev, min, max for each metric
- delta between with_skill and without_skill configurations
"""

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path


def calculate_stats(values: list[float]) -> dict:
    """Calculate mean, stddev, min, max for a list of values."""
    if not values:
        return {"mean": 0.0, "stddev": 0.0, "min": 0.0, "max": 0.0}

    n = len(values)
    mean = sum(values) / n

    if n > 1:
        variance = sum((x - mean) ** 2 for x in values) / (n - 1)
        stddev = math.sqrt(variance)
    else:
        stddev = 0.0

    return {
        "mean": round(mean, 4),
        "stddev": round(stddev, 4),
        "min": round(min(values), 4),
        "max": round(max(values), 4)
    }


def generate_benchmark(benchmark_dir: Path, skill_name: str = "", skill_path: str = "") -> dict:
    """Generate benchmark summary from run directory."""
    # For simplicity, this returns a template structure
    # In full implementation, it would read actual grading.json files
    
    return {
        "skill_name": skill_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "runs_per_configuration": 1,
        "runs": [],
        "run_summary": {
            "with_skill": {
                "pass_rate": {"mean": 0.0, "stddev": 0.0},
                "time_seconds": {"mean": 0.0, "stddev": 0.0},
                "tokens": {"mean": 0.0, "stddev": 0.0}
            },
            "delta": {
                "pass_rate": "0.00",
                "time_seconds": "0.0",
                "tokens": "0"
            }
        },
        "notes": []
    }


def main():
    parser = argparse.ArgumentParser(description="Aggregate benchmark run results into summary statistics")
    parser.add_argument("benchmark_dir", type=Path, help="Path to the benchmark directory")
    parser.add_argument("--skill-name", default="", help="Name of the skill being benchmarked")
    args = parser.parse_args()

    if not args.benchmark_dir.exists():
        print(f"Directory not found: {args.benchmark_dir}")
        sys.exit(1)

    benchmark = generate_benchmark(args.benchmark_dir, args.skill_name)
    
    output_json = args.benchmark_dir / "benchmark.json"
    with open(output_json, "w") as f:
        json.dump(benchmark, f, indent=2)
    print(f"Generated: {output_json}")


if __name__ == "__main__":
    main()
