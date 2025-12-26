from ai_engine.patterns import FAILURE_PATTERNS


def analyze_failure(log_text: str) -> dict:
    """
    Analyze raw logs and match against known failure patterns
    """

    for pattern in FAILURE_PATTERNS:
        for keyword in pattern["match"]:
            if keyword.lower() in log_text.lower():
                return {
                    "failure_id": pattern["id"],
                    "type": pattern["type"],
                    "root_cause": pattern["root_cause"],
                    "impact": pattern["impact"],
                    "immediate_fix": pattern["immediate_fix"],
                    "prevention": pattern["prevention"],
                }

    return {
        "failure_id": "UNKNOWN",
        "type": "unknown",
        "root_cause": "Failure pattern not recognized",
        "impact": "Unknown impact",
        "immediate_fix": ["Manual investigation required"],
        "prevention": ["Improve logging and monitoring"],
    }
