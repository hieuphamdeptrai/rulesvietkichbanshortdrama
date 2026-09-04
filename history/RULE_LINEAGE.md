# Rule Lineage — Compact No-Lost-Rule Proof

This release freezes **1843 rule records** across **35 historical versions**.

> The authoritative per-rule records live in `history/versions/v*.md`. This compact index proves coverage without duplicating every rule a second time. `tools/selftest.py` scans those source files directly.

| Version | Rules | Runtime owner | First ID | Last ID |
|---|---:|---|---|---|
| v1.0 | 34 | `modules/01-curiosity-core.md` | `H-10-001` | `H-10-034` |
| v1.1 | 25 | `modules/01-curiosity-core.md` | `H-11-001` | `H-11-025` |
| v1.2 | 22 | `modules/02-episode-pacing.md` | `H-12-001` | `H-12-022` |
| v1.3 | 24 | `modules/03-twist-hook-cliff.md` | `H-13-001` | `H-13-024` |
| v1.4 | 22 | `modules/03-twist-hook-cliff.md` | `H-14-001` | `H-14-022` |
| v1.5 | 24 | `modules/04-character-relationship.md` | `H-15-001` | `H-15-024` |
| v1.6 | 20 | `modules/05-mystery-clue.md` | `H-16-001` | `H-16-020` |
| v1.7 | 23 | `modules/06-escalation-payoff.md` | `H-17-001` | `H-17-023` |
| v1.8 | 22 | `modules/06-escalation-payoff.md` | `H-18-001` | `H-18-022` |
| v1.9 | 22 | `modules/02-episode-pacing.md` | `H-19-001` | `H-19-022` |
| v2.0 | 34 | `modules/07-premise-blueprint.md` | `H-20-001` | `H-20-034` |
| v2.1 | 34 | `modules/08-quality-execution.md` | `H-21-001` | `H-21-034` |
| v2.2 | 37 | `modules/08-quality-execution.md` | `H-22-001` | `H-22-037` |
| v2.3 | 47 | `modules/08-quality-execution.md` | `H-23-001` | `H-23-047` |
| v2.4 | 36 | `modules/01-curiosity-core.md` | `H-24-001` | `H-24-036` |
| v2.5 | 33 | `modules/01-curiosity-core.md` | `H-25-001` | `H-25-033` |
| v2.6 | 48 | `modules/08-quality-execution.md` | `H-26-001` | `H-26-048` |
| v2.7 | 44 | `modules/08-quality-execution.md` | `H-27-001` | `H-27-044` |
| v2.8 | 51 | `modules/07-premise-blueprint.md` | `H-28-001` | `H-28-051` |
| v2.9 | 60 | `modules/04-character-relationship.md` | `H-29-001` | `H-29-060` |
| v3.0 | 49 | `modules/15-onboarding-certification.md` | `H-30-001` | `H-30-049` |
| v3.1 | 50 | `modules/09-genre-format-style.md` | `H-31-001` | `H-31-050` |
| v3.2 | 69 | `modules/10-continuity-canon.md` | `H-32-001` | `H-32-069` |
| v3.3 | 75 | `modules/11-memory-context.md` | `H-33-001` | `H-33-075` |
| v3.4 | 97 | `modules/12-schema-compiler.md` | `H-34-001` | `H-34-097` |
| v3.5 | 54 | `modules/13-lint-planning-observability.md` | `H-35-001` | `H-35-054` |
| v3.6 | 68 | `modules/12-schema-compiler.md` | `H-36-001` | `H-36-068` |
| v3.7 | 71 | `modules/14-branching-rescue.md` | `H-37-001` | `H-37-071` |
| v3.8 | 85 | `modules/13-lint-planning-observability.md` | `H-38-001` | `H-38-085` |
| v3.9 | 91 | `modules/13-lint-planning-observability.md` | `H-39-001` | `H-39-091` |
| v4.0 | 90 | `modules/09-genre-format-style.md` | `H-40-001` | `H-40-090` |
| v4.1 | 97 | `modules/14-branching-rescue.md` | `H-41-001` | `H-41-097` |
| v4.2 | 99 | `modules/15-onboarding-certification.md` | `H-42-001` | `H-42-099` |
| v4.3 | 93 | `modules/15-onboarding-certification.md` | `H-43-001` | `H-43-093` |
| v4.4 | 93 | `modules/15-onboarding-certification.md` | `H-44-001` | `H-44-093` |

## Preservation contract

- Every historical version from v1.0 through v4.4 must remain present.
- Every frozen rule ID must be unique.
- Every historical version must declare a current operational owner.
- A future semantic change must be ACTIVE, REFINED, SCOPED, or SUPERSEDED explicitly; never silently deleted.
- Run `python tools/selftest.py` to verify the contract.
