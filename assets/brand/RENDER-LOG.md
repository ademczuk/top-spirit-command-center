# Top Spirit Generated Image Render Log

Status: pending generation

This log is the source-linked handoff for TASK-72 to TASK-75. It lists every planned PNG asset in the `assets` list of `assets/brand/manifest.json`, with starter prompts, model lanes, output paths and post-generation QA notes.

Tide can use `assets/brand/TIDE-PROMPT-PACKET.md` as the copy-ready prompt packet. Regenerate it from this log and the manifest with `python scripts/generate_brand_prompt_packet.py --write`; verify freshness with `python scripts/generate_brand_prompt_packet.py --check`.

Tide's already shipped motion hero is tracked separately in the manifest `motionAssets` list: `assets/hero-bg.mp4` and `assets/hero-poster.jpg`. Verify that live media with `python scripts/verify_motion_assets.py`.

After each final render, Tide should update that asset block:

- Set `Status` to `generated`, `accepted` or `rejected`.
- Replace `Seed: pending` with the actual seed or deterministic generation id. If the provider does not expose a seed, use `not-exposed` rather than `pending`.
- Replace `Final prompt: pending` with the submitted prompt, or with `same as starter prompt` when unchanged.
- Replace `Post-generation QA notes: pending` with `Result: <pass/review-needed/rejected> - <final review details and any follow-up needed>`.
- Add `Generated at` and `Reviewer` to every accepted/generated asset block. Add crop/upscale notes when available.
- Keep all constraints demo-safe: no alcohol, bottles, glasses, liquid, logos, readable text, real faces or fabricated customer evidence.

Global visual direction: premium beverage-distribution control room, deep navy ground, gold as the primary premium accent, reef teal as a restrained platform/data signal, clay only for evidence-gate warmth, cream only for page-context compatibility.

Status values: `pending`, `generated`, `accepted`, `rejected`.

## hero-bg

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/hero-bg.png
- Dimensions: 1920x1080 preferred, minimum 1376x768, 16:9
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Cinematic premium distribution operations control room at night, deep navy editorial-luxury environment, abstract export files and approval gates on dark glass panels, one clear gold rim light along desks and rails, very restrained reef teal data glow below 15 percent of accent area, low contrast center with generous empty space for white headline and glass card overlay, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces.
- Negative prompt: alcohol, bottles, glasses, liquid, brand logos, readable words, numbers, faces, portraits, fake client dashboards, stock photo look, teal-dominant palette.
- Post-generation QA notes: Check white headline and a translucent glass card over the center and left thirds. Reject if gold is not visible or if teal becomes the dominant accent.

## next-step-bg

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/next-step-bg.png
- Dimensions: 1920x1080, 16:9
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Closing-section backdrop for a premium operations decision room, deep navy and ink-black field with subtle architectural depth, gold key light tracing a decision table edge, restrained reef teal schematic glow in the far background, calm and uncluttered, designed to sit behind white copy and a white decision card, cinematic stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces.
- Negative prompt: alcohol, bottles, glasses, liquid, product packaging, readable text, logos, people facing camera, bright cyan scene, busy dashboard.
- Post-generation QA notes: Composite against white copy and a white card. Reject if the backdrop competes with text or lacks the gold premium accent.

## evidence-gates-texture-strip

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/evidence-gates-texture.png
- Dimensions: 1920x600, 16:5
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Abstract material texture strip for evidence gates, dark navy lacquer, warm clay undertone, thin gold hairline highlights, subtle paper-fibre and metal-rule details, no objects, no screens, no readable text, no logos, no people, even dark center for overlaid headline, cinematic macro illustration.
- Negative prompt: bottles, glasses, liquid, text, icons, logos, faces, busy scene, bright orange field, product photography.
- Post-generation QA notes: Center must stay dark and even. Reject if it introduces literal objects or looks like a product shot.

## og-social-card

- Task: TASK-72
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/og-card.png
- Dimensions: 1200x630 exact, 1.91:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Premium social-card background for an AngelServ Top Spirit command-center preview, deep navy editorial layout, abstract proof rail and approval envelope geometry, gold rim light as the main accent, restrained reef teal data signal, clean title-safe negative space, no baked-in text, no numbers, no logos, no bottles, no glasses, no liquid, no real faces, stylized cinematic illustration.
- Negative prompt: readable words, brand marks, product bottles, alcohol, people, charts with numbers, crowded dashboard, neon sci-fi.
- Post-generation QA notes: Must be exactly 1200x630 and contain no baked-in title text. Verify title-safe space survives social preview cropping.

## capabilities-card-1-mapping

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-1-mapping.png
- Dimensions: 1024x1280 exact, 4:5
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Portrait 4:5 capability-card header for process mapping, faceless backs-only silhouette of an operator studying an abstract process map wall, dark navy room, gold pin lights marking verified steps, restrained reef teal connector lines, premium beverage-distribution operations mood, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no face.
- Negative prompt: readable sticky notes, labels, charts with numbers, front-facing person, alcohol, bottles, logos, bright cyan dominance.
- Post-generation QA notes: Must match the other capability cards in light direction and style. Reject if map elements become readable.

## capabilities-card-2-optimisation

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-2-optimisation.png
- Dimensions: 1024x1280 exact, 4:5
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Portrait 4:5 capability-card header for process optimisation, premium warehouse aisle abstracted into clean navy geometry, gold light tracing an improved route, restrained reef teal operational nodes, no people, editorial luxury distribution atmosphere, stylized illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid.
- Negative prompt: product packaging, alcohol, bottles, people, readable signs, bright supermarket, generic server room, teal-dominant lighting.
- Post-generation QA notes: Should echo hero-bg without duplicating it. Reject if it becomes retail product imagery.

## capabilities-card-3-literacy

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-3-literacy.png
- Dimensions: 1024x1280 exact, 4:5
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Portrait 4:5 capability-card header for AI literacy and team enablement, faceless backs-only silhouette at an abstract whiteboard in a dark navy training room, gold highlights on approved learning steps, restrained reef teal schematic accents, premium editorial illustration, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no face.
- Negative prompt: readable whiteboard text, classroom stock photo, front-facing people, logos, alcohol, product imagery, cartoon style.
- Post-generation QA notes: Keep it capability-led, not classroom-generic. Reject if the person is identifiable.

## capabilities-card-4-apis

- Task: TASK-73
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/capabilities/cap-4-apis.png
- Dimensions: 1024x1280 exact, 4:5
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Portrait 4:5 capability-card header for APIs when justified, dark governed integration cabinet with elegant cabling and abstract secure exchange nodes, navy base, gold verification line as the main accent, restrained reef teal signal lights, premium and practical, not sci-fi, no readable text, no numbers, no logos, no bottles, no glasses, no liquid, no people.
- Negative prompt: neon cyberpunk, code text, product logos, server brand marks, alcohol, bottles, human faces, bright cyan scene.
- Post-generation QA notes: Should feel like governed infrastructure, not a generic sci-fi server render.

## proof-spine-thumb-export-layer

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/01-export-layer.png
- Dimensions: 1024x1024 exact, 1:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Square proof-spine thumbnail for Export Layer, abstract file trays and controlled folder bands in a deep navy base darker than #07111F, gold gate marker and verified path, small restrained reef teal data points, cohesive icon-like cinematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
- Negative prompt: readable file names, spreadsheet text, logos, alcohol products, faces, bright teal dominance, flat clip art.
- Post-generation QA notes: Must read clearly at 360 to 480px on a #07111F card.

## proof-spine-thumb-approval-envelope

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/02-approval-envelope.png
- Dimensions: 1024x1024 exact, 1:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Square proof-spine thumbnail for Approval Envelope, abstract envelope plane and approval boundary in deep navy darker than #07111F, gold seal and thin approval rule, restrained reef teal approval node, premium schematic illustration, no readable text, no numbers, no logos, no faces, no bottles, no glasses, no liquid.
- Negative prompt: text labels, real envelopes with writing, signatures, logos, alcohol imagery, bright cyan glow, human face.
- Post-generation QA notes: Should make the human approval gate legible without words.

## proof-spine-thumb-audit-trail

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/03-audit-trail.png
- Dimensions: 1024x1024 exact, 1:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Square proof-spine thumbnail for Source-linked Audit Trail, vertical ledger-node chain on a deep navy base darker than #07111F, gold verified source nodes, restrained reef teal connectors, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
- Negative prompt: readable ledger entries, actual documents, signatures, charts with numbers, alcohol products, faces, teal-dominant palette.
- Post-generation QA notes: Gold should mark verified/source-linked points. Reject if it resembles fake data.

## proof-spine-thumb-glossary

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/04-glossary.png
- Dimensions: 1024x1024 exact, 1:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Square proof-spine thumbnail for Business Glossary, abstract term-card grid with no words, deep navy base darker than #07111F, gold canonical term marker, restrained reef teal connectors between cards, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
- Negative prompt: readable words, dictionary pages, text labels, logos, alcohol products, faces, bright cyan dominance.
- Post-generation QA notes: Must communicate agreed definitions through structure and highlights, not text.

## proof-spine-thumb-opportunity-catalogue

- Task: TASK-74
- Owner: tide
- Model lane: Gemini nanoBanana
- Output path: assets/brand/proof-spine/05-opportunity-catalogue.png
- Dimensions: 1024x1024 exact, 1:1
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Square proof-spine thumbnail for Opportunity Catalogue, abstract effort and value tile matrix with no labels, deep navy base darker than #07111F, one gold top-ranked tile, restrained reef teal ranking lines, premium schematic illustration, no readable text, no numbers, no logos, no people, no bottles, no glasses, no liquid.
- Negative prompt: readable matrix labels, chart numbers, fake data, logos, alcohol products, faces, bright teal dominance.
- Post-generation QA notes: Should show prioritisation without any numeric or client-specific data.

## walkthrough-mockup

- Task: TASK-75
- Owner: tide
- Model lane: Grok Imagine
- Output path: assets/brand/walkthrough-control-room.png
- Dimensions: 1200x1440 or 784x943, ratio must be recorded after generation
- Status: pending
- Seed: pending
- Final prompt: pending
- Starter prompt: Premium walkthrough control-room scene for a process-review engagement, dark navy operations desk with abstract approval envelope, export layer and source-linked audit trail panels, gold desk trim and rim light, restrained reef teal schematic on screens, cream-page-compatible composition, one optional faceless backs-only silhouette, no readable screen content, no numbers, no logos, no bottles, no glasses, no liquid, no real face, stylized cinematic illustration.
- Negative prompt: readable dashboards, fake customer names, people facing camera, alcohol, bottles, logos, neon sci-fi, bright cyan dominance, stock office photo.
- Post-generation QA notes: Place on a #F6F1E8 cream swatch. Record whether the final ratio is 1200x1440 or 784x943.
