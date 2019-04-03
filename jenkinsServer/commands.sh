kubectl apply -f jank.yaml
kubectl get secret jenkins-operator-credentials-example -o 'jsonpath={.data.user}' | base64 -D
kubectl get secret jenkins-operator-credentials-example -o 'jsonpath={.data.password}' | base64 -D
kubectl describe svc jenkins-operator-http-example
/usr/bin/open -a "/Applications/Google Chrome.app" 'http://google.com/'
kubectl port-forward jenkins-operator-example 8080:8080
