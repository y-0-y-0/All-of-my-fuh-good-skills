---
name: git-guardrails-amp
description: Blocks destructive Git commands before Amp shell tools run them. Use when the user wants to prevent Git pushes, destructive resets or cleans, or forced branch deletion in Amp.
---

# Git Guardrails for Amp

The `git-guardrails-amp` Amp plugin intercepts shell tool calls before they execute. It rejects dangerous Git commands and lets the agent continue with a safe alternative.

## Blocked commands

- `git push` (all variants including `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

The rejected command never reaches the shell. Amp receives a message naming the matched rule.

## Scope

The global User Plugin applies to every Amp thread for this user. Reload plugins after publishing it to update the current thread. New threads load it automatically.

For a project-only guard, install the same plugin in that repository's `.amp/plugins/` directory instead.

## Customize

Edit `blockedPatterns` in the plugin when the user requests a different policy. Keep `git push`, `git reset --hard`, and `git clean -f` blocked unless the user explicitly removes them.

## Verify

After loading the plugin, attempt `git push origin main` in a test workspace. Amp must reject the tool call and must not run the command.
