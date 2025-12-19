FAILURE_PATTERNS = [

    {
        "id": "CI_DEPENDENCY_FAILURE",
        "type": "ci",
        "match": [
            "ModuleNotFoundError",
            "Could not find a version that satisfies the requirement",
            "pip install failed"
        ],
        "root_cause": "Application dependencies failed to install during the CI phase.",
        "impact": "Pipeline stopped before building the application artifact.",
        "immediate_fix": [
            "Verify dependency versions in requirements.txt",
            "Ensure package name and version exist on PyPI"
        ],
        "prevention": [
            "Pin dependency versions",
            "Add dependency validation step in CI"
        ]
    },

    {
        "id": "CI_TEST_FAILURE",
        "type": "ci",
        "match": [
            "AssertionError",
            "FAILED",
            "pytest failed"
        ],
        "root_cause": "One or more unit tests failed during the CI phase.",
        "impact": "Pipeline halted to prevent broken code from being deployed.",
        "immediate_fix": [
            "Review failing test logs",
            "Fix application logic or update incorrect tests"
        ],
        "prevention": [
            "Improve test coverage",
            "Run tests locally before pushing code"
        ]
    },

    {
        "id": "DOCKER_BUILD_FAILURE",
        "type": "ci",
        "match": [
            "Docker build failed",
            "failed to solve",
            "executor failed running"
        ],
        "root_cause": "Docker image build failed during the CI pipeline.",
        "impact": "No container image was produced for deployment.",
        "immediate_fix": [
            "Verify Dockerfile syntax",
            "Check base image availability"
        ],
        "prevention": [
            "Use minimal and stable base images",
            "Add Docker build validation in CI"
        ]
    },

    {
        "id": "K8S_CRASHLOOP",
        "type": "kubernetes",
        "match": [
            "CrashLoopBackOff",
            "exited with code"
        ],
        "root_cause": "Application container repeatedly crashed after startup.",
        "impact": "Pods remain unavailable and service traffic is disrupted.",
        "immediate_fix": [
            "Inspect pod logs",
            "Verify environment variables and configuration"
        ],
        "prevention": [
            "Add startup validation checks",
            "Improve liveness and readiness probes"
        ]
    },

    {
        "id": "K8S_IMAGE_PULL_ERROR",
        "type": "kubernetes",
        "match": [
            "ImagePullBackOff",
            "ErrImagePull"
        ],
        "root_cause": "Kubernetes failed to pull the container image.",
        "impact": "Pods could not be created, resulting in service downtime.",
        "immediate_fix": [
            "Verify image name and tag",
            "Check container registry access"
        ],
        "prevention": [
            "Use immutable image tags",
            "Validate image availability before deployment"
        ]
    },

    {
        "id": "K8S_LIVENESS_FAILURE",
        "type": "kubernetes",
        "match": [
            "Liveness probe failed",
            "HTTP probe failed"
        ],
        "root_cause": "Liveness probe detected an unhealthy container state.",
        "impact": "Kubernetes restarted the affected container.",
        "immediate_fix": [
            "Check application health endpoint",
            "Adjust probe timing thresholds"
        ],
        "prevention": [
            "Implement lightweight health checks",
            "Tune probe delays for startup time"
        ]
    },

    {
        "id": "K8S_HIGH_CPU",
        "type": "kubernetes",
        "match": [
            "CPU throttling",
            "exceeded cpu limit"
        ],
        "root_cause": "Application exceeded allocated CPU resources.",
        "impact": "Performance degradation and potential pod restarts.",
        "immediate_fix": [
            "Scale replicas using HPA",
            "Optimize application CPU usage"
        ],
        "prevention": [
            "Set realistic resource requests and limits",
            "Use load testing before production"
        ]
    }

]
