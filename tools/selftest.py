#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
try:
 import yaml
except ImportError:
 yaml=None
ROOT=Path(__file__).resolve().parents[1]; errors=[]; warnings=[]
def check(cond,msg):
 if not cond: errors.append(msg)
required=['README.md','SKILL.md','SYSTEM.md','CHANGELOG.md','RELEASE_NOTES.md','sdcs.yaml','RELEASE_MANIFEST.yaml','MODULE_INDEX.md','CAPABILITIES.md','history/RULE_LINEAGE.md','history/rule-inventory.yaml','runtime/orchestrator.md','runtime/routing.md']
for f in required: check((ROOT/f).exists(),f'Missing required file: {f}')
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''; check(skill.startswith('---\n'),'SKILL.md missing YAML frontmatter'); m=re.search(r'^name:\s*([^\n]+)',skill,re.M); check(bool(m),'SKILL.md missing name')
if m: check(m.group(1).strip()==ROOT.name,f'SKILL name {m.group(1).strip()} != directory {ROOT.name}')
expected=[f'v{major}.{minor}' for major,lo,hi in [(1,0,9),(2,0,9),(3,0,9),(4,0,4)] for minor in range(lo,hi+1)]; hfiles={p.stem for p in (ROOT/'history/versions').glob('v*.md')}; check(set(expected)==hfiles,f'History mismatch: {len(hfiles)}/35')
ids=[]; owner_missing=[]
for p in (ROOT/'history/versions').glob('v*.md'):
 txt=p.read_text(encoding='utf-8'); owner_missing += [] if 'Current operational owner' in txt else [p.name]; ids += re.findall(r'- \*\*(H-[0-9]+-[0-9]{3})\*\* —',txt)
check(len(ids)>=500,f'Frozen rule records too low: {len(ids)}'); check(len(ids)==len(set(ids)),f'Duplicate rule IDs: {len(ids)-len(set(ids))}'); check(not owner_missing,f'Missing runtime owner: {owner_missing}')
mods=list((ROOT/'modules').glob('*.md')); check(len(mods)==15,f'Expected 15 modules, found {len(mods)}')
for p in (ROOT/'schemas').glob('*.json'):
 try: json.loads(p.read_text(encoding='utf-8'))
 except Exception as e: errors.append(f'Invalid JSON schema {p.name}: {e}')
if yaml:
 for f in ['sdcs.yaml','RELEASE_MANIFEST.yaml','history/rule-inventory.yaml','validation/rules.yaml']:
  try: yaml.safe_load((ROOT/f).read_text(encoding='utf-8'))
  except Exception as e: errors.append(f'Invalid YAML {f}: {e}')
 inv=yaml.safe_load((ROOT/'history/rule-inventory.yaml').read_text(encoding='utf-8')); check(inv.get('rule_count')==len(ids),f'Inventory count mismatch'); paths={m.relative_to(ROOT).as_posix() for m in mods}
 for r in inv.get('versions',[]): check(r.get('runtime_owner') in paths,f'Missing owner {r.get("runtime_owner")}')
 check(sum(r.get('rule_count',0) for r in inv.get('versions',[]))==len(ids),'Inventory count sum mismatch')
else: warnings.append('PyYAML unavailable: YAML checks skipped')
try:
 tests=json.loads((ROOT/'tests/behavior/core-routing.json').read_text(encoding='utf-8')); stems={m.stem for m in mods}
 for t in tests:
  for mid in t.get('expected_required_modules',[]): check(mid in stems,f'Behavior {t["id"]} missing module {mid}')
except Exception as e: errors.append(f'Behavior test parse failure: {e}')
print('SDCS SELFTEST — release 1.0.0'); print(f'History versions: {len(hfiles)}/35'); print(f'Frozen rules: {len(ids)}'); print(f'Runtime modules: {len(mods)}/15'); print(f'Schemas: {len(list((ROOT/"schemas").glob("*.json")))}')
for w in warnings: print('WARN:',w)
if errors:
 [print('FAIL:',e) for e in errors[:50]]; print(f'RESULT: FAIL ({len(errors)} errors)'); sys.exit(1)
print('RESULT: PASS')
