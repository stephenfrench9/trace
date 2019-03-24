#!/usr/bin/env bash
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-kubernetes/master/all-in-one/jaeger-all-in-one-template.yml 
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-kubernetes/master/production-elasticsearch/configmap.yml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-kubernetes/master/production-elasticsearch/elasticsearch.yml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-kubernetes/master/jaeger-production-template.yml
