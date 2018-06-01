# Installation on Kubernetes Cluster

## Create secrets

Create a [secret object](https://kubernetes.io/docs/concepts/configuration/secret/#creating-your-own-secrets) for the ATSD [collector user](https://axibase.com/docs/atsd/administration/collector-account.html). This account will be used by collector instances to transmit metrics securely into the database.

Create a [`secret.yaml`](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-manually) file with the [following content](./files/secret.yaml):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: axibase
type: Opaque
data:
  collector-pass: MTIzNDU2Nzg5MA==
```

Create the secret using the [`kubectl create`](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#create) command:

```sh
$ kubectl create -f ./secret.yaml
secret "axibase" created
```

## Install ATSD

### Create ATSD Deployment

Create a [deployment object](https://kubernetes.io/docs/concepts/workloads/controllers/deployment) for ATSD configured using the following [`atsd-deployment.yaml`](./files/atsd-deployment.yaml) file as an example.

```yaml
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: atsd
  labels:
    app: atsd
    tier: deployment
spec:
  selector:
    matchLabels:
      app: atsd
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: atsd
    spec:
      containers:
      - image: axibase/atsd:latest
        name: atsd
        env:
        - name: COLLECTOR_USER_TYPE
          value: api-rw
        - name: COLLECTOR_USER_NAME
          value: collector
        - name: COLLECTOR_USER_PASSWORD
          valueFrom:
            secretKeyRef:
              name: axibase
              key: collector-pass
        ports:
        - containerPort: 8081
          name: tcp
        - containerPort: 8443
          name: https
        resources:
          requests:
            memory: "600Mi"
          limits:
            memory: "1200Mi"

```

Notes:

* `atsd` deployment is defined in `metadata: name` field.
* The deployment consists of one pod.
* The `selector` field defines how the deployment finds pods to be managed. In this case, we simply select a pod based on the label defined in the Pod template (`app: atsd`).
* The pod template’s specification, or `template: spec` field, indicates that the Pod should run one container, named `atsd`, which runs the latest [atsd](https://hub.docker.com/r/axibase/atsd/) image from Docker Hub.
* The deployment opens ports 8081 and 8443.

The `template` field contains the following instructions for the pod:

* Add label `app: atsd` to the container.
* Create one container and name it `atsd`.
* Run a container from the latest `axibase/atsd` image.
* The container should use [secrets as environment variables](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables), indicated by `valueFrom.secretKeyRef` field.
* The container has a memory request of 600 MiB and a memory limit of 1200 MiB.
* Open ports 8081 and 8443 to accept incoming TCP traffic.

Create the deployment using the [kubectl create](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#create) command:

```sh
$ kubectl create -f ./atsd-deployment.yaml
deployment "atsd" created
```

### Create ATSD Service

Create a [service object](https://kubernetes.io/docs/concepts/services-networking/service/) for ATSD using [`atsd-service.yaml`](./files/atsd-service.yaml) file with the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: atsd
  labels:
    app: atsd
    tier: service
spec:
  ports:
    - protocol: TCP
      port: 8081
      nodePort: 30081
      name: tcp
    - protocol: TCP
      port: 8443
      nodePort: 30443
      name: https
  selector:
    app: atsd
  type: NodePort
```

This specification will create a new Service object named `atsd` which opens TCP ports on any Pod with the `app=atsd` label.

The service type is specified as [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport), whereas each node will redirect traffic to the atsd service on the same port.
The Service automatically creates environment variables, which are [supported by Collector](installation-on-docker.md#environment-variables):

* ATSD_SERVICE_HOST (variable pattern '{service_name}_SERVICE_HOST')
* ATSD_SERVICE_PORT_HTTPS (variable pattern '{service_name}\_SERVICE_PORT_{port_name}'), specified by the `spec.ports` field:

  ```yaml
  spec:
    ports:
      - protocol: TCP
        port: 8443
        name: https
  ```

* ATSD_SERVICE_PORT_TCP (variable pattern '{service_name}\_SERVICE_PORT_{port_name}'), specified by the `spec.ports` field:

  ```yaml
  spec:
    ports:
      - protocol: TCP
        port: 8081
        name: tcp
  ```

Create the service using the [kubectl create](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#create) command:

```sh
$ kubectl create -f ./atsd-service.yaml
service "atsd" created
```

**Note** When using type [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport), the firewall is not opened by default. You need to add firewall rules to allow access for ports, indicated in the `nodePort:` field.

## Install Collector

### Create Collector Deployment

Create a [deployment object](https://kubernetes.io/docs/concepts/workloads/controllers/deployment) for Axibase Collector using [`collector-deployement.yaml`](./files/collector-deployment.yaml) file:

```yaml
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: axibase-collector
  labels:
    app: axibase-collector
    tier: deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: axibase-collector
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: axibase-collector
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
             matchExpressions:
             - key: app
               operator: In
               values:
               - axibase-collector
            topologyKey: kubernetes.io/hostname
      containers:
      - image: axibase/collector:latest
        name: axibase-collector
        env:
        - name: COLLECTOR_USER_NAME
          value: collector
        - name: COLLECTOR_USER_PASSWORD
          valueFrom:
            secretKeyRef:
              name: axibase
              key: collector-pass
        - name: JAVA_OPTS
          value: "-Xmx512m"
        args: ["-job-enable=docker-socket"]
        ports:
        - containerPort: 9443
          hostPort: 9443
          name: https
        volumeMounts:
        - name: docker-socket
          mountPath: /var/run/docker.sock
        resources:
          requests:
            memory: "200Mi"
          limits:
            memory: "600Mi"
      volumes:
      - name: docker-socket
        hostPath:
          path: /var/run/docker.sock
```

Notes:

* `axibase-collector` deployment is defined in `metadata: name` field.
* The Deployment creates **three** replicated Pods, indicated by the [`replicas`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#replicas) field. If you want to install the Collector on each node, the replicas value must be equal node count.
* The `selector` field defines how the deployment finds pods to be managed. In this case, we select a pod based on the label defined in the Pod template (`app: axibase-collector`).
* The pod template’s specification, or `template: spec` field, indicates that the Pod should run one container, named `axibase-collector`, which runs the latest [axibase-collector](https://hub.docker.com/r/axibase/collector/) image from Docker Hub.
* The deployment opens port 9443.

The `template` field contains the following instructions:

* Add label `app: axibase-collector` to each pod.
* Pods use [`affinity`](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity). We have `podAntiAffinity` that will restrict to have two same pods (label `app:axibase-collector`) in one node.
* Create one container and name it `axibase-collector`.
* Create one volume and name it `docker-socket`.
* Run the `axibase/collector` image at latest version.
* The container uses [secrets as environment variables](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables), indicated by `valueFrom.secretKeyRef` field.
* The container has a memory request of 200 MiB and a memory limit of 600 MiB.
* The container uses the `docker-socket` volume, indicated by the `volumeMounts` field.
* Open ports 9443 so that the container can send and accept traffic. The port is also opened on each Node, specified by the `hostPort: 9443` field.

Create the deployment using the [kubectl create](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#create) command:

```sh
$ kubectl create -f ./collector-deployment.yaml
deployment "axibase-collector" created
```

## Verify Installation

View deployments using [kubectl get](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#get):

```sh
$ kubectl get deploy -o wide
NAME                DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS          IMAGES                     SELECTOR
atsd                1         1         1            1           2d        atsd                axibase/atsd:latest        app=atsd
axibase-collector   3         3         3            3           2d        axibase-collector   axibase/collector:latest   app=axibase-collector
```

View pods using [kubectl get](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#get):

```sh
$ kubectl get pod -o wide
NAME                                 READY     STATUS    RESTARTS   AGE       IP          NODE
atsd-1742852640-vvzlk                1/1       Running   0          2d        10.8.0.14   gke-cluster-1-default-pool-fcd89b74-bstn
axibase-collector-2747957227-03dj2   1/1       Running   0          2d        10.8.2.8    gke-cluster-1-default-pool-fcd89b74-96gq
axibase-collector-2747957227-5hr0g   1/1       Running   0          2d        10.8.0.15   gke-cluster-1-default-pool-fcd89b74-bstn
axibase-collector-2747957227-whd99   1/1       Running   0          2d        10.8.1.8    gke-cluster-1-default-pool-fcd89b74-ln58
```

View services using [kubectl get](https://kubernetes.io/docs/user-guide/kubectl/v1.8/#get):

```sh
$ kubectl get service -o wide
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE       SELECTOR
atsd         NodePort    10.11.241.144   <none>        8081:30081/TCP,8443:30443/TCP   3d        app=atsd
kubernetes   ClusterIP   10.11.240.1     <none>        443/TCP                         3d        <none>
```
