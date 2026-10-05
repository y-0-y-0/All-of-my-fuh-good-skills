---
name: caveman-stats
description: >
  Show real token usage and estimated savings for the current session.
  Reads directly from the Claude Code session log — no AI estimation.
  Triggers on /caveman-stats. Output is injected by the mode-tracker hook;
  the model itself does not compute the numbers.
license: MIT
compatibility: cline
metadata:
  author: https://github.com/JuliusBrussee
  version: "1.0.0"
  domain: productivity
  triggers: /caveman-stats, show stats, token usage, token savings
---

# Caveman Stats

This skill is delivered by `hooks/caveman-stats.js` (read by `hooks/caveman-mode-tracker.js` on `/caveman-stats`). The model does not need to do anything when this skill fires — the hook returns `decision: "block"` with the formatted stats as the reason. The user sees the numbers immediately.

Use when user invokes `/caveman-stats` to see token savings from using caveman mode.
