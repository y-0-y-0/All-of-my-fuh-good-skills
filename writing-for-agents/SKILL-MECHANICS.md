# Skill mechanics

The skill-specific branch of [`writing-for-agents`](SKILL.md): what changes when the document is a skill (frontmatter, the invocation choice, and router skills). Everything else about writing it is the universal reference in `SKILL.md`.

## Discovery and invocation

Amp reads every skill's `name` and `description` at startup. It loads the full `SKILL.md` only when the user request matches the description or the user names the skill. Every Amp skill therefore needs a clear description stating both what it does and when to use it.

The description is the discovery surface. Include distinct trigger words that users actually write, but do not repeat the body. Keep detailed workflows in `SKILL.md` and supporting material in sibling files so they load only when needed.

Shared reference needed by several skills can live in one skill directory when its description makes the reference discoverable. Keep unrelated background material in ordinary repository documentation instead.

## Splitting by trigger

Split a skill when it has an independently useful task with a distinct trigger phrase, or when its instructions exceed the main skill's scope. Each split adds a startup description, so keep the split only when the independent discovery improves routing.

## Router skills

Use a **router skill** when several workflows overlap and users need help choosing one. The router names each workflow and its trigger, then loads the selected skill. Its description must state that it chooses a workflow and when to use it.
