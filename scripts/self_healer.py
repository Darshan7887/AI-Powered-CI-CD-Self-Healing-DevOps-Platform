from ai_engine.analyzer import AIFailureAnalyzer
from scripts.actions import (
    restart_pod,
    rollback_deployment,
    scale_deployment
)


class SelfHealingEngine:
    def __init__(self):
        self.analyzer = AIFailureAnalyzer()

    def handle_failure(self, logs: str, context: dict) -> dict:
        analysis = self.analyzer.analyze(logs)

        action = "No action taken"

        if analysis.get("failure_id") == "K8S_CRASHLOOP":
            action = restart_pod(context.get("pod"))

        elif analysis.get("failure_id") == "K8S_HIGH_CPU":
            action = scale_deployment(context.get("deployment"), replicas=3)

        elif analysis.get("failure_id") in [
            "CI_TEST_FAILURE",
            "DOCKER_BUILD_FAILURE"
        ]:
            action = rollback_deployment(context.get("deployment"))

        return {
            "analysis": analysis,
            "action": action
        }


if __name__ == "__main__":
    # Simulated failure event
    sample_logs = "CrashLoopBackOff: container exited with code 1"
    sample_context = {
        "pod": "ai-devops-app-123",
        "deployment": "ai-devops-app"
    }

    engine = SelfHealingEngine()
    result = engine.handle_failure(sample_logs, sample_context)

    print("=== INCIDENT RESPONSE ===")
    print(result)
