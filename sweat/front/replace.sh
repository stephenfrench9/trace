nameroot=$1
export pod=$(kubectl get pods | grep $nameroot | awk '{print $1}')
echo $pod
kubectl delete pod $pod
