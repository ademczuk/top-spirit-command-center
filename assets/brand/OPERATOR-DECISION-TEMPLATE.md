# Top Spirit Brand Image Decision Template

Copy this file to `backlog/decisions/top-spirit-brand-image-decision.md` when Andrew or Joey is ready to record the TASK-77 decision. Do not treat this template as approval.

Top Spirit brand image decision for TASK-77

Decision: APPROVE or REVISE
Reviewer:
Reviewed at:

Basis:
- assets/brand/PRE-INTEGRATION-VISUAL-QA.md
- assets/brand/OPERATOR-SIGNOFF-PACKET.md
- assets/brand/operator-signoff-gallery.html
- assets/brand/ASSET-LOCK.json
- python scripts/verify_brand_assets.py
- python scripts/generate_brand_asset_lock.py --check
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
  - Current QA: Pass
  - Review note: Strong navy control-room scene, clear gold rail accent, restrained teal overlays, no visible alcohol, logo, face or readable text. Suitable as a decorative hero layer with scrim.
  - Route if not approved: Marlin contrast check after wiring
  - Asset lock: cdf32b4d00f1 bytes=1854350
- next-step-bg:
  - Current QA: Pass
  - Review note: Low-contrast dark decision-room backdrop with gold table edge and muted teal schematic. Suitable behind closing copy if dimmed or overlaid.
  - Route if not approved: Marlin contrast check after wiring
  - Asset lock: ab4bcc7d8568 bytes=1488171
- evidence-gates-texture-strip:
  - Current QA: Pass
  - Review note: Pure material texture, dark center, gold and clay detail. No objects or text.
  - Route if not approved: Marlin opacity check after wiring
  - Asset lock: a4d95b91c480 bytes=1891698
- og-social-card:
  - Current QA: Review needed
  - Review note: On-palette and title-safe, but the upper-left embossing reads like faint letterforms at a glance. Verify in social preview crop that it does not look like baked-in text.
  - Route if not approved: Andrew sign-off or Tide re-render if preview looks textual
  - Asset lock: 80f25bbc9b4f bytes=867594
- capabilities-card-1-mapping:
  - Current QA: Review needed
  - Review note: Correct process-map concept with backs-only silhouette, but it is much creamier and brighter than the other capability cards. It may overpower the dark card set.
  - Route if not approved: Andrew sign-off or Tide darken/re-render
  - Asset lock: 8fa9a4edb559 bytes=1092606
- capabilities-card-2-optimisation:
  - Current QA: Pass
  - Review note: Cohesive navy warehouse abstraction, no people, strong gold route and restrained teal nodes.
  - Route if not approved: Marlin card crop check
  - Asset lock: 9648a3c36800 bytes=1093273
- capabilities-card-3-literacy:
  - Current QA: Review needed
  - Review note: Good backs-only literacy scene, but the whiteboard includes many text-like strokes and panel blocks. They are not readable, but should be checked at card size.
  - Route if not approved: Andrew sign-off or Tide simplify if it reads textual
  - Asset lock: 24c0a5423eca bytes=1377148
- capabilities-card-4-apis:
  - Current QA: Review needed
  - Review note: Strong governed-infrastructure feel, but small glyph-like marks appear on the gold strip. Treat as a no-readable-text risk until reviewed.
  - Route if not approved: Andrew sign-off or Tide remove glyph marks
  - Asset lock: e6821d0edb9e bytes=1608421
- proof-spine-thumb-export-layer:
  - Current QA: Pass
  - Review note: Clear abstract export-gate motif with dark base, gold path and restrained teal nodes.
  - Route if not approved: Marlin card-background check
  - Asset lock: ab44c70be757 bytes=1210955
- proof-spine-thumb-approval-envelope:
  - Current QA: Pass
  - Review note: Minimal approval-envelope abstraction, strong gold outline, no readable text.
  - Route if not approved: Marlin card-background check
  - Asset lock: 233c55e413df bytes=1287625
- proof-spine-thumb-audit-trail:
  - Current QA: Pass
  - Review note: Clear vertical source-chain motif, dark base and gold verified nodes.
  - Route if not approved: Marlin card-background check
  - Asset lock: 2bba2eb21716 bytes=1075242
- proof-spine-thumb-glossary:
  - Current QA: Pass
  - Review note: Abstract term-card grid with canonical gold card and teal connectors. No text.
  - Route if not approved: Marlin card-background check
  - Asset lock: 8b985d2d35df bytes=709089
- proof-spine-thumb-opportunity-catalogue:
  - Current QA: Pass
  - Review note: Abstract effort/value grid, gold top-ranked tile and teal routing. No labels or numbers.
  - Route if not approved: Marlin card-background check
  - Asset lock: 19e2d3203540 bytes=1386501
- walkthrough-mockup:
  - Current QA: Review needed
  - Review note: Premium scene and page-compatible cream ground, but it contains chart-like pages, signature-like strokes and text-like dashboard marks. Not clearly readable, but higher risk because it is the largest client-facing image.
  - Route if not approved: Andrew sign-off or Tide simplify/re-render
  - Asset lock: f902318a7e2f bytes=1744245

Routes:
- Tide:
- Marlin:
- Joey or Baleen:

After filling this decision, run:

```sh
python scripts/generate_brand_asset_lock.py --check
python scripts/verify_operator_signoff.py
```
