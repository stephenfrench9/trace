## deploy elasticsearch 
	
	(awsenv) [jaeger]$ kubectl get roles
	No resources found.
	(awsenv) [jaeger]$ kubectl get ns
	NAME          STATUS   AGE
	default       Active   15m
	kube-public   Active   15m
	kube-system   Active   15m
	(awsenv) [jaeger]$ kubectl get nodes
	NAME                                          STATUS   ROLES    AGE   VERSION
	ip-172-20-32-207.us-west-2.compute.internal   Ready    node     14m   v1.11.9
	ip-172-20-34-60.us-west-2.compute.internal    Ready    master   15m   v1.11.9
	ip-172-20-62-97.us-west-2.compute.internal    Ready    node     13m   v1.11.9
	(awsenv) [jaeger]$ kubectl get services
	NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
	kubernetes   ClusterIP   100.64.0.1   <none>        443/TCP   16m
	(awsenv) [jaeger]$ kubectl get deployments
	No resources found.
	(awsenv) [jaeger]$ kubectl apply -f 
	.greenfield.sh                    getjaeger.sh                      operator.yaml                     simple-prod-with-volumes.yaml
	.line.txt                         getyamls.sh                       role.yaml                         simple-prod.yaml
	commands.sh                       jaegertracing_v1_jaeger_crd.yaml  role_binding.yaml                 simplest.yaml
	commands1.sh                      line.txt                          service_account.yaml              with-cassandra.yaml
	elasticsearch.yml                 mega                              simple-prod-deploy-es.yaml        
	(awsenv) [jaeger]$ kubectl apply -f elasticsearch.yml 
	statefulset.apps/elasticsearch created
	service/elasticsearch created
	(awsenv) [jaeger]$ kubectl get deployments
	No resources found.
	(awsenv) [jaeger]$ kubectl get services
	NAME            TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)             AGE
	elasticsearch   ClusterIP   None         <none>        9200/TCP,9300/TCP   15s
	kubernetes      ClusterIP   100.64.0.1   <none>        443/TCP             16m
	(awsenv) [jaeger]$ kubectl get pods
	NAME              READY   STATUS    RESTARTS   AGE
	elasticsearch-0   1/1     Running   0          45s
	(awsenv) [jaeger]$ kubectl get statefulsets
	NAME            DESIRED   CURRENT   AGE
	elasticsearch   1         1         1m
	(awsenv) [jaeger]$ 

## Deploy Elastisearch and then deploy a Jaeger

	(awsenv) [jaeger]$ kubectl apply -f elasticsearch.yml 
	statefulset.apps/elasticsearch created
	service/elasticsearch created
	(awsenv) [jaeger]$ kubectl get nodes
	NAME                                          STATUS   ROLES    AGE   VERSION
	ip-172-20-32-109.us-west-2.compute.internal   Ready    node     4h    v1.11.9
	ip-172-20-33-180.us-west-2.compute.internal   Ready    master   4h    v1.11.9
	ip-172-20-35-129.us-west-2.compute.internal   Ready    node     4h    v1.11.9
	(awsenv) [jaeger]$ kubectl get pods
	NAME              READY   STATUS              RESTARTS   AGE
	elasticsearch-0   0/1     ContainerCreating   0          11s
	(awsenv) [jaeger]$ ls
	commands.sh				jaegertracing_v1_jaeger_crd.yaml	role_binding.yaml			simplest.yaml
	commands1.sh				line.txt				service_account.yaml			with-cassandra.yaml
	elasticsearch.yml			mega					simple-prod-deploy-es.yaml
	getjaeger.sh				operator.yaml				simple-prod-with-volumes.yaml
	getyamls.sh				role.yaml				simple-prod.yaml
	(awsenv) [jaeger]$ kubectl get pods
	NAME              READY   STATUS    RESTARTS   AGE
	elasticsearch-0   1/1     Running   0          1m
	(awsenv) [jaeger]$ kubectl get jaegers
	No resources found.
	(awsenv) [jaeger]$ kubectl apply -f simple-prod.yaml
	jaeger.jaegertracing.io/simple-prod created
	(awsenv) [jaeger]$ kubectl get jaegers
	NAME          AGE
	simple-prod   8s
	(awsenv) [jaeger]$ kubectl get pods
	NAME                                     READY   STATUS    RESTARTS   AGE
	elasticsearch-0                          1/1     Running   0          10m
	simple-prod-collector-8444687ff8-x7mjf   1/1     Running   0          7m
	simple-prod-query-58bf4f6b74-b2rvx       2/2     Running   0          7m
	(awsenv) [jaeger]$ kubectl get services
	NAME                             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                  AGE
	elasticsearch                    ClusterIP   None             <none>        9200/TCP,9300/TCP                        10m
	kubernetes                       ClusterIP   100.64.0.1       <none>        443/TCP                                  4h
	simple-prod-collector            ClusterIP   100.70.164.29    <none>        9411/TCP,14250/TCP,14267/TCP,14268/TCP   7m
	simple-prod-collector-headless   ClusterIP   None             <none>        9411/TCP,14250/TCP,14267/TCP,14268/TCP   7m
	simple-prod-query                ClusterIP   100.71.247.154   <none>        16686/TCP                                7m
	(awsenv) [jaeger]$ kubectl get jaegers
	NAME          AGE
	simple-prod   7m
