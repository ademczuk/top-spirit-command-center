# Top Spirit Static Brand Image Pre-Integration QA

Manual visual QA for Tide commit `8468f32`, run before Marlin wires TASK-76.

This report does not replace `assets/brand/RENDER-LOG.md` or the generated `assets/brand/QA-CHECKLIST.md`. Tide still needs to finalize render-log status, seed or generation id, final prompt and review notes. Marlin still needs to wire the assets into `docs/index.html` before final TASK-78 contrast, alt text, responsive and no-JS QA can pass.

## Machine Checks

- `python scripts/verify_brand_assets.py`: pass, 14 assets checked.
- `python scripts/brand_readiness.py --strict-assets`: blocked on render-log finalization and brand integration.
- `python scripts/verify_page_performance.py`: pass before TASK-76 wiring; current page references existing media only.

## Summary

- Hard blockers found in the image files alone: none.
- Route to Tide before sign-off: finalize render-log metadata; review the flagged image-quality risks below.
- Route to Marlin for integration: wire only after render-log finalization or with Andrew accepting the open Tide QA notes.
- Route to Andrew for brand sign-off: decide whether the flagged review-needed items are acceptable for a polished client preview or need re-render.

## Asset Findings

| Asset id | Result | Notes | Route |
| --- | --- | --- | --- |
| `hero-bg` | Pass | Strong navy control-room scene, clear gold rail accent, restrained teal overlays, no visible alcohol, logo, face or readable text. Suitable as a decorative hero layer with scrim. | Marlin contrast check after wiring |
| `next-step-bg` | Pass | Low-contrast dark decision-room backdrop with gold table edge and muted teal schematic. Suitable behind closing copy if dimmed or overlaid. | Marlin contrast check after wiring |
| `evidence-gates-texture-strip` | Pass | Pure material texture, dark center, gold and clay detail. No objects or text. | Marlin opacity check after wiring |
| `og-social-card` | Review needed | On-palette and title-safe, but the upper-left embossing reads like faint letterforms at a glance. Verify in social preview crop that it does not look like baked-in text. | Andrew sign-off or Tide re-render if preview looks textual |
| `capabilities-card-1-mapping` | Review needed | Correct process-map concept with backs-only silhouette, but it is much creamier and brighter than the other capability cards. It may overpower the dark card set. | Andrew sign-off or Tide darken/re-render |
| `capabilities-card-2-optimisation` | Pass | Cohesive navy warehouse abstraction, no people, strong gold route and restrained teal nodes. | Marlin card crop check |
| `capabilities-card-3-literacy` | Review needed | Good backs-only literacy scene, but the whiteboard includes many text-like strokes and panel blocks. They are not readable, but should be checked at card size. | Andrew sign-off or Tide simplify if it reads textual |
| `capabilities-card-4-apis` | Review needed | Strong governed-infrastructure feel, but small glyph-like marks appear on the gold strip. Treat as a no-readable-text risk until reviewed. | Andrew sign-off or Tide remove glyph marks |
| `proof-spine-thumb-export-layer` | Pass | Clear abstract export-gate motif with dark base, gold path and restrained teal nodes. | Marlin card-background check |
| `proof-spine-thumb-approval-envelope` | Pass | Minimal approval-envelope abstraction, strong gold outline, no readable text. | Marlin card-background check |
| `proof-spine-thumb-audit-trail` | Pass | Clear vertical source-chain motif, dark base and gold verified nodes. | Marlin card-background check |
| `proof-spine-thumb-glossary` | Pass | Abstract term-card grid with canonical gold card and teal connectors. No text. | Marlin card-background check |
| `proof-spine-thumb-opportunity-catalogue` | Pass | Abstract effort/value grid, gold top-ranked tile and teal routing. No labels or numbers. | Marlin card-background check |
| `walkthrough-mockup` | Review needed | Premium scene and page-compatible cream ground, but it contains chart-like pages, signature-like strokes and text-like dashboard marks. Not clearly readable, but higher risk because it is the largest client-facing image. | Andrew sign-off or Tide simplify/re-render |

## Final TASK-78 Still Required

After TASK-76 wiring, run the full integrated pass:

1. Verify `python scripts/verify_brand_integration.py` passes.
2. Verify `python scripts/brand_readiness.py --strict-assets` passes after render-log finalization.
3. Check actual text-over-image contrast for hero, evidence-gates and next-step sections.
4. Check alt text and decorative semantics in the rendered page.
5. Check responsive crops at mobile, tablet and desktop widths.
6. Check reduced-motion and no-JS behavior for proof-spine swapping.
