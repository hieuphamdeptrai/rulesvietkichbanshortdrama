# SDCS Tests

- `smoke/`: cheap static checks.
- `behavior/`: expected routing/constraints/forbidden behavior.
- `regression/`: known guardrails including No-Lost-Rule.
- `e2e/`: pipeline contracts.
- `fixtures/`: deterministic valid/invalid sample data.
- `golden-projects/`: reserved for richer benchmarks.

Run `python tools/selftest.py` for release smoke/static checks.
