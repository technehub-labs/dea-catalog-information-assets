# CR-IA-CAT-05: Process-IO Bridge — First Operational Information Assets

| Field | Value |
|---|---|
| **CR** | CR-IA-CAT-05 |
| **Title** | Process-IO bridge: the first operational information assets, derived from EXT-12 declarations |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Process-definition completeness + information-asset advancement |
| **Repository** | `technehub-labs/dea-catalog-information-assets` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-02 |
| **Depends on** | CR-IA-CAT-04 (population method); dea-catalog-business-processes CR-BP-94-EXT-12 Proceed (PR #219: the pilot IO declarations these assets derive from) |
| **Trigger** | Owner directive: work through the process-IO question comprehensively — advance information assets from the processes' declared information inputs/outputs so process definition, information assets, and information models progress together. |

## 1. Executive summary

Four canonical InformationAsset records admitted, derived one-for-one from the EXT-12 pilot's information-typed IO declarations — the catalog's first **operational** assets (the existing 7 are meta-layer reports). Each carries the producing or consuming process record as its evidence source (repository-path, system-of-record class) and asserts the corresponding `produces`/`consumes` relationship onto the declaring process id. This is the bridge: process records now ground information assets; information assets now point back at processes.

## 2. The bridge records

| Asset | Form | Derived from | Relationship |
|---|---|---|---|
| `dea:information-asset-customer-relationship-review` | report | Manage Customer Relationship outputs[0] | produced-by `processes:process-pr-operate-bbe384`; consumed-by `dea:actor-sales-account-management` |
| `dea:information-asset-acquisition-channel-design` | document | Build Customer Acquisition Channels outputs[0] | produced-by `processes:process-pr-build-nygvw7`; consumed-by `processes:process-pr-operate-bbe384` (operate stage) |
| `dea:information-asset-customer-profile-history` | feed | Manage Customer Relationship inputs[0] | consumed-by `processes:process-pr-operate-bbe384` (producing system is the CRM, not yet a cataloged process) |
| `dea:information-asset-acquisition-requirements-baseline` | document | Build Customer Acquisition Channels inputs[0] | consumed-by `processes:process-pr-build-nygvw7` |

## 3. Semantics notes

- `source_id` values must be canonical ids (schema-enforced): human consumers are expressed as actor-role ids (`dea:actor-...` form), with the EXT-12 free-text consumer preserved in the rationale. An actor catalog cross-reference is a named follow-up.
- `maps-to` classification bindings are deferred to a classification-review tranche (scope of this CR is the bridge).
- The input-side assets have no `produces` assertion: their producing systems (CRM, marketing strategy) are not process records; the consuming assertion is the honest edge today.

## 4. IO backfill plan (the comprehensiveness path)

The corpus census (post-EXT-12): **2 of 146 L2 records declare IO** (the pilots); 144 remain. The backfill proceeds in domain tranches (pr-* family by domain: operate, build, conceive...), each tranche declaring inputs/outputs per EXT-12 sections 6-7 and minting its information-typed items as assets under this bridge method. Target cadence: one domain per CR, evidence-gated.

## 5. Acceptance criteria

1. All gates Findings: 0; CATALOG.yaml 11 canonical.
2. Every relationship source/target is a canonical id or canonical-id form (schema-validated).
3. Every record's evidence cites the declaring process record path.

## 6. NOT-list

1. No `maps-to` classification bindings (deferred tranche).
2. No IO backfill of the remaining 144 L2 records in this CR.
3. No new metamodel relationships; `produces`/`consumes` are existing vocabulary.
