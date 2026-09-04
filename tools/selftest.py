#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
errors, warnings = [], []

def check(cond, msg):
    if not cond:
        errors.append(msg)

def load_yaml(path):
    if yaml is None:
        warnings.append(f"PyYAML unavailable: skipped {path}")
        return None
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"Invalid YAML {path.relative_to(ROOT)}: {e}")
        return None

required = [
    "README.md","SKILL.md","SYSTEM.md","CHANGELOG.md","RELEASE_NOTES.md",
    "sdcs.yaml","RELEASE_MANIFEST.yaml","MODULE_INDEX.md","CAPABILITIES.md",
    "history/RULE_LINEAGE.md","history/rule-inventory.yaml",
    "runtime/orchestrator.md","runtime/routing.md","runtime/reference-routing.md",
    "references/README.md","validation/release-baseline.yaml"
]
for f in required:
    check((ROOT/f).exists(), f"Missing required file: {f}")

baseline = load_yaml(ROOT/"validation/release-baseline.yaml") or {}
expected_versions = int(baseline.get("expected_history_versions", 35))
expected_rules = int(baseline.get("expected_frozen_rule_count", 1843))
expected_modules = int(baseline.get("expected_runtime_modules", 15))
expected_reference_routes = int(baseline.get("expected_reference_routes", 15))
expected_schemas = int(baseline.get("expected_schema_count", 15))
per_version_expected = baseline.get("per_version_rule_count", {})

skill = (ROOT/"SKILL.md").read_text(encoding="utf-8") if (ROOT/"SKILL.md").exists() else ""
check(skill.startswith("---\n"), "SKILL.md missing YAML frontmatter")
m = re.search(r"^name:\s*([^\n]+)", skill, re.M)
check(bool(m), "SKILL.md missing name")
if m:
    check(m.group(1).strip() == ROOT.name, f"SKILL name {m.group(1).strip()} != directory {ROOT.name}")

# Frozen history exact baseline
expected_names = [f"v{major}.{minor}" for major,lo,hi in [(1,0,9),(2,0,9),(3,0,9),(4,0,4)] for minor in range(lo,hi+1)]
hfiles = {p.stem: p for p in (ROOT/"history/versions").glob("v*.md")}
check(set(expected_names) == set(hfiles), f"History mismatch: {len(hfiles)}/{expected_versions}")

all_ids, per_version_actual, owner_missing = [], {}, []
for v,p in sorted(hfiles.items()):
    txt = p.read_text(encoding="utf-8")
    if "Current operational owner" not in txt:
        owner_missing.append(p.name)
    ids = re.findall(r"- \*\*(H-[0-9]+-[0-9]{3})\*\* —", txt)
    per_version_actual[v] = len(ids)
    all_ids.extend(ids)
check(len(all_ids) == expected_rules, f"Frozen rule count changed: {len(all_ids)} != {expected_rules}")
check(len(all_ids) == len(set(all_ids)), f"Duplicate rule IDs: {len(all_ids)-len(set(all_ids))}")
check(not owner_missing, f"Missing runtime owner: {owner_missing}")
for v,count in per_version_expected.items():
    check(per_version_actual.get(v) == count, f"{v} rule count changed: {per_version_actual.get(v)} != {count}")

# Module and origin coverage
mods = list((ROOT/"modules").glob("*.md"))
check(len(mods) == expected_modules, f"Expected {expected_modules} modules, found {len(mods)}")
sdcs = load_yaml(ROOT/"sdcs.yaml") or {}
registry_modules = sdcs.get("modules", [])
check(len(registry_modules) == expected_modules, f"sdcs.yaml module count mismatch: {len(registry_modules)}")
registry_paths = {m.get("path") for m in registry_modules}
actual_paths = {p.relative_to(ROOT).as_posix() for p in mods}
check(registry_paths == actual_paths, "sdcs.yaml module paths do not match actual modules")
origins = [v for m in registry_modules for v in m.get("origins", [])]
check(set(origins) == set(expected_names) and len(origins) == len(set(origins)) == expected_versions,
      "Module origin coverage must map every frozen design version exactly once")

# Detailed-source routing: every module and every frozen version must be reachable
refroute = (ROOT/"runtime/reference-routing.md").read_text(encoding="utf-8")
for m in registry_modules:
    check(m.get("id") in refroute, f"Missing reference route for module {m.get('id')}")
    for v in m.get("origins", []):
        check(f"history/versions/{v}.md" in refroute, f"Missing detailed source route for {v}")
check(len(registry_modules) == expected_reference_routes, "Reference route baseline mismatch")

# JSON/YAML validity
schemas = list((ROOT/"schemas").glob("*.json"))
check(len(schemas) == expected_schemas, f"Expected {expected_schemas} schemas, found {len(schemas)}")
for p in schemas:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"Invalid JSON schema {p.name}: {e}")

for f in ["sdcs.yaml","RELEASE_MANIFEST.yaml","history/rule-inventory.yaml","validation/rules.yaml","validation/release-baseline.yaml"]:
    if (ROOT/f).exists():
        load_yaml(ROOT/f)

inv = load_yaml(ROOT/"history/rule-inventory.yaml") or {}
check(inv.get("rule_count") == expected_rules, "Inventory rule_count does not match frozen baseline")
check(sum(r.get("rule_count",0) for r in inv.get("versions",[])) == expected_rules, "Inventory per-version sum mismatch")
for r in inv.get("versions",[]):
    check(r.get("runtime_owner") in actual_paths, f"Inventory owner missing: {r.get('runtime_owner')}")

# Behavior contracts
try:
    tests = json.loads((ROOT/"tests/behavior/core-routing.json").read_text(encoding="utf-8"))
    stems = {m.stem for m in mods}
    ids = [t.get("id") for t in tests]
    check(len(tests) >= 12, f"Behavior coverage too thin: {len(tests)} < 12")
    check(len(ids) == len(set(ids)), "Duplicate behavior test IDs")
    for t in tests:
        req = set(t.get("expected_required_modules", []))
        forbidden = set(t.get("forbidden_default", []))
        for mid in req | forbidden:
            check(mid in stems, f"Behavior {t.get('id')} references missing module {mid}")
        check(not (req & forbidden), f"Behavior {t.get('id')} requires and forbids same module")
except Exception as e:
    errors.append(f"Behavior test parse failure: {e}")

# Regression contract anchors
try:
    reg = json.loads((ROOT/"tests/regression/core-safety.json").read_text(encoding="utf-8"))
    sys_txt = (ROOT/"SYSTEM.md").read_text(encoding="utf-8")
    for c in reg.get("contracts",[]):
        phrase = c.get("system_phrase")
        if phrase:
            check(phrase in sys_txt, f"Regression contract {c.get('id')} missing SYSTEM anchor")
except Exception as e:
    errors.append(f"Regression test parse failure: {e}")

# Release hygiene
check(not (ROOT/"PUBLISH_TO_GITHUB.md").exists(), "Obsolete PUBLISH_TO_GITHUB.md should not ship in 1.0.1")
check(not (ROOT/".bootstrap").exists(), ".bootstrap must not ship")
check((ROOT/"docs/ACKNOWLEDGEMENTS.md").exists(), "Missing external research acknowledgement")
check((ROOT/"presets/commercial/monetized-series.yaml").exists(), "Missing optional commercial preset")
check((ROOT/"extensions/production-os/ROADMAP.md").exists(), "Missing Production OS handoff roadmap")

print("SDCS SELFTEST — release 1.0.1")
print(f"History versions: {len(hfiles)}/{expected_versions}")
print(f"Frozen rules: {len(all_ids)}/{expected_rules}")
print(f"Runtime modules: {len(mods)}/{expected_modules}")
print(f"Detailed source routes: {len(registry_modules)}/{expected_reference_routes}")
print(f"Schemas: {len(schemas)}/{expected_schemas}")
for w in warnings:
    print("WARN:", w)
if errors:
    for e in errors[:80]:
        print("FAIL:", e)
    print(f"RESULT: FAIL ({len(errors)} errors)")
    sys.exit(1)
print("RESULT: PASS")
