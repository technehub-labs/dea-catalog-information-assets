# CR-IA-CAT-02: Entity Schema Adoption

| Field | Value |
|---|---|
| **CR** | CR-IA-CAT-02 |
| **Title** | Information Asset entity schema adoption (metamodel projection + catalogue-instance layer) |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Asset catalog bring-up (unblocks capabilities U-2) |
| **Repository** | `technehub-labs/dea-catalog-information-assets` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-29 |
| **Depends on** | CR-IA-CAT-01 (foundation) |
| **Trigger** | Continuation of the CR-IA-CAT-01 roadmap: records cannot be admitted until the schema projection and its gate exist. |

## 1. Executive summary

This CR lands the catalogue-instance schema for Information Asset records: a projection of the metamodel entity schema (`dea-metamodel` v1.0.0 `schemas/entities/information-asset.json`) with the catalogue-instance layer (evidence, provenance ladder, governance) added, the metamodel relationship-instance contract vendored for classification crosswalks, fixtures that pin both directions, and Gate 5 (schema projection + record validation) wired into CI.

## 2. Scope

### In scope

1. `schemas/entity.schema.json`: projection with the id pattern narrowed to `^dea:information-asset-[a-z0-9-]+$` (information-classes id precedent), all normative enums mirrored exactly, `relationships[]` typed by the vendored relationship-instance contract, plus the instance layer:
   - `evidence` (required): `sources[]` of `{kind: repository-path|system-of-record|published-document, reference}` + `rationale`.
   - `provenance.ladder_passage[]`: stages `candidate → corroborated → reviewed → canonical` (FOUNDATIONS D-4, landed by CR-IA-CAT-03).
   - `governance`: `functional_owner`/`steward`/`approval_status` (required), `review_date`, `source_and_evidence` — the information-classes instance-layer shape.
2. `schemas/relationship-instance.schema.json`: vendored verbatim from `dea-metamodel` v1.0.0 (119-type closed enum; `mapping` required for `maps-to`; provenance block).
3. `schemas/fixtures/example-valid.yaml` (exercises the full record shape including a `maps-to` classification instance) and `example-invalid.yaml` (wrong namespace/type/lifecycle/consumption_form, missing evidence, `maps-to` without `mapping`).
4. `scripts/check_schema.py` (Gate 5): asserts the projection has not drifted from the embedded metamodel normative values, validates the fixtures in both directions, and validates every canonical record. Relative `$ref` resolution stays offline via an explicit registry mapping.
5. Workflow Step 5 in `validate-catalogue.yml`.

### Out of scope

1. Record population (CR-IA-CAT-04).
2. FOUNDATIONS and the record documentation standard (CR-IA-CAT-03).
3. Crosswalk target resolution against the information-classes catalogue (Gate 6, CR-IA-CAT-04).
4. Any metamodel schema change. The `mapping.kind` vocabulary has no sensitivity-classification value; classification bindings therefore carry `kind: related` with an explicit rationale. Registering a `classification` kind is a metamodel CR candidate (noted in CR-IA-CAT-04 §8), not a local widening.

## 3. Projection rule

The normative field set (id/type/name/description/version/lifecycle_status/consumption_form/external_references/tags/relationships/metadata) mirrors the metamodel schema exactly; the gate embeds the metamodel v1.0.0 values (type const, both enums, required list, id pattern) and fails on drift. Bump the embedded expectations in the same CR that bumps `metamodel_pin` in `dependencies.yaml`. Never widen a normative enum locally: a catalogue that diverges from the metamodel is a second source of truth.

## 4. Classification is a relationship, not a field

Per the metamodel, `dea:maps-to` (target `dea:InformationClass`) is the classification carrier, superseding the legacy "classified by" alias; per information-classes FOUNDATIONS D-6 the crosswalk is recorded on the mapped entity's side. The schema therefore has no `classification` field: records assert `relationships[]` entries of `relationship_type: maps-to` with the required `mapping` block and provenance. Gate 6 (CR-IA-CAT-04) validates the target id form and the two-sided contract.

## 5. Acceptance criteria

1. `python3 scripts/check_schema.py` → `Findings: 0` (projection faithful; fixtures behave; 0 records).
2. CI Step 5 green; Steps 1–4 remain green.
3. `relationship-instance.schema.json` is byte-identical to the metamodel v1.0.0 source.
4. The valid fixture round-trips through `yaml.safe_load` with dates as quoted strings.

## 6. NOT-list

1. No records are admitted.
2. No classification vocabulary is invented locally.
3. No `derived-from` lineage targets are asserted anywhere (data-entities catalogue unpopulated).
4. No changes outside `schemas/`, `scripts/check_schema.py`, `validate-catalogue.yml`, `change-requests/`, `CHANGELOG.md`.
