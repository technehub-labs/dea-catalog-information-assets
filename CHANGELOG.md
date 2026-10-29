# Changelog

All notable changes to this catalog are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Catalog bootstrapped from `dea-metaframework/tools/catalog-repo-template/`
  (TEMPLATE_VERSION 0.1.0). Authored under CR-CATALOG-STRUCT-06b.
- `CR-IA-CAT-01` — catalogue foundation: hybrid metamodel pointer (identity +
  allocation blocks, pinned to OpenDEAM v0.8.0 for `dea:entity-information-asset`),
  `dependencies.yaml` upstream pins (metamodel 1.0.0, root model v0.8.0,
  metaframework v2.6.0, information-classes + business-capabilities catalogs),
  catalogue gates 1–3 (parse, pointer, record posture) wired into
  `validate-catalogue.yml`, README catalogue contract, CONTRIBUTING.
  No records admitted (methodology-first; population gated on CR-IA-CAT-04).
- `CR-IA-CAT-02` — entity schema adoption: `schemas/entity.schema.json` (metamodel v1.0.0 projection +
  evidence/provenance/governance instance layer), vendored relationship-instance contract, valid/invalid
  fixtures, Gate 5 (check_schema.py) wired into CI. No records admitted.
- `CR-IA-CAT-03` — FOUNDATIONS (cardinal scope, exclusions, admission ladder, D-1..D-9 register) and
  record documentation standard (six-section per-record README contract) with Gate 6 wired. No records
  admitted.
- `CR-IA-CAT-04` — initial population: 7 canonical Information Asset records admitted from org-verifiable
  producing sources (capability catalog integrity report, discovery views, readiness record, submittal
  review, map visuals; metamodel conformance report, explorer graph), each carrying a `dea:maps-to`
  classification binding into canonical Information Class ids (first bound objects in the ecosystem);
  Gate 7 (check_crosswalk.py) + vendored information-class registry. CATALOG.yaml regenerated (7 entities).
