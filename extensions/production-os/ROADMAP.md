# SDCS Production OS — Handoff Learnings for Future Implementation

**Status:** roadmap only; not part of Story Core 1.0.1 runtime.

A useful AI-video production architecture should preserve story continuity at **scene boundaries**, not treat every generated clip independently.

## Scene boundary contract

Each scene can expose:

- `start_state` — characters, props, costume, location, spatial positions, emotion, lighting, active injuries;
- `end_state` — the same dimensions after the scene;
- `start_keyframe` — optional approved visual anchor;
- `end_keyframe` — optional approved visual anchor;
- `transition_contract` — what must carry into the next scene;
- `motion_intent` — what changes between start/end, separate from static identity;
- `asset_refs` — approved character/location/prop references;
- `generation_meta` — model, seed/settings when meaningful, source versions, approval state.

This extends SDCS v3.2 continuity and v3.6 compiler concepts.

## Tool-execution integrity

When future adapters call image/video/voice APIs:
- missing credentials or failed calls must be surfaced clearly;
- never claim media was generated unless a tool returned an actual artifact;
- secrets stay outside story Markdown/project canon;
- provider-specific code belongs in adapters/extensions, not Story Core.

## Provider independence

Core production contracts should be model-agnostic. Provider adapters translate the same Scene/Shot Pack into model-specific parameters.

## Why this matters

The durable artifact is the **state/transition contract**. A specific generation model can change later without rewriting story architecture.
