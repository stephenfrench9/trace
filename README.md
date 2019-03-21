# Trace

### Abstract

A dummy microservice consisting of 3 layers of 30 services will be deployed to kubernetes. A frontend will offer 30 buttons. Upon clicking one button, a request will be sent to one of the services in the 0 layer. The service will "sleep" for some number of milliseconds, and then it will forward the request to the 1 layer. This service will then sleep, and forward to the final layer, which will sleep and then return a hello world message to the to the frontend.

A bottleneck will be modeled by hiding one long sleep time with-in the microservice. I will then use (Jaeger or LightStep) to find that bottleneck.


## Final Product:

### Provisioning, deployment of Kubernetes
Kops

### Configuartion
Not needed. Everything will be containerized. 

### Deployment of Kubernetes pods
A shell script will run on my local machine to deploy kubernete's "Deployments" and "Services". 

### Deployments
There will be ~95 deployments. 90 will comprise my dummy microservice application. They will be named: 

 - dummy\<layer\>\<service-number\> layer is 0,1,or 2 and service-number is 0-29

4 will comprise my distributed tracing cluster, they will be named:

- jaegerCollector
- jaegerAgent
- jaegerQuery
- jaegerAggregator

(or the equivalent for LightStep). 1 will comprimise my frontend, it will be named:

- frontend





