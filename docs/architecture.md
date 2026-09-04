# Architecture

```text
USER INTENT
  ↓
ONBOARDING
  ↓
STORY OS / ORCHESTRATOR
  ↓
STATE + CANON
  ↓
MEMORY + TARGETED RETRIEVAL
  ↓
STORY ENGINES
  ↓
ARTIFACT COMPILER
  ↓
LINT / SIMULATION / RED-TEAM / SCORING
  ↓
HEALTH + SCHEDULER
  ↓
LOCK / COMMIT / RESCUE
  ↓
PROJECT REPOSITORY
```

Runtime uses progressive disclosure: load `SYSTEM.md`, current project bootstrap/state, then only the modules required by `runtime/routing.md`.
