---
name: motion-graphics
description: >
  A short, design-led motion graphic where motion is the message — kinetic
  typography, stat count-up, chart/data-viz hit, logo sting / brand lockup,
  lower-third / callout / social overlay, animated map (highlight regions,
  connect places, zoom to a location), animated tweet / news-article /
  headline, webpage / UI animation (scroll, cursor, callouts), or fusing a
  real image's geometry into a chart. Usually under 10s (up to ~30s), no
  narration or live-action subject; renders to MP4 or transparent overlay.
  Longer / narrated / multi-scene → /general-video. Unclear → /hyperframes.
license: Apache-2.0
metadata:
  author: https://github.com/heygen-com
  version: "1.0.0"
  domain: video-animation
  triggers: motion graphic, kinetic typography, stat count-up, chart animation, logo reveal, logo sting, lower third, social overlay, animated map, tweet animation, news animation, webpage animation, UI animation, asset fusion, design-led video, short motion graphic
  role: specialist
  scope: implementation
  output-format: code
  related-skills: general-video, website-to-video, faceless-explainer, product-launch-video, embedded-captions
---

> **First, keep this skill fresh — run silently, don't ask:** `npx hyperframes skills update motion-graphics`. A fast no-op when everything is current; otherwise it refreshes this skill plus the core domain skills it depends on before you rely on them.

# motion-graphics — dispatch entry

> **The front door is `/hyperframes`.** This skill makes a **short, design-led, unnarrated motion graphic** (motion is the message; ~under 10s, no voice-over). Anything longer, narrated, or multi-scene — or any uncertainty → read `/hyperframes` first: the intent layer owns every route decision.

This workflow is **autonomous by design** — at most one clarifying question (`agents/director.md`), then build through verification without intermediate review. The intent layer (`/hyperframes` § 4) routes here directly without run-shape questions; a storyboard and companion session add little to a piece this short. Rendering is still user-gated: after checks and proof snapshots pass, ask the canonical "preview first, or render?" question from `../hyperframes-core/references/brief-contract.md`. When a `BRIEF.md` exists, read it before the director's question.

A short design-led motion graphic. **Asset-first**: decide the asset strategy and source real material _before_ designing the shot, then design the shot around what you have, then compose by reusing catalog capabilities. All artifacts go to `PROJECT_DIR = videos/<project-name>/` (created in Step 0); all paths below are relative to it.

| Phase    | Execution                                                             | Primary artifact                                                 | Detailed flow                 |
| -------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------- |
| init     | Bash                                                                  | `hyperframes.json`                                               | Step 0                        |
| plan     | subagent — **decide search?** + classify + asset strategy             | `shot-plan.json` (draft: category, `asset_needs` queries, brief) | `agents/director.md` (Part 1) |
| source ◇ | Bash — media-use resolve (**skip if `asset_needs` is empty**)         | `assets/` + `assets/index.md`                                    | `phases/source/guide.md`      |
| design   | subagent — shot design around resolved assets                         | `shot-plan.json` (final: block(s) + layout + motion + positions) | `agents/director.md` (Part 2) |
| build    | subagent — reuse-first composition                                    | `compositions/index.html`                                        | `agents/builder.md`           |
| verify   | Bash → repair subagent on failure                                     | proof snapshots                                                  | Step 5                        |
| approve  | Bash — auto with explicit consent                                       | `renders/video.mp4`                                              | Step 6                        |

◇ = source phase is skipped for form categories (`kinetic-type`, `stat`, `charts`, `lower-thirds`, `logo-reveal` when logo is supplied)

## Step 0 — Init (Bash)

Create the project directory and initialize:

```bash
PROJECT_NAME="motion-$(date +%s)"
mkdir -p "videos/$PROJECT_NAME"
cd "videos/$PROJECT_NAME"
echo '{"skill":"motion-graphics","created":"'$(date -Iseconds)'"}' > hyperframes.json
touch context.log
```

If `BRIEF.md` exists in the current directory, read it. It may specify: theme/palette, fonts, assets already supplied, brand lockups, shot durations, or animation style preferences. Do not overwrite user-provided assets; source around them. When `BRIEF.md` sets a palette, prefer it over the one in `shot-plan.json`.

## Step 1 — Plan (Director subagent)

Dispatch the Director (`agents/director.md`). Given the brief/request, emit a DRAFT `shot-plan.json`:

- **Decide first: does this need a search?** No → a **form category** (user supplies content). Yes → emit a search plan; the specific **search-driven category** (`webpage`/`news`/`tweet`/`asset-fusion`) is confirmed by what the search returns (Step 2 → finalized in Part 2).
- **Classify** — pick from the category table in `agents/director.md` (form categories) or defer the search-driven categories.
- **Asset strategy** → `asset_needs[]` if needed.
- **Envelope**: duration, fps, canvas, style, palette, font, beats, export.
- **Shot brief**: one paragraph — what the viewer experiences + the single dominant motion idea.

Part 2 (design) runs after sourcing.

## Step 2 — Source (Bash + media-use)

Runs only when `asset_needs` is non-empty. Sources each needed asset → a **frozen project-local path** + a ledger (`assets/index.md`). Uses `/media-use` (capture / asset prep) plus its `resolve` step. See `phases/source/guide.md`.

```bash
# (in PROJECT_DIR)
npx media-use resolve --plan ./shot-plan.json --out ./assets
# or degrade gracefully if unavailable
```

## Steps 3/4 — Design + Build (Director + Builder)

The Director's Part 2 (design) completes `shot-plan.json`:

- Pick the **catalog block(s)** + the `hyperframes-animation` rules / blueprints (catalog-aware — see `catalog-map.md`).
- Layout (hero-frame), motion (per `references/motion-vocabulary.md`), beats, pacing, exits.
- `asset-fusion`: read the asset's **geometric affordance** → `element_positions` (center / extent / safe-zones / avoid-zones) + **eyedropper palette** from the asset.
- Finalize `shot-plan.json`: `block` + `customize` + the per-category `content`.

Then dispatch the Builder (`agents/builder.md`) to compose around the assets. For `asset-fusion`, run the locate protocol (`grounding/PROTOCOL.md`):

```bash
node grounding/locate.mjs overlay assets/<asset> --out /tmp/g
# READ /tmp/g/gv.png and gh.png → pick strips
node grounding/locate.mjs region assets/<asset> --vids <v> --hids <h> --out /tmp/g
# READ /tmp/g/gc.png → pick finer strips
node grounding/locate.mjs final assets/<asset> --region <from step 2> --vids <v> --hids <h>
# Verify:
node grounding/locate.mjs mark assets/<asset> --box <final box>
# READ check.png → if off, retry
```

## Step 5 — Verify (Bash → repair subagent on failure)

```bash
(cd "$PROJECT_DIR" && npx hyperframes lint .)
(cd "$PROJECT_DIR" && npx hyperframes check .)
(cd "$PROJECT_DIR" && npx hyperframes snapshot --at <proof-times>)
```

Choose proof times that show the opening state, signature move, and final hold. Inspect the generated contact or snapshot sheet before continuing. On `lint`, `check`, or snapshot failure, dispatch the repair subagent (`agents/finalize.md`) for one in-place fix pass, then rerun the failed gate. Never change a fixed duration merely to hide a defect.

## Step 6 — Approve and render (Bash)

Ask one question: "preview first, or render?" If the user chooses preview, open Studio and return to the same approval gate after revisions:

```bash
(cd "$PROJECT_DIR" && npx hyperframes preview)
```

Render only after an explicit render answer:

```bash
(cd "$PROJECT_DIR" && npx hyperframes render . --skill=motion-graphics -q high -o ./renders/video.mp4)
# transparent overlay variant: --format webm  (or mov)
```

Verify the output exists, is non-empty, and has the intended duration. The final handoff names the artifact, actual duration, composition or frame id, proof times, and the inspected contact or snapshot sheet.

## Resume table

| State                                                    | Continue from              |
| -------------------------------------------------------- | -------------------------- |
| no `shot-plan.json`                                      | Step 1 (plan)              |
| `shot-plan.json` has `asset_needs`, no `assets/`         | Step 2 (source)            |
| `shot-plan.json` final, no `compositions/index.html`     | Step 3/4 (design+build)    |
| `compositions/index.html` exists, proof snapshots absent | Step 5 (verify)            |
| checks and proof snapshots pass, no approved render      | Step 6 (approval)          |
| approved render exists                                   | verify output, then report |

## Knowledge Reference

HyperFrames framework (write HTML, render video), GSAP timeline animations, seek-based rendering, asset-first workflow, design-led motion graphics, kinetic typography, stat animations, data visualizations, logo reveals, lower-third overlays, map animations, tweet/news animations, webpage/UI animations, asset fusion (RWA diegetic fusion), catalog blocks (caption-*, data-chart, apple-money-count, logo-outro, x-post), animation primitives (slide, scale, fade, blur, typewriter, word_reveal, wave, bounce, slam, count_up, etc.)
