# Rules Viết Kịch Bản Short Drama — SDCS Story OS 1.0.1

**SDCS — Short Drama Curiosity System** là Story Operating System cho short drama nhiều tập, tối ưu cho mục tiêu: **khán giả xem tiếp vì bắt buộc phải biết diễn biến tiếp theo**.

Story Core đã đóng băng sau design history **v1.0 → v4.4**. Repo này không phải giant prompt; nó có state, canon, memory, routing, validation, branching, rescue, schemas, templates và tests.

## Quick start
```bash
git clone https://github.com/hieuphamdeptrai/rulesvietkichbanshortdrama.git
```
Giữ nguyên tên folder `rulesvietkichbanshortdrama` để khớp `name` trong `SKILL.md`.

### Dùng như Agent Skill / Codex Skill
Nếu môi trường của bạn hỗ trợ Agent Skills, có thể clone/copy toàn bộ folder repo này vào thư mục skills với đúng tên `rulesvietkichbanshortdrama`. `SKILL.md` là entrypoint; `SYSTEM.md` là runtime bootstrap. Nếu môi trường không tự phát hiện skill, chỉ cần yêu cầu AI đọc hai file này trước.

Sau đó yêu cầu AI:
```text
Đọc SKILL.md và SYSTEM.md.
Tạo project SDCS từ ý tưởng: "..."
```

Nếu resume project: đọc `project.yaml`, `BOOTSTRAP.md`, `PROJECT_STATE.md`, rồi retrieve module theo `runtime/routing.md`.

### Runtime fidelity
SDCS 1.0.1 adds a progressive-disclosure layer: compact modules stay fast, while canonical/high-impact tasks load the matching detailed frozen history sources. This keeps all 1,843 rules callable without duplicating or dumping them into every prompt.

## Core capabilities
Premise/high concept; characters/relationships/secrets; mystery/clue/twist/payoff; 6–50+ episode architecture; pacing/retention; screenplay execution; canon/continuity; memory/context; lint/red-team/simulation/scoring; branching; scheduler; health dashboard; style; rescue; onboarding/import/resume; certification.

## Lifecycle
`INPUT → IDEA → PREMISE → CONCEPT LOCK → CORE TRUTH → STORY BLUEPRINT → EPISODE GRID → EPISODE LOCK → SCREENPLAY → AUDIT → PRODUCTION LOCK`

## Repository map
- `SKILL.md` — skill entrypoint.
- `SYSTEM.md` — compact AI runtime.
- `runtime/` — orchestration/state/authority/context/gates.
- `modules/` — 15 consolidated runtime modules.
- `references/` — progressive-disclosure policy + optional creative references; detailed frozen rules remain in `history/versions/`.
- `history/versions/` — 35 historical design versions.
- `history/rule-inventory.yaml`, `history/RULE_LINEAGE.md` — no-lost-rule proof.
- `schemas/` — core JSON Schemas.
- `templates/` — project/artifact templates.
- `validation/` — core linter config/rules/story tests.
- `tests/` — smoke/behavior/regression/e2e fixtures.
- `tools/` — optional zero-dependency self-tests.
- `examples/minimal-project/` — project demo.
- `projects/` — workspace cho project thật.

## Optional commands
`/new` `/resume` `/status` `/health` `/forge` `/blueprint` `/episode` `/write` `/audit` `/simulate` `/mutate` `/branch` `/rescue` `/validate` `/build` `/certify`

Natural language vẫn là chính.

## Authority
Current explicit decision → Locked Canon → Current State → Approved structured data → Derived artifact → Draft → Idea Bank → Archive.

## Historical preservation
35 version files v1.0→v4.4 được giữ. Mỗi frozen rule có ID và runtime owner trong rule inventory/lineage để consolidate mà không mất logic.

## Release
- Story OS: **1.0.1**
- Frozen design history: **v1.0→v4.4**
- Core: **feature-frozen**

## Scope boundary
Story Core chuẩn bị tới production-ready story/scene/shot contract. Model-specific image/video/voice rendering sẽ là **SDCS Production OS** extension riêng.

## Self-test
```bash
python tools/selftest.py
python tools/contract_tests.py
python tools/validate_project.py examples/minimal-project
```

## License
Chưa chọn license. Repo không tự áp MIT/Apache khi bạn chưa quyết định.
