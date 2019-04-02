kubectl apply -f hello.yaml
kubectl describe deployment hello
kubectl apply -f hello-service.yaml
kubectl apply -f frontend.yaml
kubectl get service frontend --watch
