# Cross-cutting — Privacy and GDPR operating model

> Applies to exports, reports, interview notes, prompts, AI agents, Power BI files and audit logs.

## Principles

1. **Need-to-know access**: users and agents only see data required for their role and task.
2. **Purpose limitation**: exports are used only for agreed process review, reporting, automation or glossary work.
3. **Minimisation**: redact, aggregate or sample before using AI where full detail is not needed.
4. **Human validation**: financial, pricing and customer-facing outputs remain human-approved.
5. **Traceability without oversharing**: audit logs reference source IDs, not unnecessary personal data.

## AI handling by classification tier

| Tier | Can be entered into AI workflow? | Conditions |
|---|---|---|
| T0 Public | Yes | No restrictions beyond quality review. |
| T1 Internal | Yes in approved workspace | No personal/customer/pricing detail; keep within project team. |
| T2 Confidential | Limited | Approved workspace only, authorised users only, source logged, output human-reviewed. |
| T3 Restricted/GDPR | Normally no | Use redacted/minimised extracts only after owner approval and documented purpose. Never paste credentials, bank details or unauthorised personal data. |

## Role/access rules

| Role | Default access |
|---|---|
| Executive sponsor | Summary artifacts, governance decisions, prioritisation, commercial pack. |
| BICC | Export inventory, Power BI pilot, data model, glossary, lineage records. |
| Finance SME | Finance exports, net sales/GP logic, reconciliation outputs. |
| Sales/Commercial SME | Pricing/customer segmentation logic relevant to approved scope. |
| Operations/Logistics SME | Stock, delivery, depletions and warehouse process data. |
| Agent/automation | Only approved input folders and only the minimum fields required for the workflow. |

## GDPR-sensitive scenarios

| Scenario | Handling | Retention/escalation |
|---|---|---|
| Export contains named contacts/emails | Minimise or pseudonymise unless needed for process control. | Record GDPR flag; delete working copy at project retention date. |
| Bank export contains payer details | Use controlled finance workspace only. | Finance approval required before processing; no public AI tools. |
| Customer complaint/free-text notes | Treat as T3 until reviewed. | Escalate to data owner; avoid LLM use unless redacted. |
| Accidental unauthorised data exposure | Stop processing and quarantine artifact. | Notify engagement lead/BICC; log incident and remediation. |
| Prompt/output includes pricing or customer-facing decision | AI may draft/recommend only. | Approval Envelope mandatory before use. |

## Operating checklist before any new workflow

- Export/source owner named.
- Classification tier assigned.
- GDPR flag assessed.
- Authorised users/agents listed.
- Input minimisation approach chosen.
- Approval Envelope tier assigned.
- Retention and deletion rule recorded.

## Client sign-off record (TASK-94)

| Item | Detail |
|---|---|
| Gate | Privacy and GDPR operating model |
| Required approver | Executive sponsor or named data owner |
| Decision | ☐ APPROVED ☐ APPROVED WITH CONDITIONS ☐ NOT APPROVED |
| Conditions / reservations | |
| Date | |
| Signed | |

This sign-off must be completed before any T2/T3 exports are used in demos, pilots or automation workflows.
