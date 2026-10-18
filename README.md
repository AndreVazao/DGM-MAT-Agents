# DGM-MAT-Agents — Standalone Agent Package

## Purpose
Isolated, reusable agent implementations that can be invoked by the sovereign DGM-MAT core through explicit public contracts.

## Boundaries
- DGM-MAT core remains the only brain and owns orchestration, policy, permissions, task state and durable memory.
- Agents implement bounded capabilities; they must not create a parallel orchestrator or bypass approvals.
- Depend on DGM-Contracts for public interfaces and injected ports; avoid imports from core internals.
- Keep original implementations in DGM-MAT until all consumers migrate and the full regression suite is green.
- No automatic repository cloning.

## Allowed contents
Agent implementations, capability metadata, injected-port adapters, unit/contract tests and package documentation.

## Validation
Run compile checks, unit tests, contract tests and integration/regression tests in DGM-MAT. Document every consumer and migration state before removing duplicated source from the core.
