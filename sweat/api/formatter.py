import requests
from flask import Flask
from flask import request
from lib.tracing import init_tracer
from opentracing.ext import tags
from opentracing.propagation import Format

import time

app = Flask(__name__)
tracer = init_tracer('api')

def http_get(port, path, param, value):
    url = 'http://app-aserv:%s/%s' % (port, path)

    span = tracer.active_span
    span.set_tag(tags.HTTP_METHOD, 'GET')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)

    r = requests.get(url, params={param: value}, headers=headers, timeout=1)
    assert r.status_code == 200
    return r.text

@app.route("/format")
def format():
    start = time.time()
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_active_span('request', child_of=span_ctx, tags=span_tags) as scope:
        hello_to = request.args.get('helloTo')
        scope.span.log_kv({'event': 'api recieves request', 'helloTo': hello_to})

        hello_to = 'Hello, %s!' % hello_to
        try:
            hello_str = http_get(5000, 'format', 'helloTo', hello_to)
            scope.span.log_kv({'event': 'aserv', 'value': 'line 35'})
        except:
            print("api: The get request failed. no further modification to the string")
            hello_str = hello_to

        end = time.time()
        lapse = round(end - start, 4)
        hello_str = hello_str
        return hello_str # two submissions to format servers


if __name__ == "__main__":
    print("Running the flask app for api:")
    app.run(debug=True, host='0.0.0.0')

