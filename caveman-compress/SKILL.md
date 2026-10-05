---
name: caveman-compress
description: >
  Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format
  to save input tokens. Preserves all technical substance, code, URLs, and structure.
  Compressed version overwrites the original file. Human-readable backup saved as FILE.original.md.
  Trigger: /caveman-compress FILEPATH or "compress memory file"
license: MIT
compatibility: cline
metadata:
  author: https://github.com/JuliusBrussee
  version: "1.0.0"
  domain: productivity
  triggers: /caveman-compress, compress memory, compress file, reduce tokens
---

# Caveman Compress

## Purpose

Compress natural language files (CLAUDE.md, todos, preferences) into caveman-speak to reduce input tokens. Compressed version overwrites original. Human-readable backup saved as `<filename>.original.md`.

## Trigger

`/caveman-compress <filepath>` or when user asks to compress a memory file.

## Process

1. Search for `scripts/__main__.py` next to this SKILL.md if compression scripts are missing
2. Run: `python3 -m scripts <absolute_filepath>`
3. Script will:
   - Detect file type
   - Call Claude to compress
   - Validate output
   - If errors: targeted fixes only
   - Retry up to 2 times
   - Report error to user if still failing

## Compression Rules

### Remove
- Articles: a, an, the
- Filler: just, really, basically, actually, simply, essentially, generally
- Pleasantries: "sure", "certainly", "of course", "happy to"
- Hedging: "it might be worth", "you could consider"

### Preserve EXACTLY
- Code blocks (fenced ``` and indented)
- Inline code (`backtick content`)
- URLs and links
- File paths
- Commands
- Technical terms
- Proper nouns
- Dates, version numbers

### Compress
- Short synonyms: "big" not "extensive", "fix" not "implement a solution for"
- Fragments OK
- Drop "you should", "make sure to" — just state the action

## Pattern

Original: "You should always make sure to run the test suite before pushing any changes to the main branch."

Compressed: "Run tests before push to main."

## Boundaries

- ONLY compress natural language files (.md, .txt)
- NEVER modify: .py, .js, .ts, .json, .yaml, .toml, .env, .lock, .css, .html, .xml, .sql, .sh
- Original file backed up as FILE.original.md before overwriting
