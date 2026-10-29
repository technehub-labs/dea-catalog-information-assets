#!/usr/bin/env python3
"""Gate 7: classification crosswalk (CR-IA-CAT-04).

Validates the maps-to side of the two-sided crosswalk contract
(information-classes CR-IC-CAT-05, FOUNDATIONS D-6): every maps-to
relationship instance on a record here must target a canonical
Information Class id in the vendored registry snapshot, carry the required
mapping block, a rationale, and provenance. The class catalogue validates
its own half (inverse references + its crosswalk inbox); neither side
resolves remote repositories at gate time.
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"
REGISTRY_PATH = REPO / "reconciliation" / "information-class-registry.yaml"

TARGET_ID = re.compile(r"^dea:information-class-[a-z0-9-]+$")
CLASSIFICATION_NOTE = "classification"


def main() -> int:
    findings: list[str] = []

    registry = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8")) or {}
    classes = set(registry.get("classes") or [])
    if not classes:
        print(f"FAIL: {REGISTRY_PATH.relative_to(REPO)} carries no class ids")
        print("Findings: 1")
        return 1
    if not registry.get("fetched_at") or not registry.get("source"):
        print(f"FAIL: {REGISTRY_PATH.relative_to(REPO)} must record source and fetched_at")
        print("Findings: 1")
        return 1

    records = sorted(glob.glob(str(REPO / RECORD_GLOB), recursive=True))
    records = [Path(r) for r in records if "/research/" not in r and "/retired/" not in r]
    bindings = 0

    for path in records:
        rel = path.relative_to(REPO)
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        rid = doc.get("id")
        for r in doc.get("relationships") or []:
            if r.get("relationship_type") != "maps-to":
                continue
            bindings += 1
            target = str(r.get("target_id") or "")
            if not TARGET_ID.match(target):
                findings.append(f"{rel}: maps-to target {target!r} is not an Information Class id form")
            elif target not in classes:
                findings.append(
                    f"{rel}: maps-to target {target!r} is not in the vendored class registry "
                    f"(refresh the registry in the same CR, or fix the binding)"
                )
            if r.get("source_id") != rid:
                findings.append(f"{rel}: maps-to source_id {r.get('source_id')!r} does not equal the record id")
            mapping = r.get("mapping") or {}
            if mapping.get("kind") not in ("equivalent", "broader", "narrower", "related", "traceability", "external-crosswalk"):
                findings.append(f"{rel}: maps-to instance lacks a valid mapping.kind")
            rationale = str(r.get("rationale") or "")
            if CLASSIFICATION_NOTE not in rationale.lower():
                findings.append(f"{rel}: maps-to rationale does not state the classification intent")
            prov = r.get("provenance") or {}
            if not prov.get("asserted_by") or not prov.get("asserted_at"):
                findings.append(f"{rel}: maps-to provenance lacks asserted_by/asserted_at")

    print(f"Records: {len(records)}; maps-to bindings: {bindings}")
    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        print(f"Findings: {len(findings)}")
        return 1

    print("OK: every maps-to binding targets a registry class with mapping, rationale, and provenance")
    print("Findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
