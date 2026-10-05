---
name: amp-handoff
description: Hand the current conversation off to a fresh Amp thread that picks up the work immediately. Use when the user asks to continue work in a new agent session.
argument-hint: "What will the next session be used for?"
---

Write a handoff summary of the current conversation, then create a fresh Amp thread with `create_thread`. Pass the summary as its prompt and use a concise descriptive `title`. The new thread must own the work and verify its outcome.

If the handoff depends on unpushed source-thread changes, transfer the needed files with `upload_thread_file` after creating the thread. State the repository, distinguish local `main` from `origin/main`, and name each transferred path in the handoff.

Include a "Suggested skills" section in the prompt, naming relevant skills the next thread should load.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact API keys, passwords, and personally identifiable information before passing the prompt.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.
