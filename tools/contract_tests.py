#!/usr/bin/env python3
from pathlib import Path
import json, sys, re

ROOT = Path(__file__).resolve().parents[1]
errors=[]

def fail(msg): errors.append(msg)

# E2E contract is executable as a static consistency test against runtime state machine.
e2e=json.loads((ROOT/"tests/e2e/story-core.json").read_text(encoding="utf-8"))
state_txt=(ROOT/"runtime/state-machine.md").read_text(encoding="utf-8")
for state in e2e["pipeline"]:
    if state not in state_txt and state not in (ROOT/"SYSTEM.md").read_text(encoding="utf-8"):
        fail(f"E2E state missing from runtime docs: {state}")

# Progressive disclosure must be routed from runtime and skill entrypoints.
for f in ["SKILL.md","SYSTEM.md","runtime/routing.md"]:
    txt=(ROOT/f).read_text(encoding="utf-8")
    if "reference" not in txt.lower():
        fail(f"Progressive disclosure not wired in {f}")

# Optional commercial preset must never become default.
try:
    import yaml
    commercial=yaml.safe_load((ROOT/"presets/commercial/monetized-series.yaml").read_text(encoding="utf-8"))
    if commercial.get("default") is not False or commercial.get("status") != "optional":
        fail("Commercial checkpoint preset must remain optional and non-default")
except Exception as e:
    fail(f"Commercial preset parse failure: {e}")

# Production extension must remain outside core runtime registry.
sdcs=(ROOT/"sdcs.yaml").read_text(encoding="utf-8")
if "extensions/production-os" in re.sub(r"(?s)known_scope.*","",sdcs):
    fail("Production OS roadmap must not be registered as Story Core runtime module")

if errors:
    for e in errors: print("FAIL:",e)
    print(f"CONTRACT TESTS: FAIL ({len(errors)})")
    sys.exit(1)
print("CONTRACT TESTS: PASS")
