# Customer Profile and Relationship History

> The customer profile and relationship history consumed by Manage Customer Relationship: the standing record of the customer, their relationship state, and interaction history, sourced from the CRM system of record.

## Identity

| Field | Value |
|---|---|
| Id | `dea:information-asset-customer-profile-history` |
| Type | InformationAsset |
| Consumption form | feed |
| Version | 1.0.0 |
| Lifecycle status | active |

## Evidence

- repository-path: `entities/v1-alpha/pr-operate/Customer-Lifecycle-Management/Manage-Customer-Relationship/processes-process-pr-operate-bbe384.yaml (EXT-12 inputs[0])`

The declaring process record is the consuming source (EXT-12 pilot): the input is information in consumable form (a standing feed from the CRM). Corroborated at admission.

## Classification

- Deferred: `dea:maps-to` classification binding pending a classification review tranche (CR-IA-CAT-05 bridge scope).

## Classification-or-relationships

- `processes:process-pr-operate-bbe384` --consumes--> this asset. consumed by Manage Customer Relationship (EXT-12 in-customer-profile).

## Provenance

candidate -> corroborated -> reviewed -> canonical, all 2026-11-02, actor Emmanuel A. Otchere (see record `provenance.ladder_passage`).

## Governance

- functional_owner: Emmanuel A. Otchere
- steward: Emmanuel A. Otchere
- approval_status: approved (review_date 2026-11-02)
- established_by: CR-IA-CAT-05
