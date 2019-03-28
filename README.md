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

### Find examples already deployed to kubernetes

1. Deploy Jaeger to kubernetes with jaeger/kubernetes (of the jaeger project).
2. Deploy Hot-Rod to kubernetes. 
3. Track Hot-Rod with kubernetes.
4. Modify source code for hot rod so I have my dummy services.

### Write my own application from scratch. Deploy jaeger backend.

## Attempts

##### trace/jkub (following jaeger/jaeger-kubernetes)

- hot-rod.sh uses kubectl to deploy hot-rod in kubernetes. It is unresponsive
- commands.sh launches a bunch of different things many different ways. Among the launched entities are the jaeger-collector, jaeger-query, and jaeger-agent. It should deploy hot-rod but I do not see hot-rod anywhere. 
	- jaeger-all-in-one-template.yml should deploy hot-rod as well as jaeger, but I only see one jaeger agent. 
	- jaeger-query is successfully launched
	- jaeger-all-in-one is never launched.

##### trace/managing-resources - launch hot-rod into kubernetes (following k8s tutorial: managing-resources.)

-  nginx-app.yaml was modified. 
	-  Placed the jaeger-all-in-one image into the deployment, modified the ports of the service, the ports of the deployment, and the env variables of the deployment spec to match the command line arguments for launching this container with docker. The image pull successful and starts, but then throws some sort of error and backs of. 

##### trace/hotrod (jaeger/examples/hotrod)

- not done in kubernetes. 
- Launch hot-rod and jaeger backend in docker containers.

##### trace/medium (https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941)

- not done in kubernetes
- from 2017
- same as the video, but with commands
- explanation of jaeger/examples/hotrod

##### trace/openshift - (openshift commons https://www.youtube.com/watch?v=fjYAU3jayVo)
- Not done in kubernetes
- Can't see the start of the command line in the video.
- runs hot rod as well as the standard jaeger.
- same as trace/medium

##### trace/seaTrials (https://blog.thecodeteam.com/2017/10/09/easy-way-hard-way-jaeger-kubernetes-cncf/)
- put production jaeger into kubernetes
- Fix up the tiller deployment in kubernetes. 
- https://github.com/helm/helm
- commands.sh patches the tiller deployment as well as creating a service account on kubernetes.

##### trace/openTracingLesson (https://github.com/yurishkuro/opentracing-tutorial/tree/master/python)
- deploy python webservers locally. Trace them with jaeger. Specifically openTracingLesson/lesson03/solution/*.py are webservers imbued with jaeger matter.
- openTracingLesson/lesson03/* is a mess. But this is where I build shark and tootles. Docker images that fun the formatter.py server. They run on 0.0.0.0:5000 which is very different than 127.0.0.1:5000. 

##### trace/upper
- put servers up in the cloud
- formatter.yaml is a deployment with the formatter server at 0.0.0.0:5000
- nginx-yaml is from managing-resources. Its just a service backed by an nginx-pod. except now it is backed by my image. The shark image.

## Possible sticking points.

I have never worked with jaeger and I don't know how to plug it into an app. I have no idea how jaeger works. 
pppp
I don't know much about computer networks, I will need to write webservers which can send a request to another webserver on the kubernetes network. I think I can write a service which will forward requests published on one of its ports to another service, so that in my source code I can write something like:

	http.sendrequest(r1, 80)
	
And it will arrive where it needs to be.	 








