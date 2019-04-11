docker build -t stephenfrench9/yserv:prod yserv
docker push stephenfrench9/yserv:prod
export pod=$(kubectl get pods | grep yserv | awk '{print $1}')
echo $pod
kubectl delete pod $pod
