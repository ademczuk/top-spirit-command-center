# Top Spirit Brand Image QA Checklist

Generated from `assets/brand/manifest.json` and `assets/brand/RENDER-LOG.md`.
Do not edit this checklist by hand. Update the manifest or render log, then run:

```bash
python scripts/generate_brand_qa_checklist.py --write
python scripts/generate_brand_qa_checklist.py --check
```

Use this after Tide generates TASK-72 to TASK-75 static PNGs and after Marlin wires TASK-76. It supports Joey's TASK-78 pass and does not replace manual contrast or visual inspection.

Global pass criteria:
- File exists at the manifest path and passes `python scripts/verify_brand_assets.py`.
- Page wiring passes `python scripts/verify_brand_integration.py`.
- Navy is dominant, gold is the primary premium accent, reef teal stays below the requested minority accent level and clay appears only where specified.
- No alcohol, bottles, glasses, liquid, logos, readable text, numbers, real faces or fabricated customer evidence.
- Alt text, decorative semantics, contrast, responsive crop and no-JS fallback are checked in the rendered page.

## Wide backdrops and metadata

### hero-bg

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/hero-bg.png
- Dimensions: 1920x1080, minimum 1376x768, 16:9
- Integration point: Hero background behind the first-viewport glass card
- Integration selector: `[data-task76='hero-bg']`
- Required data-task76 marker: `hero-bg`
- Expected accessibility: decorative, aria-hidden true, empty alt text
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Check white headline and a translucent glass card over the center and left thirds. Reject if gold is not visible or if teal becomes the dominant accent.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm no readable words, numbers, logos, alcohol, bottles, glasses, liquid or real faces.
- [ ] Confirm navy is dominant, gold is the primary premium accent and reef teal stays restrained.
- [ ] Composite the planned text zone and confirm contrast is still readable.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### next-step-bg

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/next-step-bg.png
- Dimensions: 1920x1080, 16:9
- Integration point: Closing next-step section backdrop
- Integration selector: `[data-task76='next-step-bg']`
- Required data-task76 marker: `next-step-bg`
- Expected accessibility: decorative, aria-hidden true, empty alt text
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Composite against white copy and a white card. Reject if the backdrop competes with text or lacks the gold premium accent.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm no readable words, numbers, logos, alcohol, bottles, glasses, liquid or real faces.
- [ ] Confirm navy is dominant, gold is the primary premium accent and reef teal stays restrained.
- [ ] Composite the planned text zone and confirm contrast is still readable.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### evidence-gates-texture-strip

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/evidence-gates-texture.png
- Dimensions: 1920x600, 16:5
- Integration point: Evidence-gates section headline texture strip
- Integration selector: `[data-task76='evidence-gates-texture']`
- Required data-task76 marker: `evidence-gates-texture`
- Expected accessibility: decorative, aria-hidden true, empty alt text
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Center must stay dark and even. Reject if it introduces literal objects or looks like a product shot.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm no readable words, numbers, logos, alcohol, bottles, glasses, liquid or real faces.
- [ ] Confirm navy is dominant, gold is the primary premium accent and reef teal stays restrained.
- [ ] Composite the planned text zone and confirm contrast is still readable.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### og-social-card

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/og-card.png
- Dimensions: 1200x630 exact, 1.91:1
- Integration point: Open Graph and Twitter summary_large_image card
- Integration selector: `head`
- Expected metadata:
  - `og:image`: `https://ademczuk.github.io/top-spirit-command-center/assets/brand/og-card.png`
  - `twitter:card`: `summary_large_image`
  - `twitter:image`: `https://ademczuk.github.io/top-spirit-command-center/assets/brand/og-card.png`
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Must be exactly 1200x630 and contain no baked-in title text. Verify title-safe space survives social preview cropping.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm no readable words, numbers, logos, alcohol, bottles, glasses, liquid or real faces.
- [ ] Confirm navy is dominant, gold is the primary premium accent and reef teal stays restrained.
- [ ] Composite the planned text zone and confirm contrast is still readable.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

## Capability card headers

### capabilities-card-1-mapping

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-1-mapping.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: Process mapping
- Integration selector: `[data-task76='capability-card'][data-capability='process-mapping'] img`
- Required data-task76 marker: `capability-card`
- Expected alt text: Process mapping capability: faceless operator reviewing an abstract workflow map
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Must match the other capability cards in light direction and style. Reject if map elements become readable.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm the image supports the named capability rather than becoming generic SaaS art.
- [ ] Confirm no readable cards, signs, dashboard numbers, logos, alcohol, bottles, glasses or real faces.
- [ ] Confirm card crop works at 4:5 and in the responsive card layout.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### capabilities-card-2-optimisation

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-2-optimisation.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: Process optimisation
- Integration selector: `[data-task76='capability-card'][data-capability='process-optimisation'] img`
- Required data-task76 marker: `capability-card`
- Expected alt text: Process optimisation capability: premium warehouse aisle showing governed value flow
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Should echo hero-bg without duplicating it. Reject if it becomes retail product imagery.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm the image supports the named capability rather than becoming generic SaaS art.
- [ ] Confirm no readable cards, signs, dashboard numbers, logos, alcohol, bottles, glasses or real faces.
- [ ] Confirm card crop works at 4:5 and in the responsive card layout.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### capabilities-card-3-literacy

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-3-literacy.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: AI literacy
- Integration selector: `[data-task76='capability-card'][data-capability='ai-literacy'] img`
- Required data-task76 marker: `capability-card`
- Expected alt text: AI literacy capability: faceless silhouette at an abstract whiteboard
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Keep it capability-led, not classroom-generic. Reject if the person is identifiable.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm the image supports the named capability rather than becoming generic SaaS art.
- [ ] Confirm no readable cards, signs, dashboard numbers, logos, alcohol, bottles, glasses or real faces.
- [ ] Confirm card crop works at 4:5 and in the responsive card layout.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### capabilities-card-4-apis

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-4-apis.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: APIs when justified
- Integration selector: `[data-task76='capability-card'][data-capability='apis-when-justified'] img`
- Required data-task76 marker: `capability-card`
- Expected alt text: APIs when justified capability: dark governed cabling detail
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Should feel like governed infrastructure, not a generic sci-fi server render.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm the image supports the named capability rather than becoming generic SaaS art.
- [ ] Confirm no readable cards, signs, dashboard numbers, logos, alcohol, bottles, glasses or real faces.
- [ ] Confirm card crop works at 4:5 and in the responsive card layout.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

## Proof-spine thumbnails

### proof-spine-thumb-export-layer

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/01-export-layer.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Export Layer
- Integration selector: `[data-task76='proof-spine'][data-step='export-layer']`
- Required data-task76 marker: `proof-spine`
- Expected alt text: Export Layer: classified exports enter before automation
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Must read clearly at 360 to 480px on a #07111F card.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm thumbnail remains legible on the #07111F proof-spine panel.
- [ ] Confirm gold or reef accents carry the signal without turning teal dominant.
- [ ] Confirm the proof-step swap preserves alt text and no-JS fallback meaning.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### proof-spine-thumb-approval-envelope

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/02-approval-envelope.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Approval Envelope
- Integration selector: `[data-task76='proof-spine'][data-step='approval-envelope']`
- Required data-task76 marker: `proof-spine`
- Expected alt text: Approval Envelope: named authority commits AI drafts
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Should make the human approval gate legible without words.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm thumbnail remains legible on the #07111F proof-spine panel.
- [ ] Confirm gold or reef accents carry the signal without turning teal dominant.
- [ ] Confirm the proof-step swap preserves alt text and no-JS fallback meaning.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### proof-spine-thumb-audit-trail

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/03-audit-trail.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Source-linked Audit Trail
- Integration selector: `[data-task76='proof-spine'][data-step='audit-trail']`
- Required data-task76 marker: `proof-spine`
- Expected alt text: Source-linked Audit Trail: claims link back to source and approver
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Gold should mark verified/source-linked points. Reject if it resembles fake data.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm thumbnail remains legible on the #07111F proof-spine panel.
- [ ] Confirm gold or reef accents carry the signal without turning teal dominant.
- [ ] Confirm the proof-step swap preserves alt text and no-JS fallback meaning.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### proof-spine-thumb-glossary

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/04-glossary.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Business Glossary
- Integration selector: `[data-task76='proof-spine'][data-step='business-glossary']`
- Required data-task76 marker: `proof-spine`
- Expected alt text: Business Glossary: shared terms connect reports and agents
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Must communicate agreed definitions through structure and highlights, not text.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm thumbnail remains legible on the #07111F proof-spine panel.
- [ ] Confirm gold or reef accents carry the signal without turning teal dominant.
- [ ] Confirm the proof-step swap preserves alt text and no-JS fallback meaning.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

### proof-spine-thumb-opportunity-catalogue

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/05-opportunity-catalogue.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Opportunity Catalogue
- Integration selector: `[data-task76='proof-spine'][data-step='opportunity-catalogue']`
- Required data-task76 marker: `proof-spine`
- Expected alt text: Opportunity Catalogue: ranked value plays by effort, risk and evidence
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Should show prioritisation without any numeric or client-specific data.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm thumbnail remains legible on the #07111F proof-spine panel.
- [ ] Confirm gold or reef accents carry the signal without turning teal dominant.
- [ ] Confirm the proof-step swap preserves alt text and no-JS fallback meaning.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.

## Walkthrough control-room render

### walkthrough-mockup

- Task: TASK-75
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/walkthrough-control-room.png
- Dimensions: 1200x1440 5:6 or 784x943 existing-card
- Integration point: Walkthrough section control-room image
- Integration selector: `[data-task76='walkthrough-image']`
- Required data-task76 marker: `walkthrough-image`
- Expected alt text: Walkthrough control room: governed beverage distribution overview
- Render-log status: pending
- Seed or generation id: pending
- Render QA note: Place on a #F6F1E8 cream swatch. Record whether the final ratio is 1200x1440 or 784x943.

Checks:
- [ ] File exists and dimensions match the manifest.
- [ ] Render-log status, seed or generation id and reviewer notes are updated.
- [ ] Confirm the chosen ratio is recorded in RENDER-LOG.md.
- [ ] Confirm the control-room scene reads as premium operations and not fabricated client evidence.
- [ ] Confirm the image does not break the walkthrough card layout on mobile, tablet or desktop.
- [ ] Final result is routed: pass, Marlin markup fix, Tide re-render or Andrew sign-off question.
