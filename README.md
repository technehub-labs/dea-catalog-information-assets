# Information Asset

> Data given context and form for a specific consuming purpose (a report, dashboard, invoice); distinct from the raw Data Entity it's contextualized from.

**Layer:** L4 : **Building block:** L4-information-knowledge : **Entity:** `dea:InformationAsset` (class alias `IA`) : **Root model:** [OpenDEAM v0.8.0](https://github.com/technehub-labs/dea-architecture-framework) : **Metamodel:** [v1.0.0](https://github.com/technehub-labs/dea-metamodel)

**Owner:** TechNeHub Labs

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=IA)

## Status

**Foundation.** Scaffold bootstrapped from the catalog-repo template (CR-CATALOG-STRUCT-06b §12 new-repo gate); foundation `CR-IA-CAT-01` (2026-10-29).

This catalogue is the named unblock for the capabilities catalogue's U-2 residual ("information: no owning catalog exists — an org-level creation decision"): it is the owning catalog for information assets, the objects that Information Class records classify.

| Item | State |
|---|---|
| Repository | foundation stage: method and gates landed; population gated on `CR-IA-CAT-04` |
| Metamodel pointer | pinned to OpenDEAM v0.8.0 (the `dea:entity-information-asset` allocation enters the root model at v0.6.0) |
| Dependency manifest | `dependencies.yaml`: metamodel 1.0.0, root model v0.8.0, metaframework v2.6.0, information-classes and business-capabilities catalogs |
| Schema projection | `CR-IA-CAT-02` |
| Record documentation standard | `CR-IA-CAT-03` |
| Population | `CR-IA-CAT-04` (seed records carrying `dea:maps-to` classification crosswalks) |
| Cross-catalogue integration | `CR-IA-CAT-04` + the information-classes crosswalk inbox (CR-IC-CAT-05 D-6 two-sided contract) |
| Generated index | `CATALOG.yaml`, regenerator + strict gate in CI (never hand-edited) |

## What this catalogue is

The catalogue of **information assets**: data given context and form for a specific consuming purpose — a report, a dashboard, an invoice, a published document or feed. An information asset is the form information takes when someone consumes it; it is the entity the Information Class catalogue's sensitivity bands classify, via `dea:maps-to` assertions carried on records here (the crosswalk lives on the mapped side, per information-classes FOUNDATIONS D-6).

## What this catalogue is not

| Not this | Why | Where it lives |
|---|---|---|
| A data-entity catalogue | A data entity is the raw persistent structure (table, document, graph node); an information asset is contextualized from it via `dea:derived-from` | `dea-catalog-data-entities` (scaffold) |
| A business-object catalogue | A business object is the real-world entity of interest (Customer, Order); an information asset may `dea:represents` one | `dea-catalog-business-objects` |
| An information-class catalogue | A class is the sensitivity/regulatory band; this catalogue's records are the objects that get classed | `dea-catalog-information-classes` |
| A knowledge-asset catalogue | Knowledge assets are applied know-how independent of any actor | `dea-catalog-knowledge-assets` (not yet created) |
| A file store | Records describe assets and cite evidence; they do not host the artifacts themselves | The producing systems and repositories cited in each record |

## Entity definition

| Field | Value |
|---|---|
| Entity ID | `dea:InformationAsset` |
| OpenDEAM entity id | `dea:entity-information-asset` |
| Class alias | `IA` |
| Layer | L4 |
| Building block | L4-information-knowledge |
| Root model version | v0.8.0 |
| Metamodel version | 1.0.0 |
| Status | normative |
| Lifecycle | proposed (metamodel backfill to `existing` follows population, CR-MET-014) |

## Key tenets

1. **An information asset is consumed, not stored.** The test: does the record describe data given a consuming purpose (a report, dashboard, invoice)? If it describes a raw persistent structure, it is a Data Entity; if a real-world entity of interest, a Business Object.
2. **Classification lives here, on the mapped side.** Records carry `dea:maps-to` assertions into `dea:information-class-*` canonical ids; the class catalogue validates its half (CR-IC-CAT-05 D-6). Neither side resolves remote repositories at gate time.
3. **Lineage is asserted, not invented.** `dea:derived-from` contextualization from Data Entities is asserted only when canonical data-entity ids exist; until that catalogue is populated, absence is honest (the capabilities U-1/U-2 precedent).
4. **Evidence or it does not exist.** Every admitted record cites the producing source (repository path, system of record) it was derived from; the evidence ladder is ratified in `docs/FOUNDATIONS.md`.
5. **The vocabulary is closed.** `consumption_form` and all enums mirror the metamodel schema; widening either is a metamodel CR, not a schema edit here.

## Catalogue structure

```
dea-catalog-information-assets/
├── metamodel-pointer.yaml           ← entity allocation (identity + metamodel blocks)
├── dependencies.yaml                ← upstream pins (CR-IA-CAT-01)
├── CATALOG.yaml                     ← machine-generated index (do not hand-edit)
├── docs/
│   ├── FOUNDATIONS.md               ← catalogue method (CR-IA-CAT-03)
│   └── RECORD-STANDARD.md           ← record documentation standard (CR-IA-CAT-03)
├── schemas/
│   └── entity.schema.json           ← projection of the metamodel entity schema (CR-IA-CAT-02)
├── scripts/
│   ├── check_parse.py               ← Gate 1: YAML/JSON parsing
│   ├── check_pointer.py             ← Gate 2: pointer consistency
│   ├── check_record_posture.py      ← Gate 3: records-directory posture
│   ├── check_schema.py              ← Gate 4: schema validation (CR-IA-CAT-02)
│   ├── check_record_documentation.py ← Gate 5: record documentation (CR-IA-CAT-03)
│   ├── check_crosswalk.py           ← Gate 6: classification crosswalk (CR-IA-CAT-04)
│   ├── regenerate_catalog.py        ← vendored from dea-metaframework v2.6.0
│   └── check_catalog_index.py       ← vendored from dea-metaframework v2.6.0
├── classifications/                 ← classification vocabularies (empty until needed)
├── contributions/                   ← contribution intake queue
├── entities/
│   └── v1-alpha/                    ← records go here (population gated on CR-IA-CAT-04)
└── .github/workflows/
    ├── ci.yml                       ← authorship gate + shared toolchain (template)
    ├── validate-allocation.yml      ← OpenDEAM allocation validator (root model v0.8.0)
    └── validate-catalogue.yml       ← the catalogue gates
```

## Local validation

Run the gates before opening a pull request. They are the same scripts CI runs.

```bash
python3 scripts/check_parse.py
python3 scripts/check_pointer.py
python3 scripts/check_record_posture.py
python3 scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json
python3 scripts/check_catalog_index.py --strict --schema catalog-index-schema/catalog-index-schema.json
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Every change lands through a change request in `change-requests/`; the authorship cardinal rule (CR-BP-118 / AUT-001..003) is gate-enforced.
