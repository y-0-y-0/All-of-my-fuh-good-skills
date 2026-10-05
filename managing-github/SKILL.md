---
name: managing-github
description: "Uses the gh CLI to interact with GitHub repositories, pull requests, issues, releases, collaborators, and CI workflows. Use when checking PR status or merge readiness, viewing CI runs, managing issues, creating or merging pull requests, querying GitHub data, or listing releases and collaborators."
---

# GitHub Skill

Use the `gh` CLI to interact with GitHub repositories, issues, pull requests, and CI.

## When to Use

Use this skill when:

- Checking PR status, reviews, or merge readiness
- Viewing CI/workflow run status and logs
- Creating, closing, or commenting on issues
- Creating or merging pull requests
- Querying the GitHub API for repository data
- Listing repositories, releases, or collaborators

Do not use this skill when:

- Performing local git operations such as commit, push, pull, or branch management; use `git` directly
- Working with non-GitHub repositories such as GitLab, Bitbucket, or self-hosted services; use the relevant CLI
- Cloning repositories; use `git clone`
- Reviewing actual code changes; use a coding-agent skill or inspect the files directly
- Reviewing complex multi-file diffs; use a coding-agent skill or inspect the files directly

## Setup

Authenticate once with:

```bash
gh auth login
```

Verify authentication with:

```bash
gh auth status
```

## Common Commands

### Pull Requests

```bash
# List PRs
gh pr list --repo owner/repo

# Check CI status
gh pr checks 55 --repo owner/repo

# View PR details
gh pr view 55 --repo owner/repo

# Create PR
gh pr create --title "feat: add feature" --body "Description"

# Merge PR
gh pr merge 55 --squash --repo owner/repo
```

### Issues

```bash
# List issues
gh issue list --repo owner/repo --state open

# Create issue
gh issue create --title "Bug: something broken" --body "Details..."

# Close issue
gh issue close 42 --repo owner/repo
```

### CI/Workflow Runs

```bash
# List recent runs
gh run list --repo owner/repo --limit 10

# View specific run
gh run view <run-id> --repo owner/repo

# View failed step logs only
gh run view <run-id> --repo owner/repo --log-failed

# Re-run failed jobs
gh run rerun <run-id> --failed --repo owner/repo
```

### API Queries

```bash
# Get PR with specific fields
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# List all labels
gh api repos/owner/repo/labels --jq '.[].name'

# Get repo stats
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'
```

## JSON Output

Most commands support `--json` with `--jq` filtering for structured output:

```bash
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
gh pr list --json number,title,state,mergeable --jq '.[] | select(.mergeable == "MERGEABLE")'
```

## Templates

### PR Review Summary

```bash
PR=55 REPO=owner/repo
echo "## PR #$PR Summary"
gh pr view $PR --repo $REPO --json title,body,author,additions,deletions,changedFiles \
  --jq '"**\(.title)** by @\(.author.login)\n\n\(.body)\n\n📊 +\(.additions) -\(.deletions) across \(.changedFiles) files"'
gh pr checks $PR --repo $REPO
```

### Issue Triage

```bash
gh issue list --repo owner/repo --state open --json number,title,labels,createdAt \
  --jq '.[] | "[\(.number)] \(.title) - \([.labels[].name] | join(", ")) (\(.createdAt[:10]))"'
```

## Notes

- Always specify `--repo owner/repo` when the current directory is not a git repository.
- Use GitHub URLs directly, for example: `gh pr view https://github.com/owner/repo/pull/55`.
- Rate limits apply; use `gh api --cache 1h` for repeated queries.
