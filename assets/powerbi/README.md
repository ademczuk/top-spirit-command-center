# Power BI Desktop starter — specification

> Specification and starter data-model guidance for the BICC pilot. No `.pbix` file is stored in Git; build it locally from the starter exports.
>
> **Confidential — project team only.** Stays inside Microsoft 365 E3; no live connectors required.

---

## 1. Purpose

Prove that the Export Layer can feed useful, self-service reporting without waiting for the ERP or BI-platform decision.

---

## 2. Data sources

Connect Power BI Desktop to the CSV files in `assets/starter-data/`:

- `customer_master.csv`
- `price_list.csv`
- `stock_availability.csv`
- `sales_invoices.csv`

Use the **SharePoint Folder** or **Folder** connector if running against the live Export Layer.

---

## 3. Recommended data model

```text
sales_invoices  ----<  customer_master  (customer_id)
       |
       |---<  price_list  (product_code)
```

- `sales_invoices` is the fact table.
- `customer_master` and `price_list` are dimensions.
- `stock_availability` can be a standalone table or related to `price_list` by `product_code`.

---

## 4. Core measures

| Measure | DAX pattern | Business Glossary link |
|---|---|---|
| Net Sales | `SUM(sales_invoices[net_amount_eur])` | *Net Sales* |
| Gross Profit | `SUMX(sales_invoices, sales_invoices[quantity] * (RELATED(price_list[unit_price_eur]) - <cost>))` | *Gross Profit* |
| GP % | `DIVIDE([Gross Profit], [Net Sales], 0)` | *Gross Profit %* |
| Depletions (bottles) | `SUM(sales_invoices[quantity])` | *Depletions* |

> Note: cost data is not in the starter pack; use a placeholder cost column or add a `cost_price_eur` column to `price_list.csv`.

---

## 5. Report pages

1. **Executive summary** — KPI cards for net sales, GP, GP %, depletions.
2. **Sales trend** — line chart of net sales by week/month.
3. **By channel / region** — bar chart using `customer_master[channel]` and `[region]`.
4. **By product** — bar chart using `price_list[category]` and `product_name`.
5. **Source lineage** — table showing source file names and last refresh date.

---

## 6. Build steps

1. Open Power BI Desktop.
2. Get Data → Folder → point to `assets/starter-data/`.
3. Filter CSV files and combine.
4. Add calculated columns and measures from the Business Glossary.
5. Build the five report pages.
6. Save as `TopSpirit_Pilot_Starter.pbix` locally.
7. Share via the project SharePoint/Teams (do not publish to Power BI Service without Pro licences).

---

## 7. No-new-licences check

| Capability | E3 coverage |
|---|---|
| Power BI Desktop | Yes — free download |
| SharePoint Folder connector | Yes — standard connector |
| Local `.pbix` sharing via SharePoint | Yes |
| Power BI Service publishing | No — requires Pro/PPU |

---

*Version 1.0 — Angel Software Solutions engagement pack.*
