from __future__ import annotations

import ast
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1] / "src" / "dgm_mat_agents"


def test_standalone_agent_package_does_not_import_dgm_mat_core_internals():
    violations: list[str] = []

    for path in sorted(PACKAGE_ROOT.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        for node in ast.walk(tree):
            imported_names: list[str] = []
            if isinstance(node, ast.Import):
                imported_names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_names.append(node.module)

            for name in imported_names:
                if name == "core" or name.startswith("core."):
                    violations.append(f"{path.relative_to(PACKAGE_ROOT)}:{node.lineno}: {name}")

    assert not violations, (
        "DGM-MAT-Agents must depend on DGM-Contracts/public injected ports, "
        "not private core.* modules:\n" + "\n".join(violations)
    )
