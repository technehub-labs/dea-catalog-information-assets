# CR-IA-CAT-03: FOUNDATIONS and Record Documentation Standard

| Field | Value |
|---|---|
| **CR** | CR-IA-CAT-03 |
| **Title** | FOUNDATIONS and record documentation standard |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Asset catalog bring-up (unblocks capabilities U-2) |
| **Repository** | `technehub-labs/dea-catalog-information-assets` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-10-29 |
| **Depends on** | CR-IA-CAT-01, CR-IA-CAT-02 |
| **Trigger** | Roadmap continuation: population (CR-IA-CAT-04) is gated on the admission method and the record standard. |

## 1. Executive summary

This CR lands the catalogue's method (`docs/FOUNDATIONS.md`: cardinal scope, exclusions, consumption-form admission axis, four-stage evidence ladder, allocation, cross-catalogue policy, nine-entry decision register) and the record documentation standard (`docs/RECORD-STANDARD.md`) with its gate (`scripts/check_record_documentation.py`, Gate 6). No records are admitted.

## 2. Scope

### In scope

1. `docs/FOUNDATIONS.md` with the D-1..D-9 decision register (D-4/D-7/D-9 adopted by this CR).
2. `docs/RECORD-STANDARD.md`: record obligations beyond the schema, YAML conventions, the six-section per-record README contract, machine-check list, change discipline.
3. `scripts/check_record_documentation.py` (Gate 6) and its workflow step (Step 6).
4. `CHANGELOG.md` and register rows.

### Out of scope

1. Record population (CR-IA-CAT-04).
2. Crosswalk target validation (Gate 7, CR-IA-CAT-04).
3. Any metamodel or sibling-catalogue change.

## 3. Key decisions adopted here

- **D-4** — the admission ladder is four stages (candidate → corroborated → reviewed → canonical), asserted in `provenance.ladder_passage`.
- **D-7** — `consumption_form` is the admission axis; `other` requires CR-level justification.
- **D-9** — population admits only assets whose producing sources are org-verifiable artifacts; no hypothetical or planned assets. This governs CR-IA-CAT-04's seed selection.

## 4. Acceptance criteria

1. `python3 scripts/check_record_documentation.py` → `Findings: 0` (0 records).
2. CI Steps 1–6 green.
3. FOUNDATIONS decision register covers every decision the catalogue has taken (cross-checked against CR-IA-CAT-01/02).

## 5. NOT-list

1. No records are admitted.
2. No new vocabulary beyond the metamodel enums.
3. No ECF conformance block (Information Asset is not an ECF-matrix entity; the capabilities overlay does not apply here).
