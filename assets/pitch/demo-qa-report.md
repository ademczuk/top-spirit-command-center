# Demo QA report and offline fallback

> **Backlog:** TASK-48
> **Status:** Presentation/demo pack reviewed for repository-local use. Link checker script records current file references.

## Demo path

Use this sequence in the call:

1. Start with the premium Pages command center: [`../../docs/index.html`](../../docs/index.html).
2. Open [`../../assets/pitch/pitch-deck.md`](../../assets/pitch/pitch-deck.md) if the call needs a deck view.
3. Open the interactive walkthrough: [`../../assets/mockups/walkthrough/index.html`](../../assets/mockups/walkthrough/index.html).
4. Keep the storyboard gallery ready as an offline/diagram backup: [`../../assets/mockups/storyboard-gallery.md`](../../assets/mockups/storyboard-gallery.md).
5. Show the Export Layer setup: [`../../docs/05-technical-setup/export-layer-setup-guide.md`](../../docs/05-technical-setup/export-layer-setup-guide.md).
6. Show the Power BI build pack and sample report:
   - [`../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md`](../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md)
   - [`../../outputs/wave1/power-bi-pilot-net-sales-report.md`](../../outputs/wave1/power-bi-pilot-net-sales-report.md)
7. Show source-linked evidence:
   - [`../../outputs/wave1/power-bi-pilot-lineage.csv`](../../outputs/wave1/power-bi-pilot-lineage.csv)
   - [`../../docs/05-phase-0/source-linked-audit-trail-standard.md`](../../docs/05-phase-0/source-linked-audit-trail-standard.md)
8. Close with value tracking:
   - [`../../docs/08-scale/value-adoption-dashboard-spec.md`](../../docs/08-scale/value-adoption-dashboard-spec.md)
   - [`../../docs/08-scale/value-adoption-dashboard-sample.md`](../../docs/08-scale/value-adoption-dashboard-sample.md)

## Asset inventory checked

| Area | Required assets | Status |
|---|---|---|
| Premium Pages command center | `docs/index.html`, `docs/DESIGN.md`, `.github/workflows/pages.yml`, `scripts/verify_pages_site.py` | Present |
| Pitch | `assets/pitch/pitch-deck.md`, `assets/pitch/executive-one-pager.md` | Present |
| Interactive walkthrough | `assets/mockups/walkthrough/index.html` with eight demo beats, Previous/Next controls, progress dots and keyboard navigation | Present |
| Storyboard | `assets/mockups/storyboard-gallery.md`, eight `.mmd` files used in pitch order, `assets/mockups/01-solution-architecture.png` and `assets/mockups/rendered/*.svg` offline renders | Present |
| HTML companion mockups | `assets/mockups/html/*.html` for app-like visuals #2, #6, #8, #9, #12, #13, #14, #15, #17, #18 and #19 | Present |
| Starter data | `assets/starter-data/*.csv`, sample order text, README | Present |
| Power BI | `assets/powerbi/README.md`, Wave 1 build pack, sample report and lineage | Present |
| Prototype outputs | `outputs/wave1/*.csv`, `outputs/wave2/*.csv`, `outputs/scale/*.csv` | Present |
| Templates | `docs/04-templates/` | Present |
| Presentation kit | `docs/11-presentation/` | Present |

## Offline fallback plan

If internet, Mermaid preview or Power BI Desktop fails during the meeting:

1. Use the repo-local Markdown files as the canonical demo.
2. Open `docs/index.html` for the premium command-center entry point or `assets/mockups/walkthrough/index.html` directly if the live demo needs a single local click-through.
3. Open the committed SVGs in `assets/mockups/rendered/` or `assets/mockups/01-solution-architecture.png` if Mermaid preview fails.
4. Open the standalone HTML companion screens in `assets/mockups/html/` if an app-like UI mockup is easier than a Mermaid/source doc.
5. Use the sample Markdown report [`../../outputs/wave1/power-bi-pilot-net-sales-report.md`](../../outputs/wave1/power-bi-pilot-net-sales-report.md) instead of Power BI Desktop.
6. Use CSV lineage/output files as evidence of the export-only approach.
7. Say plainly: "The PBIX is a Wave 1 build step using your representative exports; this call shows the build pack and sample output."

## Known limitations / do not overclaim

| Item | Limitation | Presenter line |
|---|---|---|
| PBIX file | No real client PBIX exists in this repo. | "The build pack is ready; PBIX build follows once representative exports are supplied." |
| Savings figures | Sample/illustrative until time samples are captured. | "The mechanism is ready; the numbers are populated from your Wave 1 measurements." |
| Adoption metrics | Sample logs exist; real adoption needs users. | "Monthly adoption tracking starts after pilot launch." |
| Governance approval | Draft model exists; steering must approve. | "This is the model for approval today, not a claim of prior approval." |

## Fixes made for presentation readiness

- Ported the Joey/Marlin storyboard gallery and `.mmd` files onto the current presentation branch.
- Added Power BI sample report, lineage and build pack to avoid a dead-end demo if Power BI Desktop is unavailable.
- Added presentation runbook, send-pack and client action pack under `docs/11-presentation/`.
- Added `scripts/verify_presentation_links.py` to check repository-local Markdown links before the call.
- Added the premium AgentReef-style Pages command center under `docs/index.html` plus `scripts/verify_pages_site.py` and `.github/workflows/pages.yml`.

## Premium Pages visual QA — 2026-06-23

Local `_site` artifact was built with the same copy steps as `.github/workflows/pages.yml`, served with `python3 -m http.server 8765 --directory _site`, and checked using Playwright Chromium.

| Viewport | Result | Notes |
|---|---|---|
| 375 × 812 | Pass | No horizontal overflow; H1 present; 10 artifact links; 5 lineage buttons; first Tab lands on a visible link. |
| 768 × 1024 | Pass | No horizontal overflow; layout collapses to one column; lineage interaction remains keyboard reachable. |
| 1440 × 1000 | Pass | No horizontal overflow; desktop two-column hero and evidence rail render as intended. |
| Reduced motion | Pass | No active CSS animations run under `prefers-reduced-motion: reduce`; the page is reduced-motion safe by omission rather than animation override. |

The QA run does not claim final client approval or real data validation; TASK-39–TASK-45 remain client evidence blockers.

## Pre-call QA commands

```bash
python3 scripts/verify_presentation_links.py
python3 scripts/verify_pages_site.py
python3 scripts/render_storyboard_mermaid.py
python3 scripts/generate_html_mockups.py
pytest -q
python3 scripts/check_brand_guardrails.py
git diff --check
backlog task list --plain --limit 240
```

## Presenter final check

- [ ] Can open deck, gallery and runbook locally.
- [ ] Can show sample Power BI report without Power BI Desktop.
- [ ] Can explain every sample as sample.
- [ ] Can point to the exact client dependencies in [`client-action-pack.md`](client-action-pack.md).
- [ ] Can state the decision ask without reading the entire repo like a cursed bedtime story.
