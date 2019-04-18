# Distributed Tracing Can Solve Your Problems

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

# Instructions to Start 

`sh trace/sweat/deploy/commands.sh`

`kubectl get services`

Let the load balancer load for 5 minutes before you try to visit any of the ip addresses.

`sh trace/jaeger/commands.sh`

`sh trace/jaeger/commands1.sh`

commands1.sh will open up the yaml for the jaeger service. Navigate to the service type and make it a load balancer.







