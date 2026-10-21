# DGM-MAT-Agents — Migration and Ownership Ledger

**Updated:** 2026-10-21  
**Status:** implementation authority is the satellite package; Core compatibility surface remains intentionally in place.

## Repository responsibilities

- **DGM-MAT:** sovereign brain, mission orchestration, policy, approvals, durable mission/task state, memory and runtime lifecycle.
- **DGM-MAT-Agents:** standalone implementations of bounded specialist agents.
- **DGM-Contracts:** public event/data models and injected service-port protocols shared across repositories.
- **Core composition boundary:** `core/agents/boundary.py` and `core/agents/service_adapters.py` stay in DGM-MAT because they connect public agent interfaces to Core-owned services.

## Agent implementations owned by this repository

The public package exports the following implementations from `src/dgm_mat_agents/`:

- `BaseAgent`
- `ArchitectAgent`
- `AutonomyAgent`
- `DebugAgent`
- `DevOpsAgent`
- `MemoryAgent`
- `ProviderAgent`
- `RefactorAgent`
- `RepoAgent`
- `ResearchAgent`
- `RuntimeAgent`
- `SecurityAgent`
- `SelfImprovementAgent`
- `UIAgent`

Specialization modules under the package belong to the same satellite and must follow the same public-contract boundary.

## Current Core integration

The runtime composition entry point is `core/agents/boundary.py`, called by the Core runtime. It loads `dgm_mat_agents` and injects Core-owned logger, provider and task adapters where required.

Legacy import paths under `core/agents/*.py` are compatibility shims, not implementation authority. Keep them until active consumers and rollback requirements have been verified against the actual checked-out runtime and regression suite.

Historical files under `legacy/` are archive material, not evidence of an active production dependency. Do not delete them as part of this migration.

## Contract and safety rules

1. The agent package may import `dgm_contracts` and its own public/internal package modules.
2. The agent package must not import `core.*`, instantiate Core internals, start a second orchestrator, or bypass approvals.
3. Concrete services are passed through constructor-injected ports defined in DGM-Contracts.
4. Agent output is evidence, not automatic proof of correctness; callers own policy, authorization and durable mission state.
5. Never remove Core shims solely because the implementation was extracted. First inspect imports, runtime composition, tests, packaging and rollback.
6. Never claim a runtime test ran unless the relevant runtime was actually exercised.

## Validation gate

The focused GitHub Actions workflow compiles the satellite package and tests and runs the standalone contract suite. The suite also checks that no Python module under `src/dgm_mat_agents` imports `core.*`.

This satellite workflow does **not** replace DGM-MAT integration/regression tests. Before removing compatibility shims, validate:
- package installation with the intended DGM-Contracts revision;
- runtime composition through `create_runtime_agents()`;
- legacy imports still required by supported consumers;
- provider/task/logger injection behavior;
- relevant DGM-MAT regression tests and the real Windows runtime.

## Migration status

| Area | Authority | State |
|---|---|---|
| Agent implementation modules | DGM-MAT-Agents | Extracted; satellite is authoritative |
| Public data/events/service ports | DGM-Contracts | Separate shared package |
| Runtime orchestration and policy | DGM-MAT | Remains in Core |
| Core service adapters and composition boundary | DGM-MAT | Remain in Core by design |
| Legacy Core import paths | DGM-MAT compatibility shims | Retain pending consumer and rollback verification |
| `legacy/` archive | DGM-MAT | Preserve; no cleanup implied by this ledger |
