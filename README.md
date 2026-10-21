# DGM-MAT-Agents — Standalone Agent Package

## Purpose
Isolated, reusable agent implementations invoked by the sovereign DGM-MAT core through explicit public contracts. This repository is the implementation authority for the agent family.

## Boundaries
- DGM-MAT core remains the only brain and owns orchestration, policy, permissions, mission/task state and durable memory.
- Agents implement bounded capabilities; they must not create a parallel orchestrator or bypass approvals.
- Depend on DGM-Contracts for public interfaces and injected ports; do not import private `core.*` modules.
- Core keeps composition infrastructure and compatibility shims while consumers, regression coverage and rollback requirements are verified. The shims are not the implementation authority.
- No automatic repository cloning.

## Allowed contents
Agent implementations, capability metadata, injected-port adapters, unit/contract tests and package documentation.

## Validation
The focused GitHub Actions workflow compiles the package, checks the Core import boundary and runs the standalone tests. DGM-MAT integration/regression tests remain required for cross-repository changes.

See [Migration and Ownership Ledger](docs/MIGRATION-OWNERSHIP-LEDGER-2026-10-21.md) for the current ownership map and the gate that must pass before compatibility shims can be removed.
