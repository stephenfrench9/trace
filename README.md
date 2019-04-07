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

### paths forward 1

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

## Checkpoint March 28 2019

### Local Jaeger
- Launch dockerized jaeger locally. Use jaegertracing/all-in-one:1.10.
- Turn on my jaeger enabled server locally. solution/formatter.py. (adapted from g.opentracing/lesson03/)
- jaeger sees the server traces
- containerized server functions correctly, but doesn't ship traces to jaeger client

### Kubernetes Jaeger
- install jaeger with a kubernetes operator. (g.jaegertracing/jaeger-operator). Manually start a jaeger agent. Manually add a a public IP. Visit \<ext ip\>:16686, it works
- Turn on my jaeger-enabled server container on, wrapped in a deployment attached to a service. Visit it at \<ext ip\>:5000 and \<ext ip\>:5000/format?helloTo=bryn

### Helm
- do the same thing with Helm.


### pathes forward

### microservices from scratch, in python. Jaeger backend native to K8s.  
 1. Jaeger loses the app when it goes into the container. Expose more ports on my server container? Get this working locally, and then do the same to the container in the cloud.
 2. Read about jaeger. jaegertracing/jaeger, jaegertracing/jaeger-operator, jaegertracing/jaeger-kubernetes, jaegertracing/jaeger-operator.
 3. Probably need to learn stuff like: The jaeger operator allows you to make jaeger objects in kubernetes. 
 3. Read about jaeger. Jaeger website.
 4. Read about jaeger. helm/charts.
 5. read about jaeger. Blogs


- this is what I am developing right now. 

## Checkpoint Wednesday April 3 2019
- Summary: I can deploy chained microservices to the cloud as independent services and trace them with jaeger. Next step: make deployment and modification of microservices easier (they should all have their own github repo).
- I can have services in kubernetes talk to each other. When you have a kubernetes service, then http://\<service-name\> is a valid ip address that other services or servers can query. I hard bake the service name into the code base for the server that will use that service. So I need to coordinate service names between server code bases and the .yamls which actually create a service. 
- I can create docker images, tag them, and put them in dockerhub. Then I can create deployments which use these docker images. Jaeger traces them.
- I really had a hard time discovering how to connect services in kubernetes. I was trying to write conf files following ktask/connect-a-front-end-to , but that conf file was actually nginx specific. I was trying things and everything I tried was taking a while. I was following a tutorial that I shouldn't have been following.

### pathes forward

1. jenkins deployed microservices, jenkins updated microservices 
2. large chain of microservices
3. flask fronted to call the chain (can add last)
4. jaeger automatically sends email. Jaeger email notification.

## Checkpoint Friday April 5rd
- Summary: I can modify my microservice application really easily. I can build a new image, push to dockerhub, and then go to kubectl and knock down a service and bring a new one up pretty easily. The workflow is this:

	1. pycharm: edit server code (ie. aserv/formatter.py)
	2. pycharm: edit yaml, maybe. The tag on the image. (ie. deploy/aserv.yaml)
	3. Terminal:

			cd sweat/aserv (i.e.)
			docker build -t whatever .
			docker tag whatever stephenfrench9/aserv
			docker push stephenfrench9/aserv
			cd deploy
			kubectl delete -f aserv.yaml
			kubectl apply -f aserv.yaml
			
Hopefully, you won't mess with the tag on the image. And hopefully, the name of services will not change, so you can reach them from your server code. 

Jaeger goes up with trace/jaeger. It requires a little specialized knowledge and I manually edit the service yaml so its publicly accessible. 

Of course, hooligan/launch_cluster (not in this repo) puts up the cluster on configures kubernetes/kubectl with a shell scripts. 

I need to answer the question: How can distributed tracing deliver value to an organization or software product.

### Pathes forward 

Its been a while since I wrote any code or added any capabilities to the repo. I have been smoothing over my workflows (though they are still opaque to others). I have also been reading about distributed tracing and attending meetups. An engineer from 'smartsheets' told me about a problem that distributed tracing helps them solve. They often run into a problem when a customer asks for an expensive calculation in one of their 'sheets'. The service performing the calcuation with fail, and smartsheets finds in helpful to know which request caused the service to fail. Distributed tracing allows them to associate the job their service is running (deep in their system) with the user that generated this request, and they can then get ahold of the customer that caused this problem and solve some things. 

Distributed tracing is not just about reducing latency of the application, but identifying which traces are really the problem causers. 

'there are alot of things unique to this particular trace' - the smartsheets engineer. 

This particular service is failing alot - what is causing it? Lets look at all the failing traces that run through the application, and lets ask, is it a particular user that is causing this? Is it a particular upstream service that is causing this problem? 

1. Build an architecture where a service fails, and you need to find which service is failing. Pick some reasonable looking architecture to work with. maybe a couple domains and a couple layers. 
2. Change it so that traces pick up bugs, and they cause a problem downstream. Analyze with distributed tracing.
3. Discover this problem with analyzing large flows of traffic. 

### Frame the work

###### Discovering Bottlenecks in microservice applicaitons
I have a frontend that 

I have a front end that makes like 20 requests to a more sophisticated archtectue. I do it, analyze statistics. Eventually one service breaks, I go find it. 


###### Lightweight logging with jaeger contexts: taking jaeger apart. 
Can I create a debugging scheme that allows users to view all the logs corresponding to one trace, but not use the full jaeger frontend. Possibly there is some advantage to doing this in a more lightweight fashion. 

###### Sandbox for learning how to use jaeger: ship your first trace.

###### Discovering bottenecks caused by upstream services: a case study of smart sheets

### Frontend

Makes 10000 calls to the microservice, presents averages. I search for the slowest one in jaeger, look at that trace.

## Attempts

##### trace/jaegerHi
- Launch jaeger-all-in-one container on my local machine
- hello world stuff from the jaeger website

##### trace/jkub (following jaeger/jaeger-kubernetes)

- hot-rod.sh uses kubectl to deploy hot-rod in kubernetes. It is unresponsive
- commands.sh launches a bunch of different things many different ways. Among the launched entities are the jaeger-collector, jaeger-query, and jaeger-agent. It should deploy hot-rod but I do not see hot-rod anywhere. 
	- jaeger-all-in-one-template.yml should deploy hot-rod as well as jaeger, but I only see one jaeger agent. 
	- jaeger-query is successfully launched
	- jaeger-all-in-one is never launched.

##### trace/managing-resources - launch hot-rod into kubernetes (following k8s tutorial: managing-resources.)

-  nginx-app.yaml was modified. 
	-  Placed the jaeger-all-in-one image into the deployment, modified the ports of the service, the ports of the deployment, and the env variables of the deployment spec to match the command line arguments for launching this container with docker. The image pull successful and starts, but then throws some sort of error and backs of. 

##### trace/seaTrials (https://blog.thecodeteam.com/2017/10/09/easy-way-hard-way-jaeger-kubernetes-cncf/)
- put production jaeger into kubernetes
- Fix up the tiller deployment in kubernetes. 
- https://github.com/helm/helm
- commands.sh patches the tiller deployment as well as creating a service account on kubernetes.

##### trace/openTracingLesson (https://github.com/yurishkuro/opentracing-tutorial/tree/master/python)
- Build shark and tootles. These are dockerized, jaeger enabled flask apps. 
- deploy python webservers locally. Trace them with jaeger. Specifically openTracingLesson/lesson03/solution/*.py are webservers imbued with jaeger matter.
- openTracingLesson/lesson03/* is a mess. But this is where I build shark and tootles. Docker images that fun the formatter.py server. They run on 0.0.0.0:5000 which is very different than 127.0.0.1:5000. 

##### trace/server
- put jaeger-imbued dockerized flaskservers up in the cloud
- run commands.sh, and you are done
- formatter.yaml is a deployment with the formatter server at 0.0.0.0:5000
- formatter.yaml was derived from a yaml called nginx.yaml, which is from managing-resources tutorial. nginx.yaml is just a service backed by an nginx-pod. except now it is backed by my image. The shark image.

##### trace/jaeger [https://github.com/jaegertracing/jaeger-operator]
- put jaeger up in the cloud
- run commands.sh, one at a time, with your "o" and "n" scripts

##### trace/sweat
- build a docker image
- python webserver, exact copy of tutorial webserver.
- deploy webserver with trace/sweat/deploy/commands.sh and adjacent .yaml files

##### trace/jenkinsServer
- put jenkins server in the cloud
- jenkinsServer/kubernetes-operator must be executed first.
- then execute jenkinsServer

##### trace/localJenk
- throw up a local jenkins server

##### rtrace/jenkins-sand
- This has a github account attached to it. 
- trying to clone this repo onto the cluster (the github account associated with it)

# Debugging services running in kubernetes
To see the logs for a container

	kubectl logs -f <podname> <containername>
	
To see the source code for a running server

	kubectl exec $pod -c ape-aserv -- cat formatter.py
	


# Development environment for containers

# Appendix

## Possible sticking points.

I have never worked with jaeger and I don't know how to plug it into an app. I have no idea how jaeger works. 
pppp
I don't know much about computer networks, I will need to write webservers which can send a request to another webserver on the kubernetes network. I think I can write a service which will forward requests published on one of its ports to another service, so that in my source code I can write something like:

	http.sendrequest(r1, 80)
	
And it will arrive where it needs to be.

## proposed directories

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








