# Contributing to SDCS

Story Core 1.0.0 is feature-frozen. A new core capability must first prove a genuine capability gap.

Every meaningful change must:
1. Identify the owner module and overlap with existing modules.
2. Preserve all historical rules or explicitly mark a rule REFINED/SCOPED/SUPERSEDED.
3. Update `history/rule-inventory.yaml` / lineage when rule semantics change.
4. Add or update tests for changed behavior.
5. Update manifests and changelog/release notes when user-visible behavior changes.
6. Never silently alter authority, canon, memory firewall, or branch isolation.

Do not add a new module merely to increase version count.
