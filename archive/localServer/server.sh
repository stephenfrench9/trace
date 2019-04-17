docker run --rm  \
       --link jaeger \
       -p 8080-8083:8080-8083 \
       -p 5000:5000 \
       -e JAEGER_AGENT_HOST="jaeger" \
       stephenfrench9/shark:1.0
