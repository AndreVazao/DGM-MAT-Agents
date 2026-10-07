from dgm_contracts import Event

from dgm_mat_agents import AutonomyAgent, ProviderAgent, RepoAgent


class Provider:
    def __init__(self):
        self.calls = 0

    def run(self):
        self.calls += 1


class Task:
    def __init__(self):
        self.calls = []

    def analyze_issue(self, issue_type, description, origin="repo_analysis"):
        self.calls.append((issue_type, description, origin))


def event():
    return Event(event_id="agent-test", event_type="test", source="test", target="agent", payload={})


def test_provider_and_autonomy_use_injected_services():
    provider = Provider()
    task = Task()
    ProviderAgent("provider", provider_service=provider).handle_event(event())
    AutonomyAgent("autonomy", task_service=task).handle_event(event())
    assert provider.calls == 1
    assert task.calls == [("repo", "Potential duplicated systems", "repo_analysis")]


def test_repo_agent_runs_without_core_imports():
    agent = RepoAgent("repo")
    agent.handle_event(event())
    assert agent.health == "healthy"
