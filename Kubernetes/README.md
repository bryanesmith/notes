# Kubernetes

## Links

* [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

## About

* **Kubernetes** automates the distribution and scheduling of application containers across a cluster in a more efficient way.

## Architecture

![K8s architecture](images/k8s-architecture.png) 
[source](https://www.youtube.com/watch?v=TlHvYWVUZyc)

| Component | Location | Responsibility |
| --------- | -------- | -------------- |
| Control Plane | Running across multiple distributed master nodes | Controlling state of cluster |
| API Server | Control Plane | Interface between user and control plane, and control plane and  |
| etcd | Control Plane | Distributed key-value store storing cluster's persistent state | 
| Scheduler | Control Plane | Schedules pods onto worker nodes, based on available resources |
| Controller Manager | Control Plane | Runs controllers (e.g., ReplicationController, DeploymentController) which take action on cluster (e.g., ensure exactly 4 replicas; managing rolling deployments) |
| kubelet | Worker Node | Receives instructions from (and communicates with) control plane |
| kube-proxy | Worker Node | Networking proxy that routes traffic and load balances to containers |
| container runtime | Worker Node | Pulls images from container registry, starts and stops containers, managed container resources |

## Basics

### Key Concepts

* **Namespace** are used to name and isolate resources with a Kubernetes clusters
  - Kubernetes provides a default namespace called `default`

* The **control loop** is responsible for observing the state of the cluster and matching the desired state
  - (1) observe -> (2) check differences -> (3) take action -> (1) ...
  - **Reconciling**: the process of applying changes in the control loop
  - **Controllers** (managed by the **Controller Manager**) are responsible for managing resources as part of the control loop
  - E.g., if a replica dies and the cluster has 3 replicas when it should have 4, the control loop creates another replica

### Clusters

* A **Kubernetes cluster** consists of two types of resources:
  - The **Master** coordinates all activities in the cluster, including scheduling, maintaining state, scaling, and updating
  - **Nodes** are VMs or physical computers that act as the workers that run applications
* Each node has a **Kubelet**, which is an agent for managing the node and communicating with the Kubernetes master, and a container runtime (e.g., Docker, rkt)
* A Kubernetes cluster that handles production traffic should have a minimum of three nodes
* The nodes communicate with the master using the Kubernetes API, which the master exposes
  - End users can also use the Kubernetes API directly to interact with the cluster

### Deployment

* Create a **Deployment** configuration in order to deploy containerized application
  - Specify the container image for your application and the number of replicas
* Once the application instances are created, a **Kubernetes Deployment Controller** continuously monitors those instances
  - If the Node hosting an instance goes down or is deleted, the Deployment controller replaces the instance with an instance on another Node in the cluster

### Pods

* A **Pod** is a group of one or more containers, with shared storage/network, and a specification for how to run the containers
  - A Pod always runs on a Node.
  - By default they are visible from other pods and services within the same kubernetes cluster, but not outside that network
* The API server will automatically create an endpoint for each pod, based on the pod name, that is also accessible through the proxy
  - `http://${HOST}:${PORT}/api/v1/namespaces/default/pods/${POD_NAME}/proxy/`
* When a Pod dies, the `ReplicaSet` will dynamically drive the cluster back to desired state via creation of new Pods

### Expose an App

* A **Service** in Kubernetes is an abstraction which defines a logical set of Pods and a policy by which to access them
  - A Service routes traffic across a set of Pods, and enables a loose coupling between dependent Pods
  - A Service named `kubernetes` is created by default by minikube when it starts a cluster
* Each Pod in a Kubernetes cluster has a unique IP address, even Pods on the same Node
  - Those IPs are not exposed outside the cluster without a Service
* `ServiceSpec`: definition of a Service in YAML (preferred) or JSON
* Different types of Services:
  - `ClusterIP` (default): Exposes the Service on an internal IP in the cluster
  - `NodePort`: Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`
  - `LoadBalancer`: Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service
  - `ExternalName`: Exposes the Service using an arbitrary name (specified by `externalName` in the spec) by returning a CNAME record with the name. No proxy is used.
* Services match a set of Pods using `labels` and `selectors`, a grouping primitive that allows logical operation on objects in Kubernetes
  - Labels are key/value pairs attached to objects, and can be attached or modified at any time
  - Labels can be used for many purposes; e.g., designating environments (e.g., prod), tagging versions

### Scaling an App

* Scaling is accomplished by changing the number of replicas in a Deployment
* Kubernetes also supports autoscaling of Pods
* Services have an integrated load-balancer that will distribute network traffic to all Pods of an exposed Deployment
* Once you have multiple instances of an Application running, you would be able to do Rolling updates without downtime

### Rolling Updates

* Rolling updates allow Deployments' update to take place with zero downtime by incrementally updating Pods instances with new ones
* By default, the maximum number of Pods that can be unavailable during the update and the maximum number of new Pods that can be created, is one
  - Both options can be configured to either numbers or percentages (of Pods)
* If a Deployment is exposed publicly, the Service will load-balance the traffic only to available Pods during the update

## Intermediate

### Amazon EKS 

* Managed Kubernetes control plane, just attach your data plane

* Native k8s, CNCF-compliant experience (e.g., Kinect)

* Seamless experience with IAM, S3, CloudWatch, ALB Ingress Controller, AWS Certificate Manager, AWS Cognito, etc. eksctl create cluster. 

* E.g., P3 for training and P2 for inference for batch workflow. 

* Consider 1) Escalator horizontal auto scalar for batch jobs, 2) AWS Deep Learning Containers. AWS-optimized TensorFlow 

* Creating k8s cluster via Kubeflow 

* See MNIST Fashion example in [machine-learning/in-k8s GitHub repo](https://github.com/aws-samples/machine-learning-using-k8s)

* Distributed training with Horovod 

### Custom Resource Definitions (CRD)

* Custom Resource Definition **Manifest**:
  - Think of it like JSON Schema
  - format:
    ```yaml
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomerResourceDefinition
    metadata:
      ...
    spec:
      ...
    ```
  - `scope` is `Namespaced` if belong to a namespace (e.g., pods, deployments) or `Cluster` if cluster-wide
  - To deploy and manage using kubectl:
    ```bash
    > kubectl apply -f my-crds/foo-crd.yaml
    > kubectl get crds 
    NAME                CREATED AT
    foo.example.com     2024-05-12T00:00:00Z
    ```

* Sample CRD:
  ```yaml
  apiVersion: "drupal.example.com/v1"
  kind: Drupal
  metadata:
    name: my-website
  spec:
    databaseEngine: ...
    version: ...
  ```

### Helm

* Value of Helm: 
  1. package manager for K8s
  2. templating engine
  3. release management. 

* **Helm Charts**: bundles of YAML files available in public or private repository

* **Helm Hub** 

* Files:
  - `Chart.yaml`
  - `values.yaml`
  - `charts/`
  - `templates/`

* Template values (`.Values` object) via (1) `values.yaml`, (2) `--values` flag, (3) `--set` flag

* Templating useful for (1) CI/CD and (2) supporting multiple environments

* `% helm install <chartname>`

* **Tiller** server (running with K8s cluster), tracks revisions of charts, supporting upgrades and rollbacks. 
  - Tiller security concerns (too many permissions), removed in Helm v3

### Ingress

- Ingress spec contains rules, which can make different path (or even hosts and subdomains) to different Services

- Ingress Controller (E.g., nginx. AWS ABS) 

### Operators

* **Operators** are primarily for managing stateful applications (e.g., web apps with databases)
  - Operators are a special type of controller
  - While stateless applications are simple, stateful applications are more complicated and may require manual intervention if not using operators (e.g., order of destroying matters, setup, etc)
  - Kubernetes operators replace human operators, and it knows how to automatically deploy, recover, etc

* Operators make use of CRDs

* [OperatorHub.io](https://operatorhub.io/): for Kubernetes community to share operators, though very far from complete

* Different ways to build operators:
  1. In-depth knowledge of Go and Kubernetes API
  2. Kubebuilder 
  3. Operator SDK: supports non-Go -based custom operators


### StatefulSet 

- StatefulSet vs Deployment
  1. Sticky identity for each pod, and stateful names with ordinals. Created in order, deleted in reverse order
  2. Best practice is to use Persistent Volumes with remote storage
  3. Provides individual service DNS names, as well as overall service DNS name. 

- Stateful applications not ideal for containers and hence often use managed services instead


### Misc
- `Secret` and `ConfigMap` components

## Commands

### minikube commands

```shell
minikube version            # verify installed
minikube start
minikube ip
```

### kubectl commands

```shell
# USAGE: kubectl <action> <resource>

kubectl version             # verify installed
kubectl cluster-info        # list Master and KubeDNS
kubectl proxy               # Proxy to forward commands into cluster's private network

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
```

#### Listing resources

```shell
# USAGE: kubectl get        # list resources
kubectl get nodes
kubectl get deployments
kubectl get pods
kubectl get services
```

#### Create Deployment

```shell
# USAGE: kubectl run <name> --image=<image-path> --port=<port>
kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080
```

#### Describe resources

```shell
# USAGE: kubectl describe   # show detailed information about a resource
kubectl describe pods
kubectl describe deployment
kubectl describe services
```

#### Logs

```shell
# USAGE: kubectl logs       # print the logs from a container in a pod
kubectl logs $POD_NAME
```

#### Executing commands

```shell
# USAGE: kubectl exec       # execute a command on a container in a pod
kubectl exec $POD_NAME env
kubectl exec -ti $POD_NAME bash   # Start shell
kubectl exec -ti $POD_NAME curl localhost:8080
```

#### Creating a Service

```shell
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl describe services/kubernetes-bootcamp
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
curl $(minikube ip):$NODE_PORT    # Should work!
```

#### Using Deployment Labels

```shell
kubectl describe deployment       # Name is the Deployment Label
kubectl get pods -l run=kubernetes-bootcamp
kubectl get services -l run=kubernetes-bootcamp
```

#### Label a Pod

```shell
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
kubectl label pod $POD_NAME app=v1
kubectl describe pods $POD_NAME   # Labels section contains label
kubectl get pods -l app=v1        # fetch Pods by label
```

#### Delete a Service

```shell
kubectl delete service -l run=kubernetes-bootcamp
curl $(minikube ip):$NODE_PORT    # Should fail
kubectl exec -ti $POD_NAME curl localhost:8080    # Should work
```

#### Scaling

```shell
kubectl scale deployments/kubernetes-bootcamp --replicas=4
kubectl get deployments           # READY will eventually say 4/4
kubectl get pods -o wide          # More info on the Pods
kubectl describe services/kubernetes-bootcamp   # Find exposed IP and port
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
curl $(minikube ip):$NODE_PORT    # Each time this is executed, different host
```

#### Rolling Update

```shell
kubectl get deployments           # "kubernetes-bootcamp"
kubectl get pods                  # 4 Pods
kubectl describe pods             # Image is v1
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
kubectl get pods                  # Eventually 4 Terminating, 4 Running Pods

# Says: deployment "kubernetes-bootcamp" successfully rolled out
kubectl rollout status deployments/kubernetes-bootcamp  
```

#### Rollback

```shell
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
kubectl get deployments           # Something wrong. 3/4 ready, 3 available

# ... Failed to pull image"gcr.io/google-samples/kubernetes-bootcamp:v10"
# Error response from daemon: manifest for gcr.io/google-samples/kubernetes-bootcamp:v10 not found
kubectl describe pods
kubectl rollout undo deployments/kubernetes-bootcamp
kubectl get deployments           # 4/4 ready eventually.
```

## Vocab

* **kubectl**: Kubernetes CLI. Uses the Kubernetes API to interact with the cluster.
* **minikube**: local Kubernetes cluster intended for application development
