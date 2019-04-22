# Distributed Tracing Can Solve Your Problems

## Intro 
Microservice applications can be difficult to debug. This repo builds and deploys a microservice application to a kubernetes cluster. The application suffers from a bug which is difficult to diagnose with conventional logging methods, but is trivial to resolve with Distributed Tracing. The application is instrumented, and traces can be viewed in the jaeger fronted. 

This code base is not meant to be run by the general public, because access to my dockerhub account is required. If you want to build and run this app, it is possible but will take some work. The instructions are below. 

Visit my blog at https://medium.com/debugging-distributed-applications/debugging-distributed-applications-b6856122727e to learn more. 

## Directories

### app/
- contains .yamls for all the services that run on kubernetes as part of this application
- contains scripts to deploy those .yamls
- contains source code to generate docker images for those services

### archive/
- old directories and log of attempts

### awsenv/ 
- python virtual environment

### jaeger/
- launch jaeger into kubernetes

### launch/
- start up a cluster, initialized with kubernetes

### sweat/
- launch my application

## Instructions to Build and Run 

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












