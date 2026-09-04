# Publish SDCS Story OS 1.0.0 to GitHub

Target repository:
`https://github.com/hieuphamdeptrai/rulesvietkichbanshortdrama`

## Recommended: use the provided Git bundle
The `.bundle` preserves the frozen release commit.

```bash
git clone rulesvietkichbanshortdrama-SDCS-1.0.0.bundle rulesvietkichbanshortdrama
cd rulesvietkichbanshortdrama
git remote set-url origin https://github.com/hieuphamdeptrai/rulesvietkichbanshortdrama.git
git push -u origin main
```

## Or: use the ZIP
Extract the ZIP, then from the extracted repository root:

```bash
git init -b main
git remote add origin https://github.com/hieuphamdeptrai/rulesvietkichbanshortdrama.git
git add .
git commit -m "release: SDCS Story OS 1.0.0"
git push -u origin main
```

If the target repository already contains commits, fetch/merge them deliberately before pushing. Do not use `--force` unless you intentionally want to replace its history.

## Verify after publishing
```bash
python tools/selftest.py
python tools/validate_project.py examples/minimal-project
```

Expected release evidence:
- 35/35 historical versions.
- 1,843 frozen rule records.
- 15/15 consolidated runtime modules.
- 15 core JSON Schemas.
- Self-test PASS.
