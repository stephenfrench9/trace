	(venv) [seaTrials]$ helm version
	Client: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
	Error: could not find tiller
	(venv) [seaTrials]$ helm get stable/jaeger
	Error: could not find tiller
	(venv) [seaTrials]$ helm home
	/Users/stephenfrench/.helm
	(venv) [seaTrials]$ cd ~/.helm
	-bash: cd: /Users/stephenfrench/.helm: No such file or directory
	(venv) [seaTrials]$ helm fetch stable/jaeger
	Error: Couldn't load repositories file (/Users/stephenfrench/.helm/repository/repositories.yaml).
	You might need to run `helm init` (or `helm init --client-only` if tiller is already installed)
	(venv) [seaTrials]$ helm inspect stable/jaeger
	Error: failed to download "stable/jaeger" (hint: running `helm repo update` may help)
	(venv) [seaTrials]$ helm init
	Creating /Users/stephenfrench/.helm/repository 
	Creating /Users/stephenfrench/.helm/repository/cache 
	Creating /Users/stephenfrench/.helm/repository/local 
	Creating /Users/stephenfrench/.helm/plugins 
	Creating /Users/stephenfrench/.helm/starters 
	Creating /Users/stephenfrench/.helm/repository/repositories.yaml 
	Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com 
	Adding local repo with URL: http://127.0.0.1:8879/charts 
	$HELM_HOME has been configured at /Users/stephenfrench/.helm.
	
	Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.
	
	Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
	To prevent this, run `helm init` with the --tiller-tls-verify flag.
	For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
	Happy Helming!
	(venv) [seaTrials]$ kubectl get pods
	No resources found.
	(venv) [seaTrials]$ kubectl get services
	NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
	kubernetes   ClusterIP   100.64.0.1   <none>        443/TCP   17m
	(venv) [seaTrials]$ kubectl get deployments --namespace=kubesystem
	No resources found.
	(venv) [seaTrials]$ kubectl get deployments --namespace=kube-system
	NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
	dns-controller        1         1         1            1           18m
	kube-dns              2         2         2            2           18m
	kube-dns-autoscaler   1         1         1            1           18m
	tiller-deploy         1         1         1            1           1m
	(venv) [seaTrials]$ kubectl get pods --namespace=kube-system
	NAME                                                                  READY   STATUS    RESTARTS   AGE
	dns-controller-6b574d5cfc-mg64x                                       1/1     Running   0          18m
	etcd-server-events-ip-172-20-33-195.us-west-2.compute.internal        1/1     Running   0          18m
	etcd-server-ip-172-20-33-195.us-west-2.compute.internal               1/1     Running   0          18m
	kube-apiserver-ip-172-20-33-195.us-west-2.compute.internal            1/1     Running   1          17m
	kube-controller-manager-ip-172-20-33-195.us-west-2.compute.internal   1/1     Running   0          18m
	kube-dns-6b4f4b544c-fvhzg                                             3/3     Running   0          18m
	kube-dns-6b4f4b544c-p76p8                                             3/3     Running   0          16m
	kube-dns-autoscaler-6b658bd4d5-42w6f                                  1/1     Running   0          18m
	kube-proxy-ip-172-20-33-195.us-west-2.compute.internal                1/1     Running   0          17m
	kube-proxy-ip-172-20-53-236.us-west-2.compute.internal                1/1     Running   0          16m
	kube-proxy-ip-172-20-54-207.us-west-2.compute.internal                1/1     Running   0          16m
	kube-scheduler-ip-172-20-33-195.us-west-2.compute.internal            1/1     Running   0          17m
	tiller-deploy-7c69c66d57-h9dq7                                        1/1     Running   0          2m
	(venv) [seaTrials]$ helm version
	Client: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
	Server: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
	(venv) [seaTrials]$ helm get stable/jaeger
	Error: invalid release name, must match regex ^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])+$ and the length must not longer than 53
	(venv) [seaTrials]$ helm fetch stable/jaeger
	Error: chart "jaeger" matching "" not found in stable index. (try 'helm repo update'). no chart name found
	(venv) [seaTrials]$ helm get stable/jaeger-operator
	Error: invalid release name, must match regex ^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])+$ and the length must not longer than 53
	(venv) [seaTrials]$ helm install stable/jaeger/operator
	Error: failed to download "stable/jaeger/operator" (hint: running `helm repo update` may help)
	(venv) [seaTrials]$ helm repo update
	Hang tight while we grab the latest from your chart repositories...
	...Skip local chart repository
	...Successfully got an update from the "stable" chart repository
	Update Complete. ⎈ Happy Helming!⎈ 
	(venv) [seaTrials]$ helm fetch stable/jaeger-operator
	(venv) [seaTrials]$ ls
	jaeger-operator-2.3.1.tgz
	(venv) [seaTrials]$ helm get stable/jaeger-operator
	Error: invalid release name, must match regex ^(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])+$ and the length must not longer than 53
	(venv) [seaTrials]$ helm inspect stable/jaeger-operator
	
	apiVersion: v1
	appVersion: 1.10.0
	description: jaeger-operator Helm chart for Kubernetes
	home: https://www.jaegertracing.io/
	icon: https://www.jaegertracing.io/img/jaeger-icon-reverse-color.svg
	maintainers:
	- email: ctadeu@gmail.com
	  name: cpanato
	name: jaeger-operator
	version: 2.3.1
	
	---
	
# Default values for jaeger-operator.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.
	image:
	  repository: jaegertracing/jaeger-operator
	  tag: 1.10.0
	  pullPolicy: IfNotPresent
	
	rbac:
	  # Specifies whether RBAC resources should be created
	  create: true
	
	serviceAccount:
	  # Specifies whether a ServiceAccount should be created
	  create: true
	  # The name of the ServiceAccount to use.
	  # If not set and create is true, a name is generated using the fullname template
	  name:
	
	resources:
	  # limits:
	  #  cpu: 100m
	  #  memory: 128Mi
	  # requests:
	  #  cpu: 100m
	  #  memory: 128Mi
	
	nodeSelector: {}
	
	tolerations: []
	
	affinity: {}

---
# jaeger-operator

[jaeger-operator](https://github.com/jaegertracing/jaeger-operator) is a Kubernetes operator.

## Install

```console
$ helm install stable/jaeger-operator
```

## Introduction

This chart bootstraps a jaeger-operator deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.8+ with Beta APIs enabled

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release stable/jaeger-operator
```

The command deploys jaeger-operator on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the jaeger-operator chart and their default values.

Parameter | Description | Default
--- | --- | ---
`image.repository` | Controller container image repository | `jaegertracing/jaeger-operator`
`image.tag` | Controller container image tag | `1.10.0`
`image.pullPolicy` | Controller container image pull policy | `IfNotPresent`
`rbac.create` | All required roles and rolebindings will be created | `true`
`serviceAccount.create` | Service account to use | `true`
`serviceAccount.name` | Service account name to use. If not set and create is true, a name is generated using the fullname template | ``
`resources` | K8s pod resorces | `None`
`nodeSelector` | Node labels for pod assignment | `{}`
`tolerations` | Toleration labels for pod assignment | `[]`
`affinity` | Affinity settings for pod assignment | `{}`

Specify each parameter you'd like to override using a YAML file as described above in the [installation](#installing-the-chart) section.

You can also specify any non-array parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```console
$ helm install stable/jaeger-operator --name my-release \
    --set rbac.create=false
```

## After the Helm Installation

### Creating a new Jaeger instance
The simplest possible way to install is by creating a YAML file like the following:

```YAML
apiVersion: io.jaegertracing/v1alpha1
kind: Jaeger
metadata:
  name: simplest
```

The YAML file can then be used with `kubectl`:

```console
$ kubectl apply -f simplest.yaml
```

### Creating a new Jaeger with ElasticSearch

To do that you need to have an ElasticSearch installed in your Kubernetes cluster or install one using the [Helm Chart](https://github.com/helm/charts/tree/master/incubator/elasticsearch) available for that.

After that just deploy the following manifest:

```YAML
# setup an elasticsearch with `make es`
apiVersion: io.jaegertracing/v1alpha1
kind: Jaeger
metadata:
  name: simple-prod
spec:
  strategy: production
  storage:
    type: elasticsearch
    options:
      es:
        server-urls: http://elasticsearch:9200
        username: elastic
        password: changeme
```

The YAML file can then be used with `kubectl`:

```console
$ kubectl apply -f simple-prod.yaml
```

(venv) [seaTrials]$ 


# And then nothing works... but you fix it with the first hit on googling the error. 

Its the well upvoted answer on the first hit. Actually, I tried two differnt things with helm. They failed and both threw errors. I googled both. The first hit for both included the same fix, though only one resource included helpful inforomation about how to reset helm - you know - so you could get a fresh start if the fix went ary. And so that you could put the system into the error state easily. 

	(venv) [seaTrials]$ helm list
	Error: configmaps is forbidden: User "system:serviceaccount:kube-system:default" cannot list configmaps in the namespace "kube-system"
	(venv) [seaTrials]$ helm install stable/jaeger-operator
	Error: no available release name found
	(venv) [seaTrials]$ o 1
	rm: line.txt: No such file or directory
	rm: greenfield.sh: No such file or directory
	1 : kubectl create serviceaccount --namespace kube-system tiller
	
	serviceaccount/tiller created
	(venv) [seaTrials]$ n
	2 : kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
	
	clusterrolebinding.rbac.authorization.k8s.io/tiller-cluster-rule created
	(venv) [seaTrials]$ n
	3 : kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
	
	deployment.extensions/tiller-deploy patched
	(venv) [seaTrials]$ n
	4 : helm init --service-account tiller --upgrade
	
	$HELM_HOME has been configured at /Users/stephenfrench/.helm.
	
	Tiller (the Helm server-side component) has been upgraded to the current version.
	Happy Helming!
	(venv) [seaTrials]$ helm list
	(venv) [seaTrials]$ helm install stable/jaeger-operator
	NAME:   mottled-quetzal
	LAST DEPLOYED: Mon Mar 25 19:39:39 2019
	NAMESPACE: default
	STATUS: DEPLOYED
	
	RESOURCES:
	==> v1/Deployment
	NAME                             READY  UP-TO-DATE  AVAILABLE  AGE
	mottled-quetzal-jaeger-operator  0/1    1           0          1s
	
	==> v1/Pod(related)
	NAME                                              READY  STATUS             RESTARTS  AGE
	mottled-quetzal-jaeger-operator-7b9cdd8d55-frc2l  0/1    ContainerCreating  0         1s
	
	==> v1/ServiceAccount
	NAME                             SECRETS  AGE
	mottled-quetzal-jaeger-operator  1        1s
	
	==> v1beta1/Role
	NAME                             AGE
	mottled-quetzal-jaeger-operator  1s
	
	==> v1beta1/RoleBinding
	NAME                             AGE
	mottled-quetzal-jaeger-operator  1s
	
	
	NOTES:
	jaeger-operator is installed.
	
	
	Check the jaeger-operator logs
	  export POD=$(kubectl get pods-l app.kubernetes.io/instance=mottled-quetzal -lapp.kubernetes.io/name=jaeger-operator --namespace default --output name)
	  kubectl logs $POD --namespace=default
	
	
	
	(venv) [seaTrials]$
