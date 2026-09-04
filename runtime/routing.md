# Runtime Routing
Use minimum sufficient modules; do not load the whole repo by default.

| Task | Required | Conditional |
|---|---|---|
| Raw idea/new project | `15-onboarding-certification`, `07-premise-blueprint` | `09-genre-format-style` |
| Premise | `07-premise-blueprint`, `01-curiosity-core` | `08-quality-execution`, `09-genre-format-style` |
| Core truth/mystery | `05-mystery-clue`, `07-premise-blueprint`, `06-escalation-payoff` | `03-twist-hook-cliff`, `04-character-relationship` |
| Character/relationship | `04-character-relationship` | `05-mystery-clue`, `09-genre-format-style` |
| Blueprint | `07-premise-blueprint`, `04-character-relationship`, `05-mystery-clue`, `06-escalation-payoff` | `01-curiosity-core`, `09-genre-format-style` |
| Episode card | `02-episode-pacing`, `01-curiosity-core` | `03-twist-hook-cliff`, `04-character-relationship`, `05-mystery-clue`, `06-escalation-payoff`, `10-continuity-canon` |
| Screenplay | `02-episode-pacing`, `04-character-relationship`, `09-genre-format-style`, `10-continuity-canon` | `03-twist-hook-cliff`, `05-mystery-clue`, `06-escalation-payoff` |
| Twist/hook/cliff | `03-twist-hook-cliff`, `01-curiosity-core` | `05-mystery-clue`, `08-quality-execution` |
| Audit/score | `08-quality-execution`, `13-lint-planning-observability` | `10-continuity-canon`, `09-genre-format-style` |
| Continuity/state | `10-continuity-canon`, `11-memory-context` | `12-schema-compiler` |
| Compile artifact | `12-schema-compiler`, `11-memory-context` | task owner |
| Branch | `14-branching-rescue`, `08-quality-execution` | task owner |
| Rescue | `14-branching-rescue`, `13-lint-planning-observability` | root-cause owner |
| Status/planning | `13-lint-planning-observability`, `11-memory-context` | `12-schema-compiler` |
| Import/resume | `15-onboarding-certification`, `11-memory-context`, `10-continuity-canon` | `13-lint-planning-observability` |
| Certification | `15-onboarding-certification`, `13-lint-planning-observability` | relevant gate owners |

## Detailed rule escalation

After selecting compact modules, consult `runtime/reference-routing.md`.

- Canon-changing, high-impact, lock/audit/rescue/certification tasks **must** load the matching detailed `history/versions/*.md` sources mapped in `runtime/reference-routing.md`.
- Low-risk brainstorming/prototype tasks may stay on compact modules.
- Never load all 1,843 rules blindly; load the smallest complete detailed subsystem.
