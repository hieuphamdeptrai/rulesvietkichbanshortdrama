---
name: rulesvietkichbanshortdrama
description: Stateful Vietnamese Short Drama Curiosity System (SDCS) Story OS for developing addictive short-drama series from raw idea through premise, characters, mystery, episode architecture, screenplay, validation, branching, rescue, continuity, handoff, and release readiness. Use for ongoing short-drama projects where curiosity, canon, payoff, retention, and cross-episode consistency must be preserved.
compatibility: Agent Skills-compatible clients; usable manually by any capable AI that can read Markdown/YAML/JSON files.
metadata:
  release: "1.0.1"
  language: "vi"
  framework: "SDCS Story OS"
---

# SDCS Story OS — Rules Viết Kịch Bản Short Drama

## Use When
- Phát triển short drama nhiều tập từ ý tưởng thô đến premise, blueprint, episode grid và screenplay.
- Cần retention bằng **tò mò diễn biến**, không chỉ shock hoặc cliff giả.
- Cần giữ canon, knowledge, clue/payoff, continuity xuyên nhiều tập hoặc nhiều phiên chat.
- Cần audit, branch A/B/C, Rescue Mode, hoặc tiếp tục project từ repo.

## Don't Use When
- Chỉ cần viết một câu/caption không liên quan story dài.
- Chỉ cần model-specific image/video/voice rendering; đó là Production OS extension.
- Muốn brainstorm không canon hoàn toàn: dùng Prototype Mode và đánh dấu NON-CANON.

## Workflow
1. Đọc `SYSTEM.md`.
2. Có project: đọc `project.yaml`, `BOOTSTRAP.md`, `PROJECT_STATE.md`; chưa có: onboarding.
3. Xác định Current State, Current Bottleneck, Next Best Action.
4. Chỉ tải module cần cho task theo `runtime/routing.md`.
5. Canon pipeline: Premise → Core Truth → Character/Relationship → Blueprint → Information Architecture → Episode Grid → Episode Lock → Screenplay → Audit → Production Prep.
6. Sau thay đổi lớn: lint, impact/continuity, update source, invalidate derived artifacts, refresh bootstrap.
7. Quyết định lớn chưa chắc → Branch; project đang hỏng → Rescue; output chuẩn bị lock → Certification.

## Progressive Disclosure
- Luôn đọc `SYSTEM.md`, sau đó dùng `runtime/routing.md` để chọn compact modules.
- Khi task có ảnh hưởng canon lớn, chuẩn bị lock, audit, rescue, certification, major twist/payoff/finale: đọc thêm các detailed frozen source được map trong `runtime/reference-routing.md`.
- Không load toàn bộ 1.843 rule mặc định; chỉ load **smallest complete detailed subsystem**.
- `history/versions/` dùng để audit lineage/no-lost-rule hoặc khi cần truy nguyên rule.

## Rules
- Mỗi scene/episode phải tạo lý do cụ thể khiến khán giả cần biết tiếp.
- Story Integrity > Character Logic > Curiosity > Payoff > Production Feasibility > Novelty > Polish.
- Locked Canon không đổi âm thầm. User đổi thì unlock → ripple → update → regression check.
- Writer Truth, Audience Belief, Character Knowledge, Spoken Claim và Current State không được trộn.
- Không random twist, invisible clue, fake cliff, stupid-character plot, setup không payoff, consequence reset.
- Mọi episode canon phải có meaningful state change/progress; twist không bắt buộc.
- Major twist phải có footprints và consequence.
- Derived artifact không vượt source of truth; stale artifact không dùng như current.
- Repo là long-term memory; chat là working context. Dùng smallest complete context.
- Validator không tự sửa creative canon.
- Không thêm core module sau v4.4 nếu chưa chứng minh capability gap.
- Toàn bộ lịch sử v1.0→v4.4 phải có lineage, không mất rule trong im lặng.

## Examples
- `Tôi có ý tưởng: cô dâu nghe người ngoài cửa gọi đúng biệt danh của người cha đã chết.` → Project Seed + Premise Forge.
- `Viết tập 12.` → gate check + Episode Card + N-1/N/N+1 + knowledge/continuity/style.
- `Thử 3 ending.` → isolated experiment branches; winner chưa vào MAIN trước merge.
- `Arc 3 càng sửa càng chán.` → Rescue Mode, root-cause first.

## Edge Cases
- Demo nhanh → Prototype Mode, NON-CANON.
- Existing project chưa có schema → migrate theo mức cần, không bắt rebuild toàn bộ.
- User đổi Locked Truth → tôn trọng nhưng tính blast radius và invalidate downstream.
- Đã production/publish → ưu tiên reframe/insert/edit trước hard retcon nếu integrity cho phép.
- Thiếu dữ liệu → UNKNOWN/PROVISIONAL/ASSUMPTION, không bịa cho đầy form.

## References
- `SYSTEM.md` — runtime bootstrap.
- `runtime/` — state, routing, authority, gates, context.
- `modules/` — consolidated operational knowledge.
- `history/versions/` và `history/RULE_LINEAGE.md` — frozen history và no-lost-rule proof.
- `templates/`, `schemas/`, `validation/`, `tests/` — artifact/data/QA layer.
