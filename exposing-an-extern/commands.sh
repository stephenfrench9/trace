kubectl run hello-world --replicas=5 --labels="run=load-balancer-example" --image=gcr.io/google-samples/node-hello:1.0  --port=8080
kubectl get deployments hello-world
kubectl describe deployments hello-world
kubectl get replicasets
kubectl describe replicasets
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service
kubectl get services my-service
# I see a list of endpoints for the service.
kubectl describe services my-service
kubectl get pods --output=wide
# We have a deployment with an attached service. Visit it at http://ingress:8080
kubectl delete services my-service
kubectl delete deployment hello-world

# Is there something about the deployment that says, when you wrap this thing in a service, use these addresses or these containers as endpoints?

# The service accepts a request from the public internet and then it forwards it to one of its endpoints on the Port specified in the service.


# "hello kubernetes" is available publicly. Your service has a list of endpoints.

# A service proxying traffic to a bunch of containers that say hello world.
