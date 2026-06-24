# Starter export data pack

> **Demo data only.** Fully synthetic and anonymised. No real customer names, brands, prices or live values.
>
> Purpose: support the pre-call demo, BICC Power BI pilot, and Wave 2 agent prompts without waiting for client exports.

---

## Files

| File | Format | Represents | Supports |
|---|---|---|---|
| `customer_master.csv` | CSV | B2B customer list with channel, region, credit limit | Order validation, credit control, Power BI region analysis |
| `price_list.csv` | CSV | Active product catalogue and unit prices | Order validation, price-list update pilot |
| `stock_availability.csv` | CSV | Warehouse stock levels | Order validation, stock allocation |
| `bank_payments.csv` | CSV | Incoming bank payments with invoice references | Reconciliation assistant pilot |
| `sales_invoices.csv` | CSV | Issued invoices and payment status | Reconciliation, net sales / GP reporting |
| `orders_in_sample/order_001.txt` | Text | Example PDF/email order | PDF order-intake agent demo |

---

## Data classification

All files are synthetic and contain no personal data. In a live engagement they would be classified as follows:

| File | Suggested classification | Reason |
|---|---|---|
| customer_master.csv | Confidential | Customer names, credit limits, payment terms |
| price_list.csv | Internal | Commercial pricing, not public |
| stock_availability.csv | Internal | Operational data |
| bank_payments.csv | Restricted | Financial transactions |
| sales_invoices.csv | Restricted | Financial transactions |
| orders_in_sample/order_001.txt | Internal | Operational order data |

---

## How to use

1. Load the CSVs directly into Power BI Desktop or Excel for the BICC pilot.
2. Use `order_001.txt` as input for the PDF/email order-intake agent prompt demo.
3. Use `bank_payments.csv` + `sales_invoices.csv` for the reconciliation matching demo.
4. Map every value back to a source file in the Source-linked Audit Trail template.

---

*Generated for the Top Spirit (Marussia) / Angel Software Solutions engagement pack. Not for commercial use outside the authorised project team.*
