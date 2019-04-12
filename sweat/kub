service=$1
export pod=$(kubectl get pods | grep $service | awk '{print $1}')
echo $pod
kubectl delete pod $pod
