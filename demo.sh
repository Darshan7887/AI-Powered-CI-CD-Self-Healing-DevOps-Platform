#!/usr/bin/env bash

echo "========================================"
echo " AI-Powered CI/CD Self-Healing Demo"
echo "========================================"
echo

echo "[STEP 1] Simulating production failure..."
sleep 1

FAILURE_LOG="CrashLoopBackOff: container exited with code 1"

echo "Injected failure log:"
echo "  $FAILURE_LOG"
echo

echo "[STEP 2] Running AI Analyzer + Self-Healer..."
echo

python3 - <<EOF
from ai_engine.analyzer import analyze_failure

analysis = analyze_failure("$FAILURE_LOG")

print("=== AI FAILURE ANALYSIS ===")
for k, v in analysis.items():
    print(f"{k}: {v}")

print("\\n=== SELF-HEALING ACTION ===")
print(f"Action triggered: {analysis.get('immediate_fix', ['manual_check'])[0]}")
print("Status: SUCCESS")
EOF

echo
echo "========================================"
echo " Demo completed successfully"
echo "========================================"
