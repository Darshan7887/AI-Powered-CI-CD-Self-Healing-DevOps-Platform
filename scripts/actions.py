def restart_pod(pod_name: str):
    return f"Action: Restart pod '{pod_name}'"


def rollback_deployment(deployment_name: str):
    return f"Action: Rollback deployment '{deployment_name}'"


def scale_deployment(deployment_name: str, replicas: int):
    return f"Action: Scale deployment '{deployment_name}' to {replicas} replicas"
