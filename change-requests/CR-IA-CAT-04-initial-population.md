# CR-IA-CAT-04: Initial Population

| Field | Value |
|---|---|
| **CR** | CR-IA-CAT-04 |
| **Title** | Initial population: seven seed records with classification crosswalks |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Asset catalog bring-up (unblocks capabilities U-2) |
| **Repository** | `technehub-labs/dea-catalog-information-assets` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-29 |
| **Depends on** | CR-IA-CAT-01, CR-IA-CAT-02, CR-IA-CAT-03 |
| **Trigger** | Roadmap continuation. The 8 canonical Information Classes (dea-catalog-information-classes) have had no bound objects since their population; this CR admits the first. |

## 1. Executive summary

This CR admits the first seven canonical Information Asset records, each derived from an org-verifiable producing source and each carrying a `dea:maps-to` classification crosswalk into a canonical Information Class id. These are the first bound objects in the ecosystem for the information-classes catalogue, and the first canonical `dea:information-asset-*` id scheme — the scheme the capabilities catalogue's `realization.information` array (U-2) was recorded as awaiting.

## 2. Seed selection (D-9)

Per FOUNDATIONS D-9, only assets whose producing sources verifiably exist at admission time are admitted — no hypothetical or planned assets. All seven sources were corroborated at admission (ladder stage `corroborated`, 2026-10-29):

| Record | Consumption form | Producing source |
|---|---|---|
| `dea:information-asset-capability-catalog-integrity-report` | report | capabilities `docs/reports/CATALOG-INTEGRITY-REPORT.md` (generated, CR-DEA-BC-51) |
| `dea:information-asset-capability-discovery-views` | dashboard | capabilities `docs/views/` (4 generated views, CR-DEA-BC-47) |
| `dea:information-asset-capability-release-readiness-record` | document | capabilities `docs/reports/RELEASE-READINESS-RRR-2026-01.md` (CR-DEA-BC-60) |
| `dea:information-asset-capability-submittal-review-a001` | document | capabilities `submittal-reviews/BC-SR-A001.md` |
| `dea:information-asset-capability-map-visuals` | document | capabilities `visuals/v01..v09` (4 cited as series heads) |
| `dea:information-asset-metamodel-conformance-report` | report | metamodel `conformance/CONFORMANCE-REPORT-v0.1.md` |
| `dea:information-asset-metamodel-explorer-graph` | dashboard | metamodel `viewer/entity-graph.json` + `metamodel.svg` |

Deliberately excluded (D-9): the capability-map release artifact (its A3 render exists only at a release tag; the post-reset tags are withdrawn — no live artifact), and any asset whose source lives outside org repositories.

## 3. Classification bindings

Every record asserts one `maps-to` instance (Gate 7 validates target form, registry membership, mapping block, rationale, provenance):

- `dea:information-class-confidential` — the integrity report (aggregates gate findings and residual defects; need-to-know consumption).
- `dea:information-class-internal` — the other six (internal governance/discovery artifacts; no regulated content).

Binding semantics note (recorded as a metamodel follow-up, not fixed here): the `mapping.kind` vocabulary (equivalent/broader/narrower/related/traceability/external-crosswalk) has no sensitivity-classification value; bindings carry `kind: related` with an explicit classification rationale. Registering a `classification` kind is a `dea-metamodel` CR candidate.

## 4. Scope

### In scope

1. Seven record subtrees under `entities/v1-alpha/dea:information-asset-*/` (record + per-record README per the record standard).
2. `reconciliation/information-class-registry.yaml`: vendored snapshot of the 8 canonical class ids (source: information-classes CATALOG.yaml, fetched 2026-10-29) with the refresh rule.
3. `scripts/check_crosswalk.py` (Gate 7) and workflow Step 7.
4. `CATALOG.yaml` regenerated (7 entities); README status + admitted-records table; FOUNDATIONS roadmap row; CHANGELOG; register row.

### Out of scope

1. IC-side coordination (crosswalk inbox entries and inverse references in `dea-catalog-information-classes` — CR-IA-CAT-05).
2. Any `derived-from` lineage assertion (data-entities catalogue unpopulated; absence is honest).
3. Metamodel lifecycle backfill for `dea:InformationAsset` (CR-MET-014, lands after this CR).
4. Capabilities-side population of `realization.information` (the capabilities catalogue's own CR, once it consumes this id scheme).

## 5. Acceptance criteria

1. All seven records pass Gate 5 (schema), Gate 6 (documentation standard), Gate 7 (crosswalk).
2. `CATALOG.yaml` counts: entities 7, canonical 7, open_change_requests 0.
3. Every maps-to target is in the vendored registry; every binding carries mapping/rationale/provenance.
4. Authorship gate: all authorship-bearing fields carry allowlisted values.
5. CI Steps 1–7 green.

## 6. NOT-list

1. No schema or vocabulary changes.
2. No records beyond the seven seeds; further admissions require a CR.
3. No remote resolution in any gate (the registry snapshot is the offline contract).
4. No classification other than via `maps-to` instances (no classification field).
