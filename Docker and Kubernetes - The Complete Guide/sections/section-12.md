# Section 12 - Onwards to Kubernetes!

* We're running Kubernetes via **Docker Desktop**, not **Minikube**

```sh
% kubectl cluster-info
```

* Kubernetes configuration are used to describe **objects**

* **Object types** (e.g., `StatefulSet`, `ReplicaController`, `Pod`, `Service`)
    - `apiVersion: v1` gives access to a set of object types (e.g., `Pod`, `Namespace`, etc), and `apiVersion: apps/v1` enables access to a different set of object types (e.g., `ControllerRevision`, `StatefulSet`)

* **Nodes** are individual machines or VMs that runs containers, and **masters** are machines or VMs with a set of programs to manager nodes
    - Node > Pods > Containers

* **Pod** runs one or more closely related containers
    - Should only have containers that should be deployed together
    - E.g., `postgres`, `logger`, `backup-manager` is an example of a reasonable pod
    - The **name** property is useful for **logging** and to enable "networking" between containers within a pod
    - Note that the pod has a label `component: web`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: client-pod
  labels:
    component: web
spec:
  containers:
    - name: client
      image: stephengrider/multi-client
      ports:
        - containerPort: 3000
```

* **Service** sets up networking in a Kubernetes Cluster
    - The `selector` is using a **label selector** to select the pod(s) to expose

```yaml
apiVersion: v1
kind: Service
metadata:
  name: client-node-port
spec:
  type: NodePort
  ports:
    - port: 3050
      targetPort: 3000
      nodePort: 31515
  selector:
    component: web
```

| Service Type | Description |
| ------------ | ----------- |
| ClusterIP | will discuss later! |
| NodePort | Exposes a container to the outside world (mostly used for dev purposes) |
| LoadBalancer | will discuss later! |
| Ingress | will discuss later! |

| Pod port | Service port | Description |
| -------- | ------------ | ----------- |
| `containerPort` | `targetPort` | Port used by the containerized application
| - | `port` | Port used by another pod in the cluster to access a given pod |
| - | `nodePort` | Port to expose a NodePort externally. (Optional, else a random value is selected. Must be between 30000-32767.) |


* Traffic flow: **kube-proxy** -> Service NodePort -> Pod

* How to create objects using `kubectl`:
    ```sh
    % kubectl apply -f client-pod.yaml
    pod/client-pod created
    % kubectl apply -f client-node-port.yaml
    service/client-node-port created
    % kubectl get pods
    NAME         READY   STATUS    RESTARTS   AGE
    client-pod   1/1     Running   0          82s
    % kubectl get services
    NAME               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    client-node-port   NodePort    ...             <none>        3050:31515/TCP   60s
    kubernetes         ClusterIP   ...             <none>        ...              45m
    ```

| Command | Description |
| ------- | ----------- |
| `kubectl apply -f <file>.yaml` | Creating objects or applying configuration changes to objects |
| `kubectl get <object-type>` | Viewing resources |

* Deployment flow
    1. apply a deployment file to add new objects
    3. kube-apiserver (part of master) reads in file
    4. adds the desired objects to a list of cluster resources (etcd)
    5. controller notices that cluster isn't in target state
    6. reaches out to nodes to start up desired number of objects
    7. master polls the nodes about objects and status, updates etcd

* So to deploy something, we update the desired state of the master; and the master is responsible for achieving the desired state
    - The master works constantly to maintain the desired state

* Kubernetes supports **imperative** and **declarative** approaches
    - This course will focus on the declarative approach

| Deployment Type | Description |
| --------------- | ----------- |
| **Imperative deployments** | Do exactly these steps to arrive at this container setup |
| **Declarative deployments** | Out container setup should look like this, make it happen |