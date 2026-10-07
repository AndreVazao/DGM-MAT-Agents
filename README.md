# DGM-MAT Agents

Standalone agent implementations extracted from DGM-MAT Core.

## Boundary

Agents depend only on `DGM-Contracts` for public event and service-port types. Core-specific capabilities are injected by adapters owned by DGM-MAT Core.

The satellite intentionally contains no `core.*` imports.

## Current migration status

- Source preserved in DGM-MAT during validation.
- Standalone package copied from the validated Core agent set.
- Provider and autonomy services use injected ports.
- Logging uses the public `AgentLogger` port.
- Local tests and compile validation pass.
- Source deletion from DGM-MAT is deferred until integration consumers are migrated and the full DGM-MAT regression suite is green.
