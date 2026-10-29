# Change Requests: dea-catalog-information-assets

This index tracks every change request that lands on this repository. Landed CRs are immutable; corrections are recorded by later CRs and noted here.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-IA-CAT-01](CR-IA-CAT-01-catalogue-foundation.md) | Information Asset catalogue foundation (methodology-first bring-up) | Landed (this PR) | Hybrid pointer pinned to OpenDEAM v0.8.0; dependency manifest; gates 1–3; README contract. No records admitted. |
| [CR-IA-CAT-02](CR-IA-CAT-02-entity-schema-adoption.md) | Entity schema adoption (metamodel projection + catalogue-instance layer) | Landed (this PR) | Projection + instance layer + vendored relationship-instance contract + fixtures; Gate 5 wired. |
| CR-IA-CAT-03 | FOUNDATIONS + record documentation standard | Planned | Scope boundaries vs DataEntity/BusinessObject; admission ladder; record standard. |
| CR-IA-CAT-04 | Initial population (seed records with classification crosswalks) | Planned | Seed canonical records from org-verifiable artifacts; `dea:maps-to` bindings into information-classes. |
| CR-IA-CAT-05 | Cross-catalogue coordination | Planned | Information-classes crosswalk inbox entries citing CR-IA-CAT-04; capabilities U-2 unblock note. |

## Numbering

Series tag `CR-IA-CAT-NN`, numbered sequentially from 01. Cross-repo CRs that touch this repository are recorded here with their home-repo identifier.

## Related upstream

- Metamodel: [dea-metamodel](https://github.com/technehub-labs/dea-metamodel) — entity `dea:InformationAsset`, lifecycle backfill CR-MET-014.
- Root model: [dea-architecture-framework](https://github.com/technehub-labs/dea-architecture-framework) — allocation `dea:entity-information-asset` (enters at v0.6.0; pinned v0.8.0).
- Classification target: [dea-catalog-information-classes](https://github.com/technehub-labs/dea-catalog-information-classes) — CR-IC-CAT-05 two-sided crosswalk contract.
