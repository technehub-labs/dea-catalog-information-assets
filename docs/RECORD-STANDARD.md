# Record Documentation Standard (CR-IA-CAT-03)

Every canonical Information Asset record must satisfy this standard. Gate 6 (`scripts/check_record_documentation.py`) enforces the machine-checkable subset; steward review enforces the rest.

## 1. Record file

One record per subtree: `entities/v1-alpha/<id>/<id>.yaml`, where `<id>` is the full canonical id (e.g. `dea:information-asset-capability-integrity-report`). The schema (CR-IA-CAT-02) governs the field set. Standard obligations beyond the schema:

1. `name` is the asset's real name as consumers know it (title case), not a slug expansion.
2. `description` states what the asset gives context and form **to**, for whom, and in what consuming purpose — one to three sentences. It must not merely restate the name.
3. `consumption_form` names the form; `other` requires a rationale in the record's README.
4. `evidence.sources` cites at least one source that verifiably exists: a `repository-path` source carries `owner/repo:path` form; a `system-of-record` source names the system; a `published-document` source names the document.
5. `evidence.rationale` says why these sources justify admission (corroboration, not assertion).
6. `provenance.ladder_passage` records the passage to canonical with dates (quoted strings) and authorship-bearing actors (`Emmanuel A. Otchere` or `TechNeHub Labs`).
7. `governance.functional_owner` and `steward` are authorship-bearing fields (AUT rules apply).
8. Classification: either at least one `maps-to` relationship instance targeting a canonical `dea:information-class-*` id (with `mapping`, `rationale`, and `provenance`), or an explicit deferral note in the README with a reason.

## 2. YAML conventions

House lessons, gate-relevant:

- Dates are single-quoted (`'2026-10-29'`) so they stay strings through `yaml.safe_load`.
- Prose with apostrophes uses single quotes with `''` escaping, or double quotes when the prose contains a colon.
- Ids, paths, and enums are plain scalars.

## 3. Per-record README

Each record subtree carries `README.md` with exactly these sections, in order:

```markdown
# <Name>

> <definition — the record's description, quoted verbatim>

## Identity

| Field | Value |
|---|---|
| Id | ... |
| Type | InformationAsset |
| Consumption form | ... |
| Version | ... |
| Lifecycle status | ... |

## Evidence

- sources (as cited in the record)
- rationale

## Classification

The maps-to bindings (class, kind, rationale), or the explicit deferral note.

## Provenance

The ladder passage.

## Governance

Owner, steward, approval status, review date.
```

The definition blockquote must match the record's `description` verbatim (Gate 6 checks this).

## 4. Machine checks (Gate 6)

1. Every canonical record has a sibling `README.md`.
2. The README carries the six required section headings.
3. The definition blockquote equals the record's `description` (first blockquote in the file).
4. The record has non-empty `evidence.rationale` and at least one source of a known `kind`.
5. Either a `maps-to` instance exists or the README's Classification section contains a deferral marker (`Deferred:` prefix line).

## 5. Change discipline

Record changes land through CRs; a record edit regenerates `CATALOG.yaml` in the same PR. Retired records move to the subtree's `retired/` directory with a CR note, never deleted.
