# Kubernetes

## Links

* [Learn Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

## Concepts

* **Kubernetes** automates the distribution and scheduling of application containers across a cluster in a more efficient way.

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


## Vocab

* **kubectl**: Kubernetes CLI. Uses the Kubernetes API to interact with the cluster.
* **minikube**: local Kubernetes cluster intended for application development
