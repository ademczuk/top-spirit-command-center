# Uploaded build-map coverage matrix

> **Backlog:** TASK-50
> **Status:** Repo-side coverage audit. Client evidence remains external and must not be fabricated.
> **Sources audited:** uploaded `topspirit-engagement-build-map-and-mockup-pack.md` (19 artifacts) and `topspirit-what-to-build-and-mockup-prompts.md` (12 artifact prompt pack).
> **Brand guardrail:** repo artifacts use **Angel Software Solutions** wording; legacy product names from the uploaded draft are intentionally not carried forward.

## Coverage result

The repo now covers the full 19-artifact build map at one of three levels:

- **Rendered / runnable** — committed diagram/script/output assets are available without asking another AI tool to regenerate them.
- **Prepared artifact** — client-ready documentation/template exists, but live completion depends on Top Spirit / Marussia inputs.
- **Client-blocked** — the repo can only provide the capture/checklist; evidence must come from BICC, SMEs, training attendees or steering committee decisions.

| # | Uploaded artifact | Repo coverage | Offline / executable asset | Honest blocker before client-complete |
|---|---|---|---|---|
| 1 | Solution architecture | `assets/mockups/01-solution-architecture.mmd`, `docs/03-mockup-pack.md` | `assets/mockups/rendered/01-solution-architecture.svg`, `assets/mockups/01-solution-architecture.png` | Confirm actual source systems and export folders in Phase 0. |
| 2 | Engagement roadmap | `docs/02-engagement-at-a-glance.md`, `assets/pitch/pitch-deck.md` slide 8 | `assets/mockups/html/02-engagement-roadmap.html` | Dates, owners and cadence need sponsor confirmation. |
| 3 | Cross-department process landscape | `assets/mockups/03-process-landscape.mmd`, `docs/06-wave-1/order-to-cash-process-map.md` | `assets/mockups/rendered/03-process-landscape.svg` | Department/process inventory must be validated in workshops. |
| 4 | Current-state as-is map | `assets/mockups/04-as-is-order-to-cash.mmd`, `docs/06-wave-1/order-to-cash-process-map.md` | `assets/mockups/rendered/04-as-is-order-to-cash.svg` | Time/error claims need SME samples and observation. |
| 5 | Target-state to-be map | `assets/mockups/05-to-be-order-to-cash.mmd`, `docs/06-wave-1/order-to-cash-process-map.md` | `assets/mockups/rendered/05-to-be-order-to-cash.svg` | Savings estimates stay illustrative until measured. |
| 6 | Effort/value/risk matrix | `docs/08-scale/opportunity-catalogue.md` prioritisation rubric | `assets/mockups/html/06-effort-value-risk-matrix.html` | Steering committee must score value/effort/risk/evidence. |
| 7 | Agent in approval envelope | `assets/mockups/07-agent-approval-envelope.mmd`, `docs/06-wave-1/governance-approval-envelopes.md` | `assets/mockups/rendered/07-agent-approval-envelope.svg` | Named approver roles and thresholds require steering approval. |
| 8 | Document order-intake pilot | `docs/07-wave-2/order-intake-automation-pilot.md`, `scripts/order_intake_extractor.py` | `assets/mockups/html/08-document-order-intake.html`, `outputs/wave2/order_intake_review_queue.csv` | Real order samples, volumes and approval owner required. |
| 9 | Reconciliation assistant | `docs/07-wave-2/financial-reconciliation-assistant-pilot.md`, `scripts/reconciliation_matcher.py` | `assets/mockups/html/09-financial-reconciliation-assistant.html`, `outputs/wave2/reconciliation_suggestions.csv` | Real bank/open-invoice exports and finance timings required. |
| 10 | Human-in-the-loop governance tiers | `assets/mockups/10-governance-tiers.mmd`, `docs/04-templates/governance-tiers-template.md` | `assets/mockups/rendered/10-governance-tiers.svg` | Steering committee must approve or amend tiers. |
| 11 | Source-linked audit trail | `assets/mockups/11-source-linked-audit-trail.mmd`, `docs/05-phase-0/source-linked-audit-trail-standard.md` | `assets/mockups/rendered/11-source-linked-audit-trail.svg` | Live lineage rows require real export IDs and approvals. |
| 12 | Data classification + export inventory | `docs/05-phase-0/data-classification-and-export-inventory.md` | `assets/mockups/html/12-data-classification-export-inventory.html` | BICC/data owners must fill owner, availability, classification, GDPR and retention fields. |
| 13 | Data dictionary / glossary | `docs/08-scale/living-business-glossary.md`, `docs/08-scale/business-glossary-seed.md` | `assets/mockups/html/13-business-glossary.html` | Definitions need business-owner review and conflicts resolved. |
| 14 | Business-case one-pager | `docs/04-templates/business-case-template.md`, `docs/08-scale/business-cases/` | `assets/mockups/html/14-business-case-one-pager.html`, nine proposed business-case stubs | Baseline effort, volume, loaded hourly rate and reviewer are client inputs. |
| 15 | Opportunity catalogue | `docs/08-scale/opportunity-catalogue.md` | `assets/mockups/html/15-opportunity-catalogue-board.html` | Steering committee must agree scores and sequencing. |
| 16 | Value & adoption dashboard | `assets/mockups/16-value-adoption-dashboard.mmd`, `docs/08-scale/value-adoption-dashboard-spec.md` | `assets/mockups/rendered/16-value-adoption-dashboard.svg`, `outputs/scale/*.csv` sample logs | Real adoption and savings metrics arrive only after live use. |
| 17 | AI-literacy programme + maturity | `docs/05-phase-0/ai-literacy-foundations-pilot.md`, `docs/08-scale/ai-literacy-programme-capability-maturity.md` | `assets/mockups/html/17-ai-literacy-maturity.html` | Requires 5+ attendees, feedback and maturity evidence. |
| 18 | Power BI Desktop dashboard | `docs/06-wave-1/power-bi-desktop-pilot-build-pack.md`, `outputs/wave1/power-bi-pilot-net-sales-report.md` | `assets/mockups/html/18-power-bi-dashboard.html`, `outputs/wave1/power-bi-pilot-lineage.csv` | BICC must open Power BI Desktop, refresh with representative exports and explain it independently. |
| 19 | ERP decision pack | `docs/08-scale/next-erp-recommendation-pack.md` | `assets/mockups/html/19-erp-decision-pack.html` | Recommendation needs client constraints, roadmap preference and steering decision. |

## Repo-side gaps closed by TASK-50

- Added deterministic prototype regression tests for the sample scripts and their committed outputs.
- Added portable path serialization so Windows and Linux runs emit POSIX lineage/source references in CSV artifacts.
- Added Mermaid rendering support (`scripts/render_storyboard_mermaid.py` + `.mermaid-puppeteer.json`) and committed offline SVGs for the storyboard visuals plus a deck-safe architecture PNG.
- Added the interactive walkthrough (`assets/mockups/walkthrough/index.html`) and HTML companion pack (`assets/mockups/html/`) for uploaded prompt artifacts that called for UI/HTML screens rather than Mermaid diagrams.
- Added CI verification for script compilation, pytest, output regeneration, HTML mockup generation, presentation links, whitespace and legacy-brand scanning.
- Added this coverage matrix so the 19-artifact upload can be checked without rereading the raw prompt pack line by line.

## Remaining external/client blockers

These are intentionally **not** marked complete by repository work:

| Task | External evidence needed |
|---|---|
| TASK-5 | BICC refreshes the Power BI Desktop pilot with representative exports and explains the report unaided. |
| TASK-39 | Signed export inventory with real owners, availability, classification, GDPR flags and retention decision. |
| TASK-40 | AI-literacy session attendance, feedback and refinements. |
| TASK-41 | O2C time samples and agreed hours-saved calculation. |
| TASK-42 | Business-user validation of the consolidated manual report against the trusted report. |
| TASK-43 | Steering decision on governance tiers and Approval Envelope thresholds. |
| TASK-44 | Steering prioritisation of opportunity catalogue scores and wave sequence. |
| TASK-45 | Evidence that BICC/tool owners can maintain and refresh artifacts after handover. |

## Verification hooks

Run from repo root:

```bash
python3 -m py_compile scripts/*.py
pytest -q
python3 scripts/build_manual_report.py
python3 scripts/order_intake_extractor.py
python3 scripts/reconciliation_matcher.py
python3 scripts/render_storyboard_mermaid.py
python3 scripts/generate_html_mockups.py
python3 scripts/verify_presentation_links.py
python3 scripts/check_brand_guardrails.py
git diff --check
backlog board export top-spirit-board.md --force
```
