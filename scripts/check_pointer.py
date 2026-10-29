#!/usr/bin/env python3
"""Gate 2: metamodel-pointer.yaml is present and internally consistent.

The pointer carries two blocks with two consumers (CR-IA-CAT-01 §5):

  - The top-level identity keys (id/name/abbreviation/version/status/
    metamodel_version/owner/description) are consumed by the vendored
    regenerate_catalog.py to build CATALOG.yaml's catalog block.
  - The `metamodel:` allocation block is validated against the pinned
    OpenDEAM root model by validate-allocation.yml
    (dea-architecture-framework scripts/validate_consumer.py), and the
    identity values asserted here mirror what the root model carries at
    the pinned ref for dea:entity-information-asset.

A finding here means the pointer drifted from its allocation. Fix the
allocation in dea-architecture-framework (or the CR that changed the
identity), not this file.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent

REQUIRED_IDENTITY_FIELDS = (
    "id",
    "name",
    "abbreviation",
    "version",
    "status",
    "metamodel_version",
    "owner",
    "description",
)
REQUIRED_METAMODEL_FIELDS = (
    "version",
    "entity_id",
    "class_alias",
    "layer",
    "building_block",
    "viewer_url",
)

EXPECTED_ID = "dea:catalog-information-assets"
EXPECTED_ABBREVIATION = "IA"
EXPECTED_METAMODEL_VERSION = "v0.8.0"
EXPECTED_ENTITY_ID = "dea:entity-information-asset"
EXPECTED_CLASS_ALIAS = "IA"
EXPECTED_LAYER = "L4"
EXPECTED_BUILDING_BLOCK = "L4-information-knowledge"


def main() -> int:
    findings: list[str] = []

    path = REPO / "metamodel-pointer.yaml"
    if not path.exists():
        print("FAIL: metamodel-pointer.yaml is missing")
        print("Findings: 1")
        return 1

    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    for field in REQUIRED_IDENTITY_FIELDS:
        if field not in doc:
            findings.append(f"missing identity field: {field}")

    if doc.get("id") != EXPECTED_ID:
        findings.append(f"id is {doc.get('id')!r}, expected {EXPECTED_ID!r}")
    if doc.get("abbreviation") != EXPECTED_ABBREVIATION:
        findings.append(f"abbreviation is {doc.get('abbreviation')!r}, expected {EXPECTED_ABBREVIATION!r}")

    mm = doc.get("metamodel") or {}
    for field in REQUIRED_METAMODEL_FIELDS:
        if field not in mm:
            findings.append(f"missing metamodel field: {field}")

    if mm.get("entity_id") != EXPECTED_ENTITY_ID:
        findings.append(f"metamodel.entity_id is {mm.get('entity_id')!r}, expected {EXPECTED_ENTITY_ID!r}")
    if mm.get("class_alias") != EXPECTED_CLASS_ALIAS:
        findings.append(f"metamodel.class_alias is {mm.get('class_alias')!r}, expected {EXPECTED_CLASS_ALIAS!r}")
    if mm.get("layer") != EXPECTED_LAYER:
        findings.append(f"metamodel.layer is {mm.get('layer')!r}, expected {EXPECTED_LAYER!r}")
    if mm.get("building_block") != EXPECTED_BUILDING_BLOCK:
        findings.append(
            f"metamodel.building_block is {mm.get('building_block')!r}, expected {EXPECTED_BUILDING_BLOCK!r}"
        )
    version = str(mm.get("version", ""))
    if not re.fullmatch(r"v\d+\.\d+\.\d+(-[a-z0-9.]+)?", version):
        findings.append(f"metamodel.version {version!r} is not a well-formed pin (vX.Y.Z[-tag])")

    links = doc.get("links") or {}
    for link in ("metamodel_repo", "root_model", "github"):
        if link not in links:
            findings.append(f"missing links.{link}")

    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        print(f"Findings: {len(findings)}")
        return 1

    print("OK: pointer present and internally consistent")
    print("Findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
