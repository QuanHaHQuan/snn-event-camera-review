#!/usr/bin/env python3
"""Validate taxonomy pilot CSV syntax, provenance joins and codebook invariants."""

from __future__ import annotations

import csv
import argparse
import copy
import re
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--annotations", type=Path, default=ROOT / "00-index/taxonomy-pilot-annotations.csv")
parser.add_argument("--events", type=Path, default=ROOT / "03-review-draft/taxonomy-pilot-events.csv")
modes = parser.add_mutually_exclusive_group()
modes.add_argument(
    "--standalone-calibration",
    action="store_true",
    help="validate a separate 59-column calibration table without joining or rewriting the immutable pilot history",
)
modes.add_argument("--expansion-batch", action="store_true", help="validate a separate candidate-audit batch under the frozen limited-expansion policy; never rewrite pilot history")
parser.add_argument("--calibration-events", type=Path, help="reversibly validate E2 adjudication against its separate immutable baseline")
args = parser.parse_args()
ANNOTATIONS = args.annotations
TEMPLATE = ROOT / "04-templates/taxonomy-paper-annotation-schema.csv"
AUDIT = ROOT / "00-index/candidate-screening-audit.csv"
EVENTS = args.events
CONTRACT = json.loads((ROOT / "04-templates/taxonomy-paper-annotation-schema.json").read_text())
CODEBOOK = (ROOT / "03-review-draft/taxonomy-annotation-codebook.md").read_text()

JSON_FIELDS = set(CONTRACT["json_fields"])

ENUMS = CONTRACT["enums"]

MULTI = set(CONTRACT["multi_enum_fields"])

JSON_KEYS = {k: set(v) for k, v in CONTRACT["json_keys"].items()}


def fail(errors, rownum, message):
    errors.append(f"row {rownum}: {message}")


with TEMPLATE.open(newline="", encoding="utf-8") as handle:
    template_header = next(csv.reader(handle))
with ANNOTATIONS.open(newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    header = reader.fieldnames
    rows = list(reader)
with AUDIT.open(newline="", encoding="utf-8") as handle:
    audit = {row["paper_id"]: row for row in csv.DictReader(handle)}
if args.standalone_calibration:
    audit = {
        row["paper_id"]: {
            "title": row["canonical_title"],
            "year": row["year"],
            "venue": row["venue"],
            "abstract": row["abstract_text"],
            "abstract_sha256": row["abstract_sha256"],
        }
        for row in rows
    }

errors = []
policy = CONTRACT.get("release_policy", {})
if CONTRACT["status"] == "frozen_limited_expansion":
    if "<!-- release-status: frozen_limited_expansion -->" not in CODEBOOK:
        errors.append("codebook release status differs from JSON contract")
    if not policy.get("batch_expansion_permitted") or policy.get("taxonomy_final"):
        errors.append("limited freeze policy must permit batches without claiming final taxonomy")
if args.expansion_batch:
    if CONTRACT["status"] != "frozen_limited_expansion":
        errors.append("expansion batch requires a limited-expansion freeze")
    protected = [ROOT / "00-index/taxonomy-pilot-annotations.csv", ROOT / CONTRACT["calibration_baseline"]["annotations_path"]]
    if ANNOTATIONS.resolve() in [p.resolve() for p in protected]:
        errors.append("expansion mode cannot bypass canonical pilot/calibration history")
    if len({r["paper_id"] for r in rows}) > policy["later_batch_max_canonical_papers"]:
        errors.append("expansion batch exceeds the frozen canonical-paper cap")
if args.calibration_events and not args.standalone_calibration:
    errors.append("calibration events require standalone-calibration mode")
fields_in_book = re.findall(r"^### F\d+\. `([^`]+)`", CODEBOOK, re.M)
if template_header != CONTRACT["columns"] or fields_in_book != template_header:
    errors.append("codebook F01-F59, CSV header and JSON contract columns differ")
for marker, expected in [("vocabulary", CONTRACT["enums"]), ("nested-vocabulary", CONTRACT["nested_enums"])]:
    body = CODEBOOK.split(f"<!-- {marker}-start -->", 1)[1].split(f"<!-- {marker}-end -->", 1)[0]
    actual = {k: v.split(";") for k, v in re.findall(r"^\| `([^`]+)` \| `([^`]+)` \|$", body, re.M)}
    if actual != expected:
        errors.append(f"{marker} mirror differs from JSON contract")
if header != template_header:
    errors.append("annotation header does not exactly match the schema template")

units = Counter((row["paper_id"], row["annotation_unit"]) for row in rows)
for key, count in units.items():
    if count != 1:
        errors.append(f"duplicate annotation unit {key}: {count}")

for rownum, row in enumerate(rows, 2):
    identity = f"{row['paper_id']} {row['annotation_unit']}"
    for field in header:
        if row[field] == "":
            fail(errors, rownum, f"{identity}: empty field {field}")

    source = audit.get(row["paper_id"])
    if not source:
        fail(errors, rownum, f"{identity}: paper_id absent from audit")
    else:
        for field, audit_field in [("canonical_title", "title"), ("year", "year"), ("venue", "venue"), ("abstract_text", "abstract"), ("abstract_sha256", "abstract_sha256")]:
            if row[field] != source[audit_field]:
                fail(errors, rownum, f"{identity}: {field} does not exactly match audit")
        digest = hashlib.sha256(row["abstract_text"].encode("utf-8")).hexdigest()
        if digest != row["abstract_sha256"]:
            fail(errors, rownum, f"{identity}: recomputed abstract hash differs")

    parsed = {}
    for field in JSON_FIELDS:
        try:
            parsed[field] = json.loads(row[field])
        except json.JSONDecodeError as exc:
            fail(errors, rownum, f"{identity}: invalid JSON in {field}: {exc}")
    if len(parsed) != len(JSON_FIELDS):
        continue

    for field, allowed in ENUMS.items():
        values = row[field].split(";") if field in MULTI else [row[field]]
        if len(values) != len(set(values)):
            fail(errors, rownum, f"{identity}: duplicate enum in {field}")
        bad = [value for value in values if value not in allowed]
        if bad:
            fail(errors, rownum, f"{identity}: illegal {field} values {bad}")
        positions = [allowed.index(value) for value in values if value in allowed]
        if positions != sorted(positions):
            fail(errors, rownum, f"{identity}: {field} values are not in codebook order")
        if len(values) > 1 and any(value in {"unknown", "none", "not_applicable", "pending", "excluded_paper", "redundant_reference"} for value in values):
            fail(errors, rownum, f"{identity}: sentinel mixed with substantive values in {field}")

    for field, required_keys in JSON_KEYS.items():
        value = parsed[field]
        items = value if isinstance(value, list) else [value]
        for item in items:
            if field == "spiking_boundary_map" and item == "not_applicable":
                continue
            if not isinstance(item, dict) or set(item) != required_keys:
                fail(errors, rownum, f"{identity}: {field} has wrong object keys")

    for path, allowed in CONTRACT["nested_enums"].items():
        root, *tail = path.split(".")
        container = parsed[root]
        if container == "not_applicable":
            continue
        if tail == ["*"]:
            values = list(container.values())
        elif tail == ["*", "status"]:
            values = [item["status"] for item in container.values()]
        else:
            values = [item[tail[0]] for item in container]
        if any(value not in allowed for value in values):
            fail(errors, rownum, f"{identity}: illegal nested value in {path}")
    for item in parsed["efficiency_claim_details"]:
        if item["kind"] not in ENUMS["efficiency_evidence"]:
            fail(errors, rownum, f"{identity}: illegal efficiency kind")
    for field in ["evidence_quote_or_paraphrase", "evidence_location", "evidence_basis", "taxonomy_issue", "pdf_check_question"]:
        key = {"taxonomy_issue": "issue_id", "pdf_check_question": "question_id"}.get(field, "evidence_id")
        ids = [item[key] for item in parsed[field]]
        if len(ids) != len(set(ids)):
            fail(errors, rownum, f"{identity}: duplicate {key} in {field}")
    if row["taxonomy_placement"] == "role_hypothesis":
        if row["scope"] != "core_intersection" or row["primary_functional_role"] in {"not_applicable", "unknown"}:
            fail(errors, rownum, f"{identity}: invalid main-taxonomy entry")
    if row["taxonomy_placement"] == "cross_cutting" and row["primary_functional_role"] != "not_applicable":
        fail(errors, rownum, f"{identity}: pure cross-cutting contribution has an inference role")
    if row["primary_functional_role"] == "algorithmic_engine":
        if "algorithm_update" not in row["snn_module_functions"].split(";"):
            fail(errors, rownum, f"{identity}: algorithmic_engine missing algorithm update function")
    if "neuronal_spike_train" in row["representation_form"].split(";"):
        if row["spiking_computation"] != "confirmed" or "event_interface" not in [row["primary_functional_role"], *row["secondary_functional_roles"].split(";")]:
            fail(errors, rownum, f"{identity}: neuronal_spike_train lacks verified interface")
    if row["review_status"] == "astra_adjudicated" and not any(i["owner"] == "astra" and i["status"] in {"resolved", "deferred"} for i in parsed["taxonomy_issue"]):
        fail(errors, rownum, f"{identity}: Astra review lacks issue disposition")

    if args.expansion_batch:
        if row["selection_status"] == "usable":
            fail(errors, rownum, f"{identity}: expansion freeze does not authorize final usable selection")
        graph = "graph_network" in row["architecture_family"].split(";") or "graph" in row["representation_form"].split(";")
        if graph and row["scope"] == "core_intersection" and row["taxonomy_placement"] == "role_hypothesis":
            approved = row["review_status"] == "astra_adjudicated" and row["pdf_check_status"] == "resolved" and any(
                i["issue_id"].startswith("G-") and i["owner"] == "astra" and i["status"] == "resolved"
                for i in parsed["taxonomy_issue"]
            )
            if not approved:
                fail(errors, rownum, f"{identity}: uncalibrated event-graph SNN requires Sol High evidence and Astra G- issue disposition before main placement")

    official = parsed["official_source"]
    if official["pdf_sha256"] == "not_applicable":
        if row["pdf_check_status"] != "not_required":
            fail(errors, rownum, f"{identity}: missing PDF hash without abstract-only closure")
    elif official["pdf_sha256"] == "unknown" and (args.standalone_calibration or args.expansion_batch):
        if row["pdf_check_status"] == "resolved" and not re.search(r"v\d+$", official["version"]):
            fail(errors, rownum, f"{identity}: resolved remote PDF without a byte hash must name an immutable version")
    elif len(official["pdf_sha256"]) != 64:
        fail(errors, rownum, f"{identity}: official PDF hash is not 64 hex characters")

    boundary = parsed["spiking_boundary_map"]
    if boundary == "not_applicable":
        if row["spiking_extent"] != "not_applicable" or row["primary_functional_role"] != "not_applicable":
            fail(errors, rownum, f"{identity}: not_applicable boundary requires no new inference role/extent")
    else:
        for component, item in boundary.items():
            if set(item) != {"status", "detail"}:
                fail(errors, rownum, f"{identity}: boundary {component} keys invalid")
            if item["status"] not in {"all_spiking", "mixed", "non_spiking", "absent", "unknown"}:
                fail(errors, rownum, f"{identity}: boundary {component} status invalid")

    extent = row["spiking_extent"]
    if extent == "fully_spiking_task_network":
        if boundary["backbone"]["status"] != "all_spiking" or boundary["head"]["status"] != "all_spiking":
            fail(errors, rownum, f"{identity}: fully_spiking_task_network requires spiking backbone and head")
        if boundary["fusion"]["status"] not in {"all_spiking", "absent"}:
            fail(errors, rownum, f"{identity}: fully_spiking_task_network has incompatible fusion")
    if extent == "fully_spiking_backbone" and boundary["backbone"]["status"] != "all_spiking":
        fail(errors, rownum, f"{identity}: fully_spiking_backbone lacks all_spiking backbone")
    if extent == "end_to_end_spiking_pipeline" and any(item["status"] not in {"all_spiking", "absent"} for item in boundary.values()):
        fail(errors, rownum, f"{identity}: end_to_end_spiking_pipeline contains a non-all-spiking component")

    if row["scope"] == "core_intersection":
        if row["spiking_computation"] != "confirmed":
            fail(errors, rownum, f"{identity}: finalized core row lacks confirmed spiking computation")
        if row["intersection_directness"] not in {"method_coupled", "event_specific_training_analysis"}:
            fail(errors, rownum, f"{identity}: core row has insufficient intersection directness")

    secondary = row["secondary_functional_roles"].split(";")
    if row["primary_functional_role"] in secondary:
        fail(errors, rownum, f"{identity}: secondary role duplicates primary role")

    if row["selection_status"] == "proposed_usable":
        if row["inclusion_tier"] in {"pending", "redundant_reference", "excluded_paper"}:
            fail(errors, rownum, f"{identity}: proposed usable row has invalid inclusion tier")
        if row["inclusion_reason"] in {"", "not_applicable", "unknown"}:
            fail(errors, rownum, f"{identity}: proposed usable row lacks inclusion reason")
        if row["exclusion_reason"] != "not_applicable":
            fail(errors, rownum, f"{identity}: proposed usable row has exclusion reason")

    quote_ids = {item["evidence_id"] for item in parsed["evidence_quote_or_paraphrase"]}
    location_ids = {item["evidence_id"] for item in parsed["evidence_location"]}
    basis_ids = {item["evidence_id"] for item in parsed["evidence_basis"]}
    if not quote_ids or quote_ids != location_ids or quote_ids != basis_ids:
        fail(errors, rownum, f"{identity}: evidence ID triplets are empty or disconnected")
    references = []
    references.extend(item["evidence_id"] for item in parsed["dataset_evaluation"])
    references.extend(item["evidence_id"] for item in parsed["efficiency_claim_details"])
    for item in parsed["taxonomy_issue"]:
        references.extend(item["evidence_ids"])
    for item in parsed["pdf_check_question"]:
        references.extend(item["evidence_ids"])
    dangling = sorted(set(references) - quote_ids)
    if dangling:
        fail(errors, rownum, f"{identity}: dangling evidence references {dangling}")

    if row["needs_pdf_check"] == "no":
        if row["pdf_check_status"] not in {"resolved", "not_required"}:
            fail(errors, rownum, f"{identity}: no PDF need but status is not closed")
        if any(item["answer"] == "pending" for item in parsed["pdf_check_question"]):
            fail(errors, rownum, f"{identity}: pending PDF question despite closed status")
    if row["needs_pdf_check"] == "yes" and not parsed["pdf_check_question"]:
        fail(errors, rownum, f"{identity}: PDF check required without a question")

if args.standalone_calibration:
    baseline = CONTRACT.get("calibration_baseline")
    canonical_calibration = baseline and ANNOTATIONS.resolve() == (ROOT / baseline["annotations_path"]).resolve()
    if canonical_calibration or args.calibration_events:
        event_path = args.calibration_events or ROOT / baseline["event_path"]
        with event_path.open(newline="", encoding="utf-8") as handle:
            calibration_events = list(csv.DictReader(handle))
        reconstructed = copy.deepcopy(rows)
        lookup = {(r["paper_id"], r["annotation_unit"]): r for r in reconstructed}
        seen = set()
        for event in reversed(calibration_events):
            if event["event_id"] in seen:
                errors.append("duplicate calibration event ID")
            seen.add(event["event_id"])
            if event["event_type"] not in CONTRACT["event_types"] or event["codebook_version"] not in CONTRACT["historical_event_versions"]:
                errors.append("illegal calibration event type/version")
            key = (event["paper_id"], event["annotation_unit"])
            if key not in lookup:
                errors.append(f"calibration event has no row: {key}")
                continue
            changes = json.loads(event["field_changes_json"])
            for field, change in changes.items():
                if field not in header or not isinstance(change, dict) or set(change) != {"from", "to"}:
                    errors.append(f"invalid calibration change: {event['event_id']}")
                    continue
                if lookup[key][field] != change["to"]:
                    errors.append(f"calibration to-value differs: {event['event_id']} {field}")
                lookup[key][field] = change["from"]
        encoded = json.dumps(reconstructed, ensure_ascii=False, separators=(",", ":")).encode()
        if hashlib.sha256(encoded).hexdigest() != baseline["canonical_sha256"]:
            errors.append("reverse calibration migration does not reproduce Sol E2 snapshot")
        if not errors:
            print(f"PASS: {len(calibration_events)} reversible E2 events reproduce the independent Sol calibration snapshot")
if args.standalone_calibration or args.expansion_batch:
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    kind = "expansion batch" if args.expansion_batch else "standalone calibration"
    print(f"PASS: {len(rows)} {kind} rows, {len(set(row['paper_id'] for row in rows))} papers, {len(header)} columns")
    print("PASS: codebook/schema mirrors, enums, evidence links, role/boundary invariants and PDF-check closure")
    print("PASS: candidate-audit identity/abstract joins and limited-freeze gates" if args.expansion_batch else "LIMIT: standalone calibration checks source strings/hashes, not independent official metadata authenticity")
    print("LIMIT: separate table; run default validator independently to protect pilot history. Machine gates do not prove role contracts or detect mislabeled graphs.")
    raise SystemExit(0)

with EVENTS.open(newline="", encoding="utf-8") as handle:
    event_rows = list(csv.DictReader(handle))
event_ids = Counter(row["event_id"] for row in event_rows)
for event_id, count in event_ids.items():
    if count != 1:
        errors.append(f"duplicate event_id {event_id}: {count}")
for rownum, row in enumerate(event_rows, 2):
    try:
        json.loads(row["field_changes_json"])
    except json.JSONDecodeError as exc:
        errors.append(f"event row {rownum}: invalid field_changes_json: {exc}")

# Immutable first-pass/blind history and reversible 0.2 migration.
def canonical_digest(value):
    encoded = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

baseline = CONTRACT["pilot_baseline"]
n = baseline["historical_event_count"]
if canonical_digest(event_rows[:n]) != baseline["historical_events_sha256"]:
    errors.append("historical pilot events were altered")
for name, digest in baseline["blind_file_sha256"].items():
    if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
        errors.append(f"historical blind record was altered: {name}")
reconstructed = copy.deepcopy(rows)
lookup = {(r["paper_id"], r["annotation_unit"]): r for r in reconstructed}
for event in reversed(event_rows[n:]):
    key = (event["paper_id"], event["annotation_unit"])
    changes = json.loads(event["field_changes_json"])
    if key not in lookup:
        errors.append(f"migration event has no annotation: {key}")
        continue
    row = lookup[key]
    for field, change in changes.items():
        if field not in header or not isinstance(change, dict) or set(change) != {"from", "to"}:
            errors.append(f"invalid migration change: {event['event_id']} {field}")
            continue
        if row[field] != change["to"]:
            errors.append(f"migration to-value differs: {event['event_id']} {field}")
        row[field] = change["from"]
if canonical_digest(reconstructed) != baseline["annotations_canonical_sha256"]:
    errors.append("reverse migration does not reproduce the 0.1 pilot snapshot")
for event in event_rows:
    if event["event_type"] not in CONTRACT["event_types"] or event["codebook_version"] not in CONTRACT["historical_event_versions"]:
        errors.append(f"invalid event type/version: {event['event_id']}")

if errors:
    print(f"FAIL: {len(errors)} validation error(s)")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"PASS: {len(rows)} annotation rows, {len(set(row['paper_id'] for row in rows))} papers, {len(header)} columns")
print(f"PASS: {len(event_rows)} audit events; event types {dict(Counter(row['event_type'] for row in event_rows))}")
print("PASS: audit joins, codebook/schema mirrors, nested enums, evidence links, role/boundary invariants and PDF-check closure")
print("PASS: historical blind/events unchanged and every changed cell reversibly migrates to the 0.1 snapshot")
issues = {(row["paper_id"], i["issue_id"]): i for row in rows for i in json.loads(row["taxonomy_issue"])}
print("INFO: issue states", dict(Counter(i["status"] for i in issues.values())))
print("LIMIT: syntax/provenance validation is not a fresh PDF audit, semantic agreement test, or codebook freeze")
