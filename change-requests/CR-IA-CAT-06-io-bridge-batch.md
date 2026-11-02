# CR-IA-CAT-06: Process-IO Bridge Batch — Domain-Level Deliverable Assets

| Field | Value |
|---|---|
| **CR** | CR-IA-CAT-06 |
| **Title** | Process-IO bridge batch: 14 domain-level deliverable assets from the complete L2 backfill |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Process-definition completeness + information-asset advancement |
| **Repository** | `technehub-labs/dea-catalog-information-assets` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-02 |
| **Depends on** | CR-IA-CAT-05 (bridge method); dea-catalog-business-processes CR-BP-220 (the complete L2 IO backfill these assets derive from) |
| **Trigger** | Owner directive: perform the backfill to complete it. CR-BP-220 declares IO on all 146 L2 records; this CR mints the information-typed outputs as assets under the CR-IA-CAT-05 bridge method. |

## 1. Executive summary

**14 domain-level deliverable assets** admitted, derived from the complete L2 IO backfill: each ECF domain's `document`-typed and `information`-typed output classes become one aggregate asset carrying `produces` edges from every producing process record (60 information-typed outputs across 7 domains → 14 deduplicated domain/type classes → 60 produces assertions). The IA catalog goes **11 → 25 canonical**.

## 2. The batch

| Asset | Producers | Form |
|---|---|---|
| ao-document / ao-information | 5 / 5 | document / report |
| eo-document / eo-information | 5 / 1 | document / report |
| fa-document / fa-information | 4 / 8 | document / report |
| ge-document / ge-information | 4 / 7 | document / report |
| pr-document / pr-information | 6 / 2 | document / report |
| pv-document / pv-information | 3 / 1 | document / report |
| sd-document / sd-information | 4 / 4 | document / report |

## 3. Deduplication rule

The 60 information-typed outputs deduplicate by **(ECF domain, output type)** — the domain's L2 processes produce a coherent class of deliverables (designs, assessments, specifications, formal results) that aggregate naturally. The aggregate asset cites every producing process record; the produces edges (capped at 12 per asset for record manageability) carry the per-process assertion. Future refinement tranches can split aggregates into finer-grained named assets where the business distinguishes them.

## 4. Acceptance criteria

1. All gates Findings: 0; CATALOG.yaml 25 canonical.
2. Every produces edge targets a canonical process id (schema-validated).
3. Every record's evidence cites the producing process records.

## 5. NOT-list

1. No `maps-to` classification bindings (deferred tranche).
2. No input-side assets in this batch (input types were predominantly business_object; the 4 input-side assets from CR-IA-CAT-05 stand).
3. No L3/L4 IO derivation (EXT-12 table: optional, separately gated).
