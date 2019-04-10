export pod=$(kubectl get pods | grep api | awk '{print $1}')
echo $pod
kubectl delete pod $pod
