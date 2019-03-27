FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install flask
RUN pip install opentracing
RUN pip install jaeger_client

LABEL maintainer="Stephen"
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["formatter.py"]
