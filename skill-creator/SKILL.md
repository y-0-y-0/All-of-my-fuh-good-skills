---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
license: Apache-2.0
compatibility: cline
metadata:
  author: https://github.com/anthropics/skills
  version: "1.0.0"
  domain: agent-workflows
  triggers: skill, create skill, make skill, write skill, edit skill, improve skill, optimize skill, skill development, skill iteration, test skill, benchmark skill, skill performance, skill evaluation, eval, skill evals
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

At a high level, the process of creating a skill goes like this:

- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them
- Help the user evaluate the results both qualitatively and quantitatively
  - While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  - Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
- Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
- Repeat until you're satisfied
- Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a draft, write the test cases, figure out how they want to evaluate, run all the prompts, and repeat.

On the other hand, maybe they already have a draft of the skill. In this case you can go straight to the eval/iterate part of the loop.

Of course, you should always be flexible and if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.

Then after the skill is done (but again, the order is flexible), you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.

Cool? Cool.

## Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently that it started), there's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google "how to install npm". On the other hand, the bulk of users are probably fairly computer-literate.

So please pay attention to context cues to understand how to phrase your communication! In the default case, just to give you some idea:

- "evaluation" and "benchmark" are borderline, but OK
- for "JSON" and "assertion" you want to see serious cues from the user that they know what those things are before using them without explaining them

It's OK to briefly explain terms if you're in doubt, and feel free to clarify terms with a short definition if you're unsure if the user will get it.

---

## Creating a skill

### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow the user wants to capture (e.g., they say "turn this into a skill"). If so, extract answers from the conversation history first — the tools used, the sequence of steps, corrections the user made, input/output formats observed. The user may need to fill the gaps, and should confirm before proceeding to the next step.

1. What should this skill enable Claude to do?
2. When should this skill be invoked? What user queries or situations trigger it?
3. How does the user want to evaluate the results?

### Draft the Skill

Write the skill following the structure outlined in `template/TEMPLATE.md`. Key elements:

- **Title**: Clear, descriptive name
- **Description**: When the skill should be used (triggers)
- **Instructions**: Step-by-step guidance for Claude
- **Examples**: Specific input/output examples
- **Constraints**: What Claude must/must not do
- **References**: Links to detailed guidance when needed

### Create Test Cases

Create evals in `evals/evals.json` with:

- `prompt`: The task to execute
- `expected_output`: What success looks like
- `expectations`: Verifiable statements about the output

Run at least 3-5 evals before iterating. For benchmarks, run 10-20.

### Run Evaluations

Execute the skill against test prompts, capturing outputs in a structured format. Compare results with and without the skill to measure impact.

### Evaluate Results

With the user, review outputs qualitatively. Then:

1. Create `benchmark.json` with aggregate metrics
2. Run `eval-viewer/generate_review.py` to generate an HTML review page
3. Analyze patterns and anomalies

### Iterate

Revise the skill based on evaluation feedback. Repeat the test cycle.

### Package

When satisfied, save as `.skill` file using the `package_skill.py` script.

---

## Reference files

The agents/ directory contains instructions for specialized subagents. Read them when you need to spawn the relevant subagent.

- `agents/grader.md` — How to evaluate assertions against outputs
- `agents/comparator.md` — How to do blind A/B comparison between two outputs
- `agents/analyzer.md` — How to analyze why one version beat another

The references/ directory has additional documentation:
- `references/schemas.md` — JSON structures for evals.json, grading.json, etc.

---

## Core Workflow

1. Figure out what the skill is about
2. Draft or edit the skill
3. Run claude-with-access-to-the-skill on test prompts
4. With the user, evaluate the outputs:
   - Create benchmark.json and run `eval-viewer/generate_review.py` to help the user review them
   - Run quantitative evals
5. Repeat until you and the user are satisfied
6. Package the final skill and return it to the user
