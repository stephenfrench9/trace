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

## Possible paths forward

### jaeger-all-in-one and Hot-Rod (docker images) on Kubernetes 

This plan involves launching two docker images from the jaeger tutorials just on kubernetes.

0. Launch a Kubernetes deployment with publicly exposed front-end from one of the kubernetes tutorials.
1. Deploy jaeger's helloworld all-in-one docker image, as well as a sample app that it successfully traces, called hot-rod. These images will be substituted in for the image in the tutorial. I will publish the frontend servers for the hot rod app and jaeger to the public internet, and visit those pages.
2. Get into the source code for the hot rod app, and try to break it into different containers. (Right now it is only one container). As I do this, I will keep Jaeger "plugged" into it. 
3. Get into the source code for the jaeger container, try to break it into containers. Maintain the monitoring of the other app.
4. Modify the hot-rod app services, as well as replicate them, to build my microservice archtecture. 

### use the jaeger-kubernetes/ portion of the jaeger project rather than the jaeger all in one image. (thanks Curtis)

1. Deploy Jaeger to kubernetes with jaeger/kubernetes (of the jaeger project).
2. Deploy Hot-Rod to kubernetes. 
3. Track Hot-Rod with kubernetes.
4. Modify source code for hot rod so I have my dummy services.

##### trace/jkub

- The trace/jkub/ deploys jaeger into Kubernetes. trace/jkub/hot-rod.sh deploys the Hot Rod app into kubernetes. But The app is not functional, nor is it tied to jaeger. Next step: Do a better job of deploying the app? Write a deployment yaml for it? Steal a deployment yaml from the kubernetes tutorials, probably exposing-an-external or managing-services.

##### trace/managing-resources - launch hot-rod into kubernetes

-  Stole a deployment script from trace/managing-resources. Placed the jaeger-all-in-one image into the deployment, modified the ports of the service, the ports of the deployment, and the env variables of the deployment spec to match the command line arguments for launching this container with docker. The image pull successful and starts, but then throws some sort of error and backs of. 


## Possible sticking points.

I have never worked with jaeger and I don't know how to plug it into an app. I have no idea how jaeger works. 

I don't know much about computer networks, I will need to write webservers which can send a request to another webserver on the kubernetes network. I think I can write a service which will forward requests published on one of its ports to another service, so that in my source code I can write something like:

	http.sendrequest(r1, 80)
	
And it will arrive where it needs to be.	 








