export pod=$(kubectl get pods | grep yserv | awk '{print $1}')
echo $pod
kubectl delete pod $pod
