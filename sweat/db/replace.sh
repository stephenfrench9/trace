export pod=$(kubectl get pods | grep database | awk '{print $1}')
echo $pod
kubectl delete pod $pod
