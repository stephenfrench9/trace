kubectl apply -f deploy/crds/jenkinsio_v1alpha1_jenkins_crd.yaml
kubectl apply -f deploy/service_account.yaml
kubectl apply -f deploy/role.yaml
kubectl apply -f deploy/role_binding.yaml
kubectl apply -f deploy/operator.yaml
kubectl get pods -w
