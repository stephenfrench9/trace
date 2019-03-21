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

### Jaeger and Hot-Rod on Kubernetes 

0. Launch a Kubernetes deployment with publicly exposed front-end from one of the kubernetes tutorials.

1. Deploy jaeger's helloworld all-in-one docker image, as well as a sample app that it successfully traces, called hot-rod. These images will be substituted in for the image in the tutorial. I will publish the frontend servers for the hot rod app and jaeger to the public internet, and visit those pages.

2. Get into the source code for the hot rod app, and try to break it into different containers. (Right now it is only one container). As I do this, I will keep Jaeger "plugged" into it. 

3. Get into the source code for the jaeger container, try to break it into containers. Maintain the monitoring of the other app.

4. Modify the hot-rod app services, as well as replicate them, to build my microservice archtecture. 

### Another way

I should probably think of this. 

## Possible sticking points.

I have never worked with jaeger and I don't know how to plug it into an app. I have no idea how jaeger works. 

I don't know much about computer networks, I will need to write webservers which can send a request to another webserver on the kubernetes network. I think I can write a service which will forward requests published on one of its ports to another service, so that in my source code I can write something like:

	http.sendrequest(r1, 80)
	
And it will arrive where it needs to be.	 








