#!/bin/bash
service=$1

docker build -t stephenfrench9/$service:prod $service
docker push stephenfrench9/$service:prod