# Machine-readable Story Model & Artifact Compiler
**Origins:** v3.4, v3.6

## Core graph
PROJECT, CHARACTER, SECRET, RELATIONSHIP, MYSTERY, QUESTION, CLUE, PROP, LOCATION, EVENT, ARC, EPISODE, SCENE, SHOT, STATE, AUDIENCE STATE, THEORY, TWIST, SETUP, PAYOFF, DECISION, ISSUE, MUTATION, CONTEXT PACK, PRODUCTION ASSET.

- Use stable readable IDs; status DRAFT/PROVISIONAL/APPROVED/LOCKED/RETIRED/SUPERSEDED.
- Truth/Belief/Claim/State/Plan/Decision are separate concepts.
- Normalize source facts; denormalize into task Context Packs/views.
- One source-of-truth per fact type; derived files never override source.
- State changes reference Events for causal trace.
- Visibility Public/Released/Character Only/Writer Only/Production Only and temporal release protect firewalls.
- Validation strictness rises with project state; schema-valid does not mean story-good.
- Artifact classes Development/Writing/Memory/Audit/Production/Handoff.
- Every artifact contract defines Purpose/Inputs/Required/Optional/Output/Authority/Invalidation.
- Compiler does not invent major missing facts; missing source → OPEN/TBD/blocked depending artifact.
- Writing pipeline: compile Writing Pack→generate→extract deltas→validate→commit.
- Source change marks dependent artifact STALE. Selective/JIT compile; no needless rebuild.
- Public/Audience/Character POV compile physically excludes forbidden truth.
- SCRIPT_SCOPE_DRIFT flags unplanned major story change inside screenplay.
- Most artifacts are views over the same story graph.
