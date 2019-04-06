import requests
from flask import Flask
from flask import request
from lib.tracing import init_tracer
from opentracing.ext import tags
from opentracing.propagation import Format

import time

app = Flask(__name__)
tracer = init_tracer('yserv')

def http_get(port, path, param, value):
    url = 'http://app-zserv:%s/%s' % (port, path)

    span = tracer.active_span
    span.set_tag(tags.HTTP_METHOD, 'GET')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)

    r = requests.get(url, params={param: value}, headers=headers)
    assert r.status_code == 200
    return r.text

@app.route("/format")
def format():
    print("can't print")
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_active_span('request', child_of=span_ctx, tags=span_tags) as scope:
        scope.span.log_kv({'event': 'yserv-server', 'value': 'line 32'})
        hello_to = request.args.get('helloTo')
        hello_to = 'Hello, %s!' % hello_to
        hello_str = 'yserv initialized'
        scope.span.log_kv({'event': 'yserv-server', 'value': 'line 36'})
        try:
            scope.span.log_kv({'event': 'yserv-server', 'value': 'line 35'})
            hello_str = http_get(5000, 'format', 'helloTo', hello_to)
            scope.span.log_kv({'event': 'yserv-server', 'value': 'line 40'})
        except:
            print("The get request failed")

        return hello_str # two submissions to format servers


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

