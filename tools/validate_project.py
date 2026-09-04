#!/usr/bin/env python3
from pathlib import Path
import sys
try:
 import yaml
except ImportError:
 yaml=None
p=Path(sys.argv[1] if len(sys.argv)>1 else '.'); errors=[]
for f in ['project.yaml','PROJECT_STATE.md','CANON.md','DECISIONS.md','ISSUES.md']:
 if not (p/f).exists(): errors.append(f'Missing {f}')
if (p/'project.yaml').exists() and yaml:
 try:
  d=yaml.safe_load((p/'project.yaml').read_text(encoding='utf-8')) or {}
  for k in ['project_id','title','project_version','sdcs_release','current_state','current_branch']:
   if not d.get(k): errors.append(f'project.yaml missing {k}')
  states={'INPUT','IDEA','PREMISE','CONCEPT_LOCK','CORE_TRUTH','STORY_BLUEPRINT','EPISODE_GRID','EPISODE_LOCK','SCREENPLAY','AUDIT','PRODUCTION_LOCK'}
  if d.get('current_state') not in states: errors.append(f'Invalid current_state: {d.get("current_state")}')
 except Exception as e: errors.append(f'Invalid project.yaml: {e}')
print(f'Validate project: {p}')
if errors:
 [print('FAIL:',e) for e in errors]; sys.exit(1)
print('RESULT: PASS')
