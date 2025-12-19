from patterns import FAILURE_PATTERNS


class AIFailureAnalyzer:
    def __init__(self, patterns=FAILURE_PATTERNS):
        self.patterns = patterns

    def analyze(self, logs: str) -> dict:
        logs_lower = logs.lower()

        for pattern in self.patterns:
            for signature in pattern["match"]:
                if signature.lower() in logs_lower:
                    return self._generate_report(pattern, logs)

        return {
            "status": "unknown",
            "summary": "No known failure pattern matched.",
            "recommendation": [
                "Inspect full logs manually",
                "Add new failure pattern if recurring"
            ]
        }

    def _generate_report(self, pattern: dict, logs: str) -> dict:
        return {
            "status": "identified",
            "failure_id": pattern["id"],
            "category": pattern["type"],
            "root_cause": pattern["root_cause"],
            "impact": pattern["impact"],
            "immediate_fix": pattern["immediate_fix"],
            "prevention": pattern["prevention"],
        }


if __name__ == "__main__":
    # Example usage (simulation)
    sample_logs = """
    CrashLoopBackOff: container exited with code 1
    Error: REQUIRED_CONFIG not set
    """

    analyzer = AIFailureAnalyzer()
    report = analyzer.analyze(sample_logs)

    for key, value in report.items():
        print(f"{key.upper()}: {value}")
