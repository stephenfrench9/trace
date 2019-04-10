export pod=$(kubectl get pods | grep web | awk '{print $1}')
echo $pod
kubectl delete pod $pod
