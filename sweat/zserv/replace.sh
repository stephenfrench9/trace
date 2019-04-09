export pod=$(kubectl get pods | grep zserv | awk '{print $1}')
echo $pod
kubectl delete pod $pod
