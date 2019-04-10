export pod=$(kubectl get pods | grep aserv | awk '{print $1}')
echo $pod
kubectl delete pod $pod
