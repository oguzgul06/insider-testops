import time
from kubernetes import client, config, stream

config.load_incluster_config()
NAMESPACE = "default"
core = client.CoreV1Api()

def run_tests(pod_name):
    print(f"Running tests on {pod_name}")
    resp = stream.stream(
        core.connect_get_namespaced_pod_exec,
        pod_name,
        NAMESPACE,
        command=["pytest", "/tests", "-q"],
        stderr=True, stdin=False, stdout=True, tty=False
    )
    print(resp)

def main():
    pods = core.list_namespaced_pod(NAMESPACE, label_selector="app=chrome-node").items
    for pod in pods:
        run_tests(pod.metadata.name)

if __name__ == "__main__":
    main()
