# maps — category module

Geographic motion: highlight regions, connect places, zoom to a location. **First decision: does the shot need a real basemap** (satellite/street/terrain imagery, globe, or zoom to a real address)? That picks the lane.

## Plan (Director)

Set `content.lane` first:

- **vector** (default) — stylized region shapes, no real imagery. Native + live in HF, cheap. `asset_needs: []`.
- **basemap** — needs real satellite/dark tiles, globe, or zoom-to-real-place. `asset_needs: [{ type: "map-bake", … }]`. **Bake the imagery in Source**: HF forbids render-time network and requires determinism, so live tiles (which re-fetch and can change per render) can't be the imagery layer — baking freezes it (and is smooth as a bonus). See Basemap lane + Determinism.

`content`: `{ lane, shot: highlight|flow|choropleth|labels|flag|pin-rollout|zoom-to, regions[], points[], basemap: satellite|dark, palette, headline, overlays: [label|pin|callout-card] }`.

`overlays` are independent of `shot` and work in both lanes. **`callout-card`** = a pinned card (flag chip + stat + progress bar) — this is the "documentary popup" (top #13); compose it on any zoom-to/highlight shot rather than treating it as its own shot.

## Vocabulary / leans on

**Vector lane** (D3 + TopoJSON — reuse the existing map family, don't duplicate):

- Reuse: `us-map` (+bubble/hex/flow), `world-map`, `spain-map`.
- **Hand-author** these (NOT in the catalog — build per the signatures below, don't expect an `add`): `geo-highlight` (N countries colored + labels + border pulse), `geo-flow` (world arcs / hub network), `flag-borders` (flag clipped to a country), `pin-rollout` (cities pulse in sequence + counter).
- Signature: country fill-in stagger · pin drop + pulse ring · arc `stroke-dashoffset` draw-on + flyer · choropleth color reveal · **viewBox** zoom.

**Basemap lane** (MapLibre, baked in Source — validated pipeline, `bake-basemap.mjs`, fully env-parametric — runs for any country, not just the prototypes):

- **Bake** `bake-basemap.mjs` (puppeteer + MapLibre; env-driven: `NAME STYLE COUNTRIES CENTER ZSTART ZEND PITCH BEARING FPS DUR`): drive the camera **zoom→hold** (`easeInOutCubic`) and **`await map.once('idle')` before every frame** so each frame has complete tiles (Remotion `delayRender` technique → no tile pop). The helper resolves Chrome itself, pins deps exactly, derives the overseas-territory filter per subject, and **fails loud on idle-timeout** (suspect frames → non-zero exit). External deps: the pinned CDN libs (maplibre/topojson/world-atlas) + the Esri/CARTO tile endpoints are third-party — re-verify availability + ToS on any version bump. `preserveDrawingBuffer:true`, `fadeDuration:0`. The helper then **encodes the frames to an all-intra MP4 itself** (`ffmpeg -framerate FPS -i f%04d.png -c:v libx264 -g 1 -pix_fmt yuv420p`) and writes everything to **`$OUT` (default `cwd`)**, not the skill dir → `<NAME>.mp4` + `<NAME>-coords.json`.
- **Export geo→screen** at the hold view: `map.project()` each requested country → `<NAME>-coords.json` = `{ view, countries: [{ name, color, d (SVG path), bbox, label }] }`. The camera holds static after the zoom, so these paths stay pixel-aligned. `label` is an **approximate** anchor (vertex-average of the mainland ring — for concave countries nudge per Legibility). Consume `coords.countries[i]`; the `smooth-frde2`/`smooth-flag` example dirs predate this helper and use a flat `{fr,de,…}` shape, so adapt their wiring.
- **Builder**: `<video>` basemap on track 0 + an **SVG overlay** that, during the hold, animates country **borders (`stroke-dashoffset` draw-on)** + **fills (colour-block reveal)** + labels/pins/cards — all geo-aligned via `coords.json`.

## Legibility (hard rule)

Offset labels from the highlighted shape and from each other; clamp to the safe area; a callout pill must not sit on another label or a border. A key element stays readable ≥~0.3s.

## Attribution (hard rule)

Real basemap imagery carries usage terms — bake a credit element into the composition whenever a basemap is on screen (Esri satellite → "Esri, Maxar, Earthstar Geographics"; CARTO → "© CARTO, © OpenStreetMap"). A small low-corner label. Non-negotiable for anything published.

## Determinism (hard rules)

- Drive everything from the seek clock; **never `tl.call`** for stateful updates (counters, text) → proxy tween + `onUpdate`.
- SVG zoom = animate **viewBox** (don't hand-compute group transform origins).
- Centered overlays (cards/labels using `transform: translate(-50%,…)` to center): animate **opacity only**, or wrap in an outer centered div — GSAP animating `y`/`scale` overwrites the whole transform and kills the centering.
- Country geometry: filter to the polygon(s) **in a lon/lat box around the subject** — world-atlas bundles overseas territories that blow up the bbox (France + Guiana). Keep near islands (Corsica, Sicily), drop far ones.
- **Tile world-scale**: MapLibre's internal world width is `512·2^zoom` regardless of the raster `tileSize`. Esri/CARTO raster → `tileSize:256` (correct); a 512px / @2x / retina / vector source needs `tileSize:512` or every zoom level is off by one.
- **Antimeridian**: a feature crossing ±180° (Russia, Fiji, NZ) smears under per-vertex `map.project()`. Unwrap longitudes around the camera-center ref before projecting.
- **Smoothness = per-frame complete tiles + eased camera.** In the bake, `await map.once('idle')` before each screenshot and ease the camera with `easeInOutCubic`.
- **Overlay alignment**: project feature borders at a **held** camera and only animate the overlay during the hold — a moving camera + a fixed projected path drift apart.
- **Pre-hold hidden state**: an overlay revealed _at_ the hold must be `gsap.set` to its hidden state at build time (`scaleX:0`, full `stroke-dasharray`, `opacity:0`) — a bare `fromTo` does **not** apply its "from" until the tween starts, so the element otherwise shows at its natural (visible, mispositioned) state during the zoom-in.

## Out of scope

3D photorealistic landmarks (Cesium territory) · per-country / per-template blocks (parametrize instead) · charts (→ `charts`).

## Register

`director.md` classifier line (the lane fork) + `catalog-map.md` `maps/geo` row (add the basemap lane). Phase pipeline untouched.
