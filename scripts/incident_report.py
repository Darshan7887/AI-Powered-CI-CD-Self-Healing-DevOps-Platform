from datetime import datetime
import os


def generate_incident_report(analysis: dict, action: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"incident_{timestamp}.md"

    os.makedirs("reports", exist_ok=True)

    content = f"""
# Incident Report

**Timestamp:** {timestamp} UTC  
**Status:** {analysis.get('status', 'unknown')}

---

## Summary
Automated monitoring detected a failure in the system.  
AI-assisted analysis identified the root cause and triggered recovery.

---

## Root Cause
{analysis.get('root_cause', 'Unknown')}

---

## Impact
{analysis.get('impact', 'Impact could not be determined')}

---

## Automated Action Taken
{action}

---

## Prevention Recommendations
"""
    for item in analysis.get("prevention", []):
        content += f"- {item}\n"

    path = os.path.join("reports", report_name)
    with open(path, "w") as f:
        f.write(content.strip())

    return path
