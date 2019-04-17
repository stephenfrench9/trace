docker run --rm -it \
       --link jaeger \
       -p8080-8083:8080-8083 \
       -e JAEGER_AGENT_HOST="jaeger" \
       jaegertracing/example-hotrod:1.10 \
       all
