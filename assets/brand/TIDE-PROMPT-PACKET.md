# Tide Static Image Prompt Packet

Generated from `assets/brand/manifest.json` and `assets/brand/RENDER-LOG.md`.
Do not edit this packet by hand. Update the manifest or render log, then run:

```bash
python scripts/generate_brand_prompt_packet.py --write
python scripts/generate_brand_prompt_packet.py --check
```

Use this packet for TASK-72 to TASK-75 static PNG generation. The shipped motion hero is tracked separately under `motionAssets` in the manifest.

Global constraints:
- PNG output unless an explicit later task changes format
- no alcohol, bottles, glasses or liquid
- no real faces; use faceless backs-only silhouettes only where required
- no logos
- no readable text, numbers, customer data or fabricated client evidence
- navy ground, gold primary premium accent, reef teal minority platform accent
- Use the resolved navy, gold, reef teal, clay and cream direction from `assets/brand/tokens.json`.
- Keep generated images free of readable words, numbers, logos, real faces, alcohol, bottles, glasses and liquid.
- After generation, update `assets/brand/RENDER-LOG.md` with status, seed or generation id, reviewer and crop or upscale notes.

## TASK-72

### hero-bg

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/hero-bg.png
- Dimensions: 1920x1080, minimum 1376x768, 16:9
- Integration point: Hero background behind the first-viewport glass card
- Current status: pending
- Seed: pending

Prompt:

```text
Cinematic premium distribution operations control room at night, deep navy editorial-luxury environment, abstract export files and approval gates on dark glass panels, one clear gold rim light along desks and rails, very restrained reef teal data glow below 15 percent of accent area, low contrast center with generous empty space for white headline and glass card overlay, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces.
```

Negative prompt:

```text
alcohol, bottles, glasses, liquid, brand logos, readable words, numbers, faces, portraits, fake client dashboards, stock photo look, teal-dominant palette.
```

QA notes: Check white headline and a translucent glass card over the center and left thirds. Reject if gold is not visible or if teal becomes the dominant accent.

### next-step-bg

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/next-step-bg.png
- Dimensions: 1920x1080, 16:9
- Integration point: Closing next-step section backdrop
- Current status: pending
- Seed: pending

Prompt:

```text
Closing-section backdrop for a premium operations decision room, deep navy and ink-black field with subtle architectural depth, gold key light tracing a decision table edge, restrained reef teal schematic glow in the far background, calm and uncluttered, designed to sit behind white copy and a white decision card, cinematic stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces.
```

Negative prompt:

```text
alcohol, bottles, glasses, liquid, product packaging, readable text, logos, people facing camera, bright cyan scene, busy dashboard.
```

QA notes: Composite against white copy and a white card. Reject if the backdrop competes with text or lacks the gold premium accent.

### evidence-gates-texture-strip

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/evidence-gates-texture.png
- Dimensions: 1920x600, 16:5
- Integration point: Evidence-gates section headline texture strip
- Current status: pending
- Seed: pending

Prompt:

```text
Abstract material texture strip for evidence gates, dark navy lacquer, warm clay undertone, thin gold hairline highlights, subtle paper-fibre and metal-rule details, no objects, no screens, no readable text, no logos, no people, even dark center for overlaid headline, cinematic macro illustration.
```

Negative prompt:

```text
bottles, glasses, liquid, text, icons, logos, faces, busy scene, bright orange field, product photography.
```

QA notes: Center must stay dark and even. Reject if it introduces literal objects or looks like a product shot.

### og-social-card

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/og-card.png
- Dimensions: 1200x630 exact, 1.91:1
- Integration point: Open Graph and Twitter summary_large_image card
- Current status: pending
- Seed: pending

Prompt:

```text
Premium social-card background for an AngelServ Top Spirit command-center preview, deep navy editorial layout, abstract proof rail and approval envelope geometry, gold rim light as the main accent, restrained reef teal data signal, clean title-safe negative space, no baked-in text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces, stylized cinematic illustration.
```

Negative prompt:

```text
readable words, brand marks, product bottles, alcohol, people, charts with numbers, crowded dashboard, neon sci-fi.
```

QA notes: Must be exactly 1200x630 and contain no baked-in title text. Verify title-safe space survives social preview cropping.

## TASK-73

### capabilities-card-1-mapping

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-1-mapping.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: Process mapping
- Current status: pending
- Seed: pending

Prompt:

```text
Portrait 4:5 capability-card header for process mapping, faceless backs-only silhouette of an operator studying an abstract process map wall, dark navy room, gold pin lights marking verified steps, restrained reef teal connector lines, premium beverage-distribution operations mood, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no face.
```

Negative prompt:

```text
readable sticky notes, labels, charts with numbers, front-facing person, alcohol, bottles, logos, bright cyan dominance.
```

QA notes: Must match the other capability cards in light direction and style. Reject if map elements become readable.

### capabilities-card-2-optimisation

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-2-optimisation.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: Process optimisation
- Current status: pending
- Seed: pending

Prompt:

```text
Portrait 4:5 capability-card header for process optimisation, premium warehouse aisle abstracted into clean navy geometry, gold light tracing an improved route, restrained reef teal operational nodes, no people, editorial luxury distribution atmosphere, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
product packaging, alcohol, bottles, people, readable signs, bright supermarket, generic server room, teal-dominant lighting.
```

QA notes: Should echo hero-bg without duplicating it. Reject if it becomes retail product imagery.

### capabilities-card-3-literacy

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-3-literacy.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: AI literacy
- Current status: pending
- Seed: pending

Prompt:

```text
Portrait 4:5 capability-card header for AI literacy and team enablement, faceless backs-only silhouette at an abstract whiteboard in a dark navy training room, gold highlights on approved learning steps, restrained reef teal schematic accents, premium editorial illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no face.
```

Negative prompt:

```text
readable whiteboard text, classroom stock photo, front-facing people, logos, alcohol, product imagery, cartoon style.
```

QA notes: Keep it capability-led, not classroom-generic. Reject if the person is identifiable.

### capabilities-card-4-apis

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-4-apis.png
- Dimensions: 1024x1280 exact, 4:5
- Integration point: Capability card: APIs when justified
- Current status: pending
- Seed: pending

Prompt:

```text
Portrait 4:5 capability-card header for APIs when justified, dark governed integration cabinet with elegant cabling and abstract secure exchange nodes, navy base, gold verification line as the main accent, restrained reef teal signal lights, premium and practical, not sci-fi, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no people.
```

Negative prompt:

```text
neon cyberpunk, code text, product logos, server brand marks, alcohol, bottles, human faces, bright cyan scene.
```

QA notes: Should feel like governed infrastructure, not a generic sci-fi server render.

## TASK-74

### proof-spine-thumb-export-layer

- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/01-export-layer.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Export Layer
- Current status: pending
- Seed: pending

Prompt:

```text
Square proof-spine thumbnail for Export Layer, abstract file trays and controlled folder bands in a deep navy base darker than #07111F, gold gate marker and verified path, small restrained reef teal data points, cohesive icon-like cinematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
readable file names, spreadsheet text, logos, alcohol products, faces, bright teal dominance, flat clip art.
```

QA notes: Must read clearly at 360 to 480px on a #07111F card.

### proof-spine-thumb-approval-envelope

- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/02-approval-envelope.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Approval Envelope
- Current status: pending
- Seed: pending

Prompt:

```text
Square proof-spine thumbnail for Approval Envelope, abstract envelope plane and approval boundary in deep navy darker than #07111F, gold seal and thin approval rule, restrained reef teal approval node, premium schematic illustration, no readable text, no numbers, no logos, no faces, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
text labels, real envelopes with writing, signatures, logos, alcohol imagery, bright cyan glow, human face.
```

QA notes: Should make the human approval gate legible without words.

### proof-spine-thumb-audit-trail

- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/03-audit-trail.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Source-linked Audit Trail
- Current status: pending
- Seed: pending

Prompt:

```text
Square proof-spine thumbnail for Source-linked Audit Trail, vertical ledger-node chain on a deep navy base darker than #07111F, gold verified source nodes, restrained reef teal connectors, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
readable ledger entries, actual documents, signatures, charts with numbers, alcohol products, faces, teal-dominant palette.
```

QA notes: Gold should mark verified/source-linked points. Reject if it resembles fake data.

### proof-spine-thumb-glossary

- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/04-glossary.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Business Glossary
- Current status: pending
- Seed: pending

Prompt:

```text
Square proof-spine thumbnail for Business Glossary, abstract term-card grid with no words, deep navy base darker than #07111F, gold canonical term marker, restrained reef teal connectors between cards, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
readable words, dictionary pages, text labels, logos, alcohol products, faces, bright cyan dominance.
```

QA notes: Must communicate agreed definitions through structure and highlights, not text.

### proof-spine-thumb-opportunity-catalogue

- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/05-opportunity-catalogue.png
- Dimensions: 1024x1024 exact, 1:1
- Integration point: Proof spine step: Opportunity Catalogue
- Current status: pending
- Seed: pending

Prompt:

```text
Square proof-spine thumbnail for Opportunity Catalogue, abstract effort and value tile matrix with no labels, deep navy base darker than #07111F, one gold top-ranked tile, restrained reef teal ranking lines, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
```

Negative prompt:

```text
readable matrix labels, chart numbers, fake data, logos, alcohol products, faces, bright teal dominance.
```

QA notes: Should show prioritisation without any numeric or client-specific data.

## TASK-75

### walkthrough-mockup

- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/walkthrough-control-room.png
- Dimensions: 1200x1440 5:6 or 784x943 existing-card
- Integration point: Walkthrough section control-room image
- Current status: pending
- Seed: pending

Prompt:

```text
Premium walkthrough control-room scene for a process-review engagement, dark navy operations desk with abstract approval envelope, export layer and source-linked audit trail panels, gold desk trim and rim light, restrained reef teal schematic on screens, cream-page-compatible composition, one optional faceless backs-only silhouette, no readable screen content, no numbers, no logos, no bottles, no glasses, no liquid, no real face, stylized cinematic illustration.
```

Negative prompt:

```text
readable dashboards, fake customer names, people facing camera, alcohol, bottles, logos, neon sci-fi, bright cyan dominance, stock office photo.
```

QA notes: Place on a #F6F1E8 cream swatch. Record whether the final ratio is 1200x1440 or 784x943.
