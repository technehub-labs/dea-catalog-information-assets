# Contributing to dea-catalog-information-assets

## Change control

Every change lands through a change request (CR) recorded in `change-requests/` and carried by a pull request against `main`. Direct pushes to `main` are reserved for the initial scaffold (house precedent: capabilities, information-classes).

CR format follows the house pattern (metadata table with CR/Title/Status/Layer/Programme/Repository/Author/Date, numbered sections, an explicit out-of-scope list, verifiable acceptance criteria). See `change-requests/CR-IA-CAT-01` for the shape. Every CR registers a row in `change-requests/README.md`.

## Workflow

1. Branch: `feat/CR-IA-CAT-NN-short-title`.
2. Implement; regenerate the index when entity content changes: `python3 scripts/regenerate_catalog.py --schema catalog-index-schema/catalog-index-schema.json`.
3. Run the gates locally (see README §Local validation). All must print `Findings: 0`.
4. Open a pull request; CI runs the same gates plus the allocation validator and the authorship gate.
5. Verify checks are green before merge (no branch protection — the discipline is manual).

## Authorship cardinal rule

Every authorship-bearing field (`**Owner**`, `**Author**`, stewards, actors in provenance ladders) carries `Emmanuel A. Otchere` or `TechNeHub Labs` — never an agent or tool name. The gate (`scripts/check_authorship.py --strict`, AUT-001..003, from CR-BP-118) blocks otherwise. The denylist includes `Coder (for eaojnr)`; it must not be reintroduced.

## Pointer discipline

`metamodel-pointer.yaml` declares the entity allocation; allocation changes go through the root model (`dea-architecture-framework`), not through the pointer. `CATALOG.yaml` is machine-generated; never hand-edit it — regenerate.
