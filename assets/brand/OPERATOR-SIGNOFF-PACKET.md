# Top Spirit Brand Image Operator Sign-Off Packet

This packet is the review surface for TASK-77. It does not approve the image set by itself. Andrew or Joey still needs to record an explicit APPROVE or REVISE decision before Marlin wires the assets into `docs/index.html` or before the branded page is pushed live.

For a visual review surface, open `assets/brand/operator-signoff-gallery.html`. Regenerate it after any image, manifest or QA-note change with:

```sh
python scripts/generate_operator_signoff_gallery.py --write
python scripts/generate_operator_signoff_gallery.py --check
python scripts/generate_operator_decision_template.py --write
python scripts/generate_operator_decision_template.py --check
python scripts/generate_brand_asset_lock.py --check
```

## Scope

Review the 14 static PNG renders from Tide commit `8468f32` against the resolved Top Spirit brand lane:

- Dominant ground: deep navy `#07111F` and `#101B2A`.
- Primary premium accent: gold `#D6A94A`.
- Minority software accent: reef teal `#0D9488`.
- Warm supporting tones: clay `#B45309` and cream `#F6F1E8`.
- Demo-safety: no alcohol, bottles, glasses, liquid, real faces, logos, readable text, customer data or fabricated client evidence.

The earlier SkillUI red, maroon and cyan readings are superseded for this site.

## Current Machine Status

Run from the repository root.

| Check | Current result | Meaning |
| --- | --- | --- |
| `python scripts/verify_brand_assets.py` | PASS, 14 assets checked | PNG files exist and match expected dimensions or accepted alternatives. |
| `python scripts/verify_render_log.py` | PASS in default mode | Starter render log is structurally readable while generation metadata remains pending. |
| `python scripts/verify_render_log.py --require-finalized-assets` | BLOCKED | Tide still needs final status, generated-at, reviewer, seed or generation id, final prompt and `Result:` QA notes for every image. |
| `python scripts/generate_brand_asset_lock.py --check` | PASS | The 14 static PNGs and shipped motion hero assets are pinned to exact SHA-256 digests for approval and deployment handoff. |
| `python scripts/generate_operator_decision_template.py --check` | PASS | The copy-ready TASK-77 decision template is current with the manifest, QA report and asset lock. |
| `python scripts/generate_operator_signoff_gallery.py --check` | PASS | The visual review gallery is current with the manifest and QA report. |
| `python scripts/brand_readiness.py --strict-assets` | BLOCKED | Blocks on render-log finalization and TASK-76 page integration. |
| `python scripts/verify_page_performance.py` | PASS before TASK-76 wiring | Current page has no external runtime scripts and stays inside media budgets. Re-run after wiring. |

Tide reported on the mesh that Grok Imagine and Gemini did not expose seeds in their API responses. If that remains true, the render log should record a deterministic final value such as `not-exposed` plus model, generated-at, reviewer and final prompt rather than leaving `pending`.

## Review-Needed Items

The pre-integration QA at `assets/brand/PRE-INTEGRATION-VISUAL-QA.md` found no hard demo-safety blocker in the files alone. It did flag these items for the operator decision:

| Asset id | Decision needed |
| --- | --- |
| `og-social-card` | Confirm the faint upper-left embossing does not read like baked-in text in social preview crops, or ask Tide to re-render. |
| `capabilities-card-1-mapping` | Confirm the brighter cream treatment is acceptable beside the darker capability cards, or ask Tide to darken or re-render. |
| `capabilities-card-3-literacy` | Confirm the whiteboard marks are not perceived as readable text at card size, or ask Tide to simplify. |
| `capabilities-card-4-apis` | Confirm the small marks on the gold strip are not perceived as glyphs or text, or ask Tide to remove them. |
| `walkthrough-mockup` | Confirm the chart-like pages, signature-like strokes and dashboard marks are acceptable for the largest client-facing image, or ask Tide to simplify or re-render. |

## Approval Options

### APPROVE

Use this only if all 14 images are acceptable for a polished client preview, including the review-needed items above.

Required follow-up:

1. Tide finalizes `assets/brand/RENDER-LOG.md` for all accepted images.
2. Marlin wires the images into `docs/index.html` for TASK-76.
3. Joey or Baleen runs TASK-78 integrated QA for contrast, alt text, responsive crops, no-JS behavior and final demo-safety.
4. TASK-79 live QA runs after deploy.

### REVISE

Use this if one or more images should not ship yet.

Required follow-up:

1. Name each rejected image by asset id.
2. Give Tide one concrete fix per rejected image.
3. Keep TASK-76 held unless Andrew explicitly approves wiring the remaining accepted images first.
4. Re-run the asset verifier after replacement images land.

## Decision Template

Use `assets/brand/OPERATOR-DECISION-TEMPLATE.md` as the copy-ready starting point. Copy it into a TASK-77 comment or a file under `backlog/decisions/`. Recommended path: `backlog/decisions/top-spirit-brand-image-decision.md`.

```md
Top Spirit brand image decision for TASK-77

Decision: APPROVE or REVISE
Reviewer:
Reviewed at:
Basis:
- assets/brand/PRE-INTEGRATION-VISUAL-QA.md
- assets/brand/OPERATOR-SIGNOFF-PACKET.md
- assets/brand/ASSET-LOCK.json
- python scripts/verify_brand_assets.py
- python scripts/verify_render_log.py --require-finalized-assets
- python scripts/brand_readiness.py --strict-assets

Demo-safety decision:
- No alcohol, bottles, glasses or liquid:
- No real faces:
- No logos:
- No readable text or glyph-like marks:
- No customer data or fabricated client evidence:

Brand decision:
- Navy dominant:
- Gold primary premium accent:
- Reef teal minority accent:
- Cohesive premium beverage-distribution logistics feel:

Per-image decision:
- hero-bg:
- next-step-bg:
- evidence-gates-texture-strip:
- og-social-card:
- capabilities-card-1-mapping:
- capabilities-card-2-optimisation:
- capabilities-card-3-literacy:
- capabilities-card-4-apis:
- proof-spine-thumb-export-layer:
- proof-spine-thumb-approval-envelope:
- proof-spine-thumb-audit-trail:
- proof-spine-thumb-glossary:
- proof-spine-thumb-opportunity-catalogue:
- walkthrough-mockup:

Routes:
- Tide:
- Marlin:
- Joey or Baleen:
```

After recording an APPROVE decision, run:

```sh
python scripts/generate_brand_asset_lock.py --check
python scripts/verify_operator_signoff.py
```

The checker requires `Decision: APPROVE`, a TASK-77 citation, an `ASSET-LOCK.json` citation, all 14 asset ids, and explicit demo-safety plus navy/gold/reef-teal confirmations.

## Owner Table

| Owner | Next action |
| --- | --- |
| Andrew or Joey | Record APPROVE or REVISE for all 14 images. |
| Tide | Finalize render metadata after the decision, or re-render rejected images first. |
| Marlin | Wire TASK-76 after approval or explicit permission to integrate before metadata finalization. |
| Joey or Baleen | Complete TASK-78 after the images are wired into the rendered page. |
| Any node | Run TASK-79 live QA after deploy. |
