export pod=$(kubectl get pods | grep front | awk '{print $1}')
echo $pod
kubectl delete pod $pod
