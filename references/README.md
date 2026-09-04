# SDCS References — Progressive Disclosure Layer

`modules/` contains compact operational summaries. The **full detailed frozen rules** already exist in `history/versions/`.

SDCS 1.0.1 therefore does **not duplicate** 1,843 rules into another directory. Instead it adds explicit progressive-disclosure routing:

1. `SKILL.md` / `SYSTEM.md` establish runtime behavior.
2. `runtime/routing.md` selects the minimum sufficient compact modules.
3. `runtime/reference-routing.md` maps those modules to the exact detailed historical version files that must be loaded for high-impact work.
4. `history/RULE_LINEAGE.md` and `history/rule-inventory.yaml` prove preservation.

## Load detailed source files when

- committing or changing canon;
- building/locking Core Truth, Blueprint, Episode Card, or Screenplay;
- designing major twist/payoff/finale;
- auditing, red-teaming, simulating, rescuing, or certifying;
- a compact module leaves an ambiguity;
- the user asks for full relevant SDCS rules.

## Smallest-complete-context rule

Do not load all 35 history files by default. Load only the detailed source versions owned by the modules selected for the current task.
