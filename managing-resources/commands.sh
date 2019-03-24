kubectl create -f nginx-app.yaml
# kubectl create also accepts multiple -f arguments:
# kubectl create -f https://k8s.io/examples/application/nginx/nginx-svc.yaml -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
# kubectl create -f https://k8s.io/examples/application/nginx/
# kubectl will read any files with suffixes .yaml, .yml, or .json. # 
# kubectl create -f https://raw.githubusercontent.com/kubernetes/website/master/content/en/examples/application/nginx/nginx-deployment.yaml
kubectl delete -f https://k8s.io/examples/application/nginx-app.yaml
kubectl delete deployments/my-nginx services/my-nginx-svc
kubectl delete deployment,services -l app=nginx
kubectl get $(kubectl create -f docs/concepts/cluster-administration/nginx/ -o name | grep service)
kubectl create -f project/k8s/development
kubectl create -f project/k8s/development --recursive
kubectl create -f project/k8s/namespaces -f project/k8s/development --recursive
kubectl create -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
kubectl get pods -Lapp -Ltier -Lrole
kubectl get pods -lapp=guestbook,role=slave
kubectl label pods -l app=nginx tier=fe
kubectl get pods -l app=nginx -L tier
kubectl annotate pods my-nginx-v4-9gw19 description='my frontend running nginx'
kubectl get pods my-nginx-v4-9gw19 -o yaml
kubectl scale deployment/my-nginx --replicas=1
kubectl get pods -l app=nginx
kubectl autoscale deployment/my-nginx --min=1 --max=3
kubectl apply
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
kubectl edit
kubectl edit deployment/my-nginx
kubectl get deployment my-nginx -o yaml > /tmp/nginx.yaml
kubectl apply -f /tmp/nginx.yaml
kubectl patch
kubectl replace -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml --force
kubectl run my-nginx --image=nginx:1.7.9 --replicas=3
kubectl edit deployment/my-nginx
