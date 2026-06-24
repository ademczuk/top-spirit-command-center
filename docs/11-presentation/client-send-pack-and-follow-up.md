# Client send-pack and post-call follow-up kit

> **Backlog:** TASK-49
> **Purpose:** prevent accidental oversharing, give the client a clean pack, and make the next decision easy.

## Send-pack rule

Only send client-facing artifacts that are polished, neutral, and safe. Keep operational coordination, internal swarm notes, raw backlog chatter and agent dispatch evidence out of the client pack unless explicitly requested internally.

## Pre-call pack

Send **before** the call if the goal is to give the sponsor context without overwhelming them:

| Artifact | Send? | Why |
|---|---:|---|
| [`../../assets/pitch/executive-one-pager.md`](../../assets/pitch/executive-one-pager.md) | Yes | Executive framing and next-step context. |
| [`../../assets/pitch/pitch-deck.md`](../../assets/pitch/pitch-deck.md) | Optional | Send if the sponsor wants pre-read slides; otherwise use live. |
| [`../../docs/02-engagement-at-a-glance.md`](../../docs/02-engagement-at-a-glance.md) | Optional | Good for BICC / delivery lead pre-read. |
| [`../../docs/05-technical-setup/export-layer-setup-guide.md`](../../docs/05-technical-setup/export-layer-setup-guide.md) | Optional / BICC only | Useful if technical readiness is already being discussed. |

## In-call pack

Use live, but do not necessarily send yet:

| Artifact | Use in call | Notes |
|---|---|---|
| [`../../assets/mockups/walkthrough/index.html`](../../assets/mockups/walkthrough/index.html) | Yes | Interactive eight-screen guided demo; single local HTML file, no live data. |
| [`../../assets/mockups/storyboard-gallery.md`](../../assets/mockups/storyboard-gallery.md) | Yes | Offline storyboard gallery; no live data. |
| [`../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md`](../../docs/06-wave-1/power-bi-desktop-pilot-build-pack.md) | Yes | Show export-only report build approach. |
| [`../../outputs/wave1/power-bi-pilot-net-sales-report.md`](../../outputs/wave1/power-bi-pilot-net-sales-report.md) | Yes | Label as sample output. |
| [`../../docs/08-scale/next-erp-recommendation-pack.md`](../../docs/08-scale/next-erp-recommendation-pack.md) | Yes, if ERP question arises | Vendor-neutral; decision framework, not vendor recommendation. |

## Post-call pack

Send after the call with a short note and agreed next steps:

| Artifact | Send? | Why |
|---|---:|---|
| Pitch deck / one-pager | Yes | Meeting record. |
| Presentation runbook excerpts | No | Internal speaker notes; summarize instead. |
| [`../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md`](../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md) | Yes, once commercial discussion starts | Shows fixed-scope pilot shape. |
| [`client-action-pack.md`](client-action-pack.md) | Yes, edited to client-friendly owner names | Clarifies what Top Spirit needs to provide. |
| Source templates | Yes, selectively | Send templates relevant to agreed next step only. |

## Internal-only / hold back

Do **not** send these externally by default:

- `backlog/` task files and AgentReef dispatch rows.
- `docs/10-agentreef-dispatch-log.md` unless explicitly requested internally.
- Raw internal notes, tool outputs, mesh-chat evidence, or automation logs.
- Any file containing credentials, tokens, secret state, private keys, or unrelated client material.

## Decision options for the call

| Option | Decision | When to choose |
|---|---|---|
| **A — Start Phase 0 / Wave 1 pilot** | Name sponsor/BICC lead, confirm exports, schedule workshops and agree pilot use case. | Recommended if the approach fits and there is appetite to move. |
| **B — Run a short scoping workshop first** | Book a 60–90 minute process/export validation workshop before committing to Phase 0. | Choose if stakeholders need more confidence or export availability is unclear. |
| **C — Defer** | No pilot until ERP/BI decision is clearer. | Choose only if leadership refuses interim value delivery. Flag opportunity cost. |

## Post-call follow-up email

Subject: `Top Spirit × Angel Software Solutions — next steps from AI/process automation call`

```text
Hi [Name],

Thank you for the discussion today. My read is that the useful next step is to keep the ERP/BI decision evidence-gated while starting a fixed-scope Phase 0 / Wave 1 pilot that creates value now from file exports inside Microsoft 365 E3.

Suggested next steps:
1. Confirm the steering sponsor and BICC counterpart.
2. Confirm the first representative exports we can use for the export inventory and Power BI/reporting pilot.
3. Book the Phase 0 workshops: export inventory, order-to-cash process map, glossary/definition alignment and governance/Approval Envelope review.
4. Agree whether the first Wave 1 value case is the consolidated manual report, Power BI pilot, or order-to-cash intake flow.

Attached / linked:
- Executive one-pager and pitch deck
- Engagement-at-a-glance summary
- Export Layer setup guide
- Fixed-scope pilot plan
- Client action checklist

Best,
[Name]
```

## Commercial / pilot alignment

The send-pack aligns to [`../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md`](../../docs/09-commercial/fixed-scope-pilot-commercial-plan.md): a bounded Phase 0 / Wave 1 pilot with clear dependencies, no uncontrolled ERP commitment, no live connector promise, and measurable value criteria.
