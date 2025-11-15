import time
import sys
from kubernetes import client, config, stream

config.load_kube_config()
apps = client.AppsV1Api()
core = client.CoreV1Api()

NAMESPACE = "default"

def scale_nodes(count):
    apps.patch_namespaced_deployment_scale(
        "chrome-node", NAMESPACE, {"spec": {"replicas": count}}
    )
    print(f"Scaled chrome-node to {count} pods.")

def wait_ready(count):
    while True:
        pods = core.list_namespaced_pod(
            NAMESPACE, label_selector="app=chrome-node"
        ).items

        ready = sum(1 for p in pods if p.status.container_statuses and p.status.container_statuses[0].ready)
        print(f"Pods ready: {ready}/{count}")

        if ready >= count:
            return pods
        time.sleep(3)

def run_tests(pod):
    name = pod.metadata.name
    print(f"Running tests on {name}")
    result = stream.stream(
        core.connect_get_namespaced_pod_exec,
        name, NAMESPACE,
        command=["pytest", "/tests", "-q"],
        stderr=True, stdin=False, stdout=True, tty=False
    )
    print(result)

def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    scale_nodes(count)
    pods = wait_ready(count)
    for p in pods:
        run_tests(p)

if __name__ == "__main__":
    main()
