from ai_engine.analyzer import analyze_failure


def main():
    simulated_log = "CrashLoopBackOff: container exited with code 1"

    analysis = analyze_failure(simulated_log)

    print("\n[AI ANALYZER RESULT]")
    for k, v in analysis.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
