# BugFinder
#### Distributed Tracing can solve your problems

## Intro 
Microservice applications can be difficult to debug. A growing number of organizations combat this problem by instrumenting their applications with distributed tracing tools like 'Jaeger' or 'Zipkin'. Analyzing those traces can provide insight into why your application is running slowly, ultimately easing debugging pains. 

Typically, one pays money to a service like New Relic or RookOut to analyze those traces. BugFinder is a free alternative to those services. (BugFinder provides significantly less functionality. It can also be used as an easy-to-understand exercise that provides exposure to the analysis that these SaaS platforms provide.)

This repo does 3 main things:

1. Launches a Kubernetes cluster on AWS using Kops
2. Deploys a Jaeger-operator, Jaeger, and Elasticsearch to the K8s cluster
3. Launches a 6-microservice testbed application

The testbed application suffers from a bug which is difficult to diagnose with conventional logging methods, but is trivial to resolve with Distributed Tracing. The application is instrumented, and BugFinder locates the bug with ease.

This code base is not meant to be run by the general public, because access to my dockerhub account is required. If you want to build and run this app, it is possible but will take some work. The instructions are below. 

To learn about the bug that is baked into the application, visit my blog at https://medium.com/debugging-distributed-applications/debugging-distributed-applications-b6856122727e. 

## Directories

### archive/
- old directories.
- My journal of things I tried

### awsenv/ 
- python virtual environment

### jaeger/
- launch jaeger into kubernetes

### launch/
- start up a cluster, initialized with kubernetes

### sweat/
- launch my testbed application
- launch bugfinder
- contains .yamls for all the services that run on kubernetes as part of this application
- contains scripts to deploy those .yamls
- contains source code to generate docker images for those services

## Instructions to Build and Run 

#### The below instructions are currently in disrepair, check back later

launch the applications

`sh trace/sweat/deploy/commands.sh`

`kubectl get services`

launch jaeger

`sh trace/jaeger/commands.sh`

`sh trace/jaeger/commands1.sh`

commands1.sh will open up the yaml for the jaeger service. Navigate to the service type and make it a load balancer.

Edit sweat/dockeruser so that it contains only your username. (no extra spaces)

Make sure that you are logged into docker 

Update the images in Docker using 

`hub <image name>`

for example

`hub ios`

Then navigate to all of the .yamls in sweat/ and navigate to the image portion of the .yaml and change the name of the container in the container spec field. The field is 

`spec:template:spec:containers:image`

Also run

`kub <image name>`

to get kubernetes to pull this image down.












