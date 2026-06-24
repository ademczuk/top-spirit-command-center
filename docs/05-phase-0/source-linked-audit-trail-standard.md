# Cross-cutting — Source-linked audit trail standard

> Rule: every figure, recommendation and AI/automation output must be traceable back to authorised sources.

## 1. Lineage ID scheme

| Prefix | Source type | Example |
|---|---|---|
| `EXP` | File export | `EXP-ERP-SALES-001` |
| `RPT` | Existing report/workbook | `RPT-BICC-SALES-001` |
| `INT` | Interview/workshop notes | `INT-OTC-001` |
| `CALC` | Transformation/formula | `CALC-NETSALES-001` |
| `DEC` | Human decision/sign-off | `DEC-GOV-TIER-001` |
| `OUT` | Produced output/report/automation result | `OUT-PBI-W1-001` |

ID format: `<PREFIX>-<DOMAIN>-<NAME>-<NNN>`, stable once assigned.

## 2. Audit-trail record template

| Field | Meaning |
|---|---|
| Lineage ID | Stable ID for this source or transformation. |
| Artifact name | File/report/process/business case/output. |
| Source owner | Business owner accountable for it. |
| Extraction date | When source was exported or captured. |
| Classification | T0/T1/T2/T3. |
| GDPR flag | None / personal / financial personal / unknown. |
| Transformation logic | Formula, filter, join, mapping, prompt or model action. |
| Reviewer | Human who validated the output. |
| Review outcome | Approved / rejected / revised / pending. |
| Downstream artifacts | Where this record is used. |

## 3. Required lineage in each artifact

| Artifact | Minimum lineage required |
|---|---|
| Process map | Interview IDs, export/report IDs used as evidence, SME reviewer. |
| Target-state redesign | As-is map ID, savings assumptions, approval decisions. |
| Manual report rebuild | Source export IDs, transformation formulas, reconciled output ID. |
| Power BI pilot | Export IDs, data model notes, measure definitions, refresh owner. |
| Business glossary term | Source exports/reports, owner, formula, review date. |
| Opportunity business case | Effort/value assumptions, source evidence, reviewer. |
| AI/agent output | Input source IDs, model/prompt version, confidence, human approval. |

## 4. Example end-to-end trace

**Headline figure:** `OUT-PBI-W1-001 Net Sales May 2026`

1. Source file: `EXP-ERP-SALES-001 sales_invoice_lines_20260601.csv`.
2. Transformation: `CALC-NETSALES-001 = gross sales - discounts - credit notes, excluding VAT`.
3. Glossary definition: `TERM-NETSALES-001`, owned by Finance SME.
4. Report output: `OUT-PBI-W1-001`, Power BI Desktop pilot page 1.
5. Review: `DEC-BICC-001`, BICC confirms measure reconciles to legacy report within agreed tolerance.

## 5. Reviewer sign-off checklist

- Source file or interview note is listed in the export/input inventory.
- Classification and GDPR flag are present.
- Formula/transformation/prompt is recorded in plain language.
- Output reconciles to current known report or SME explanation.
- Human reviewer and date are recorded.
