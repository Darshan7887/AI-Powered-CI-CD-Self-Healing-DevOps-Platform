# AI-Powered CI/CD & Self-Healing DevOps Platform

## Overview
This project is a **self-healing DevOps platform** that detects system failures, analyzes them using AI-assisted logic, and automatically suggests or triggers recovery actions.

In simple terms, it behaves like an **automated DevOps/SRE engineer** that:
- notices failures,
- understands why they happened,
- decides what to do,
- and documents the incident.

---

## What This Project Does (Simple Explanation)

1. **Simulates real failures**
   - Application crashes
   - Kubernetes pod failures
   - CI/CD-related issues

2. **Reads failure logs**
   - Example: `CrashLoopBackOff`, `ImagePullBackOff`, test failures

3. **AI analyzes the failure**
   - Matches logs with known failure patterns
   - Identifies root cause and impact
   - Suggests fixes and prevention steps

4. **Self-healing logic runs**
   - Restart pod
   - Rollback deployment
   - Scale application
   - Or report only if unknown

5. **Generates an incident report**
   - What happened
   - Why it happened
   - What action was taken
   - How to prevent it next time

All of this can be demonstrated with **one command**.

---

## One-Command Demo

Run the complete system using:

```bash
./demo.sh
