# Presentation runbook — agenda, talk track and rehearsal

> **Backlog:** TASK-47
> **Audience:** Andrew / Angel presenter, Top Spirit sponsor, BICC lead, AI Steering Committee.
> **Goal:** convert the repo into a confident client call, not a search through folders in front of the client.

## Meeting objectives

1. Confirm the problem frame: ERP and BI choices are open, but value can be delivered now.
2. Show the Angel approach: **Export Layer + Approval Envelopes + Source-linked Audit Trail**.
3. Demonstrate that the pack is practical: templates, sample data, storyboard, Power BI build pack and governance model.
4. Agree the immediate decision: proceed with a fixed-scope Phase 0 / Wave 1 pilot.
5. Identify the client-side dependencies: sponsor, BICC owner, exports, SMEs, workshop dates.

## Suggested agenda — 45 minutes

| Time | Segment | Lead | Artifact |
|---:|---|---|---|
| 0–5 | Context and objective | Angel | [`../../assets/pitch/pitch-deck.md`](../../assets/pitch/pitch-deck.md) slides 1–2 |
| 5–10 | Value-now promise and constraints | Angel | Slides 3–4; [`../../docs/02-engagement-at-a-glance.md`](../../docs/02-engagement-at-a-glance.md) |
| 10–20 | Process and automation storyboard | Angel + Sponsor | [`../../assets/mockups/storyboard-gallery.md`](../../assets/mockups/storyboard-gallery.md) visuals 1–6 |
| 20–27 | Governance, privacy and audit trail | Angel | [`../../docs/06-wave-1/governance-approval-envelopes.md`](../../docs/06-wave-1/governance-approval-envelopes.md), visual 7 |
| 27–34 | Power BI / reporting and value tracking | BICC + Angel | [`../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md`](../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md), [`../../docs/08-scale/value-adoption-dashboard-spec.md`](../../docs/08-scale/value-adoption-dashboard-spec.md) |
| 34–40 | ERP-neutral decision path | Angel + Steering | [`../../docs/08-scale/next-erp-recommendation-pack.md`](../../docs/08-scale/next-erp-recommendation-pack.md) |
| 40–45 | Decision ask and next steps | Angel | [`client-send-pack-and-follow-up.md`](client-send-pack-and-follow-up.md) |

## Compressed agenda — 30 minutes

| Time | Segment | What to cut / keep |
|---:|---|---|
| 0–4 | Context | Keep ERP/BI uncertainty and manual-work pain. |
| 4–9 | Promise | Keep file exports, M365 E3 and human approval. |
| 9–17 | Storyboard | Show visuals 1, 4, 5, 7 and 8 only. |
| 17–23 | First pilot | Show Power BI build pack + manual-report prototype output. |
| 23–27 | Governance + ERP neutrality | Use one slide for Approval Envelope and next-ERP staged decision. |
| 27–30 | Ask | Confirm sponsor, BICC owner, exports and Phase 0 start. |

## Slide-by-slide speaker notes

| Deck slide | What to say | Proof artifact |
|---|---|---|
| 1 — Title | "This is not an ERP replacement pitch. It is a way to create measurable value while ERP and BI decisions are still open." | [`../../README.md`](../../README.md) overview |
| 2 — Situation | "The cost is already visible: manual entry, fragmented reports, reconciliation by hand. Waiting for ERP means leaving savings on the table." | [`../../docs/01-project-expectations.md`](../../docs/01-project-expectations.md) |
| 3 — Promise | "We start from exports, stay within M365 E3, and avoid new licences until evidence justifies them." | [`../../docs/05-technical-setup/export-layer-setup-guide.md`](../../docs/05-technical-setup/export-layer-setup-guide.md) |
| 4 — Three pillars | "Every workflow has three safety rails: model the process, place AI inside Approval Envelopes, and keep a Source-linked Audit Trail." | [`../../docs/05-phase-0/source-linked-audit-trail-standard.md`](../../docs/05-phase-0/source-linked-audit-trail-standard.md) |
| 5 — Order-to-cash | "AI drafts. A person approves. The audit trail records the evidence." | [`../../docs/06-wave-1/order-to-cash-process-map.md`](../../docs/06-wave-1/order-to-cash-process-map.md) |
| 6 — Governance | "Tier 3 means financial, pricing and customer-facing outputs are always human decisions." | [`../../docs/06-wave-1/governance-approval-envelopes.md`](../../docs/06-wave-1/governance-approval-envelopes.md) |
| 7 — Audit trail | "If a number appears in a report, we can point back to the export, extraction date and reviewer." | [`../../docs/04-templates/source-linked-audit-trail-template.md`](../../docs/04-templates/source-linked-audit-trail-template.md) |
| 8 — Phasing | "Phase 0 builds the rules; Wave 1 proves value; Wave 2 scales only what survives evidence." | [`../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md`](../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md) |
| 9 — Success | "We track hours saved and adoption, not impressions. Adoption evidence is what makes the claim useful." | [`../../docs/08-scale/value-adoption-dashboard-spec.md`](../../docs/08-scale/value-adoption-dashboard-spec.md) |
| 10 — Next step | "We are asking for a sponsor, BICC counterpart, representative exports and a Phase 0 kickoff date." | [`client-send-pack-and-follow-up.md`](client-send-pack-and-follow-up.md#decision-options-for-the-call) |

## Objection handling

| Objection | Answer |
|---|---|
| "Shouldn't we wait for the ERP decision?" | No. The work is ERP-neutral: export inventory, process maps, glossary, audit trail and Power BI pilot all survive either brownfield or greenfield. Waiting only delays value and learning. |
| "Will this require new software licences?" | Not for the first phase. The operating constraint is Microsoft 365 E3 and file exports. Any new tool must earn its case through measured value. |
| "Is AI making financial or customer decisions?" | No. AI drafts and recommends. Financial, pricing and customer-facing outcomes sit inside Approval Envelopes with named human approval. |
| "What about GDPR?" | Phase 0 classifies data, flags personal/sensitive fields, defines permitted AI use and records evidence in the Source-linked Audit Trail. |
| "Will this become throwaway work if we change ERP?" | No. The Export Layer, business glossary, process maps, governance and adoption tracker are migration assets. They reduce ERP risk rather than compete with ERP. |
| "Can the team maintain this?" | That is explicit scope: AI literacy, BICC handover, refresh checklists and capability maturity evidence. The solution is not accepted until the team can explain and operate it. |

## Rehearsal checklist

- [ ] Presenter has the deck, one-pager, storyboard gallery and this runbook open.
- [ ] Mermaid diagrams render in the chosen viewer; if not, use the inline code blocks in the gallery.
- [ ] Offline fallback folder is known: repo clone with `assets/`, `docs/`, `outputs/` available locally.
- [ ] Presenter can explain the difference between **sample output** and **client evidence**.
- [ ] Presenter can state the next-step ask in one sentence.
- [ ] Internal-only material is not sent to the client by accident.
- [ ] No raw secrets, tokens, unrelated client names, or live data appear in screenshots.

## Explicit next-step ask

> "If this approach fits, the decision today is to start a fixed-scope Phase 0 / Wave 1 pilot: name the sponsor and BICC counterpart, confirm representative exports, book the process/glossary workshops, and agree the first Power BI/reporting use case. We will keep the ERP decision staged and evidence-gated."

## What not to say

- Do not promise a real PBIX has been built from client data until it has.
- Do not quote savings as facts before time samples exist.
- Do not claim the steering committee approved governance before the meeting.
- Do not call this an ERP implementation.
- Do not let the word "agent" sound like uncontrolled automation; always pair it with **Approval Envelope**.
