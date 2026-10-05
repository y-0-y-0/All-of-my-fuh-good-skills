---
name: cavecrew
description: >
  Decision guide for delegating to caveman-style subagents. Tells the main
  thread WHEN to spawn `cavecrew-investigator` (locate code), `cavecrew-builder`
  (1-2 file edit), or `cavecrew-reviewer` (diff review) instead of doing the
  work inline or using vanilla `Explore`. Subagent output is caveman-compressed
  so the tool-result injected back into main context is ~60% smaller — main
  context lasts longer across long sessions.
  Trigger: "delegate to subagent", "use cavecrew", "spawn investigator/builder/reviewer",
  "save context", "compressed agent output".
license: MIT
compatibility: cline
metadata:
  author: https://github.com/JuliusBrussee
  version: "1.0.0"
  domain: agent-workflows
  triggers: cavecrew, delegate, subagent, spawn investigator, spawn builder, spawn reviewer, save context
---

# Cavecrew

Three subagent presets that emit caveman output. Same job as Anthropic defaults (Explore, edit-style agents, reviewer); difference is the tool-result they return is compressed.

## When to use cavecrew vs alternatives

| Task | Use |
|------|-----|
| "Where is X defined / what calls Y / list uses of Z" | `cavecrew-investigator` |
| Surgical edit, ≤2 files, scope obvious | `cavecrew-builder` |
| Review diff, branch, or file for bugs | `cavecrew-reviewer` |

## Output contracts

**`cavecrew-investigator`**
```
<Header>:
- path:line — `symbol` — short note
totals: <counts>.
```

**`cavecrew-builder`**
```
<path:line-range> — <change ≤10 words>.
verified: <re-read OK | mismatch @ path:line>.
```

**`cavecrew-reviewer`**
```
path:line: <emoji> <severity>: <problem>. <fix>.
totals: N🔴 N🟡 N🔵 N❓
```

## Chaining patterns

**Locate → fix → verify:**
1. `cavecrew-investigator` returns site list.
2. Main thread hands paths to `cavecrew-builder`.
3. `cavecrew-reviewer` audits the diff.
