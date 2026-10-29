# Foundations: Information Asset Catalog

This document records the method the catalogue follows: its cardinal scope, its exclusions, its admission criteria, and its decision register. It records direction; it does not constitute the catalog method's full surface — the record documentation standard ([RECORD-STANDARD.md](RECORD-STANDARD.md)) and the schema projection carry the operational contract.

## 1. Cardinal scope

An **Information Asset** is data given context and form for a specific consuming purpose — a report, a dashboard, an invoice, a published document or feed. It is the form information takes when someone consumes it.

The catalogue sits in the middle of the metamodel's information family (the `dea:Information` core anchor, CR-4 §12): Data Entities are raw persistent structures; Information Assets are contextualized, consumption-ready forms derived from them; Knowledge Assets are applied know-how. This catalogue owns the middle position and nothing else.

This catalogue is the classification **target owner's counterpart**: the records here are the objects that Information Class records (`dea-catalog-information-classes`) classify. Until this catalogue existed, the 8 live Information Classes had nothing bound to them, and the capabilities catalogue's `realization.information` array (U-2) had no canonical id scheme to resolve.

## 2. What is deliberately excluded

| Excluded | Belongs to |
|---|---|
| Raw persistent structures (tables, documents, graph nodes) | `dea-catalog-data-entities` (scaffold) |
| Real-world entities of interest (Customer, Order) | `dea-catalog-business-objects` |
| Sensitivity/regulatory bands and their handling requirements | `dea-catalog-information-classes` |
| Applied know-how independent of any actor | knowledge assets (no catalogue yet) |
| The artifact files themselves | the producing systems and repositories cited as evidence |

## 3. Consumption forms

The admission axis is the metamodel's closed `consumption_form` vocabulary: `report`, `dashboard`, `document`, `feed`, `other`. A record that cannot name its consumption form is not yet understood well enough to admit; `other` is a CR-justified escape, not a default.

## 4. Admission criteria and evidence ladder

1. **Consumable form.** The record names a specific consuming purpose and a consumption form.
2. **Producing source.** The record cites at least one evidence source (`repository-path`, `system-of-record`, or `published-document`) that verifiably exists at admission time.
3. **Classification considered.** The record either asserts a `dea:maps-to` classification crosswalk or explicitly defers one with a rationale (unclassified records are a finding at review, not at admission).
4. **No local identities.** Ids take the `dea:information-asset-<slug>` form only; external references live in `external_references` and never substitute for the OpenDEAM id (E004).

Evidence ladder (asserted in `provenance.ladder_passage`):

| Stage | Meaning |
|---|---|
| candidate | Proposed from an evidence source |
| corroborated | The producing source is verified (the artifact exists where cited) |
| reviewed | Steward review against this FOUNDATIONS and the record standard |
| canonical | Admitted by a landing CR |

## 5. Allocation

`dea:entity-information-asset` (alias `IA`), layer L4, building block L4-information-knowledge, pinned against OpenDEAM v0.8.0 (the allocation enters the root model at v0.6.0). The pointer is validated remotely by `validate-allocation.yml` and locally by Gate 2. Upstream pins live in `dependencies.yaml`: metamodel 1.0.0, root model v0.8.0, metaframework v2.6.0.

## 6. Cross-catalogue reference policy

1. **Classification crosswalks are recorded here, on the mapped side** (information-classes FOUNDATIONS D-6): records assert `dea:maps-to` relationship instances targeting `dea:information-class-*` canonical ids. The class catalogue validates its half (inverse references and its crosswalk inbox); neither side resolves remote repositories at gate time.
2. **Lineage waits for canonical targets.** `derived-from` assertions against Data Entities are made only when canonical data-entity ids exist; until that catalogue is populated, absence is honest (the capabilities U-1/U-2 precedent — no local substitutes).
3. **No scheme invention.** Where a sibling id scheme does not exist (business objects pending U-1, resources/systems pending U-2), this catalogue does not invent one.

## 7. Decision-points register

| # | Decision | Status |
|---|---|---|
| D-1 | Methodology-first bring-up: no records are admitted before the schema, standard, and population CR (CR-IA-CAT-01/02/03/04 sequence) | Adopted (CR-IA-CAT-01) |
| D-2 | The catalogue follows the CR-IC-CAT-01 pattern with a hybrid pointer: identity keys for the regenerator + `metamodel:` allocation block for the root-model validator | Adopted (CR-IA-CAT-01) |
| D-3 | Record ids take the `dea:information-asset-<slug>` form (information-classes `dea:`-prefix precedent); no separate namespace token is introduced | Adopted (CR-IA-CAT-01) |
| D-4 | The admission ladder is four stages: candidate → corroborated → reviewed → canonical | Adopted (this CR) |
| D-5 | Classification is a `dea:maps-to` relationship instance, never a record field | Adopted (CR-IA-CAT-02) |
| D-6 | `mapping.kind` for classification bindings is `related` with an explicit rationale until the metamodel defines a `classification` kind (follow-up CR candidate; never a local widening) | Adopted (CR-IA-CAT-02) |
| D-7 | `consumption_form` is the admission axis; `other` requires a CR-level justification | Adopted (this CR) |
| D-8 | `CATALOG.yaml` is committed, not ignored (template deviation): the freshness gate diffs the committed index | Adopted (CR-IA-CAT-01) |
| D-9 | Population admits only assets whose producing sources are org-verifiable artifacts; no hypothetical or planned assets | Adopted (this CR, governs CR-IA-CAT-04) |

## 8. Roadmap

| Phase | CR | State |
|---|---|---|
| Foundation | CR-IA-CAT-01 | Landed |
| Schema | CR-IA-CAT-02 | Landed |
| Record standard (this CR) | CR-IA-CAT-03 | This PR |
| Population | CR-IA-CAT-04 | Next |
| Cross-catalogue coordination | CR-IA-CAT-05 | Planned |
| Metamodel lifecycle backfill | CR-MET-014 (dea-metamodel) | Planned |
| Governance portfolio registration | CR-013 (dea-governance) | Planned |
