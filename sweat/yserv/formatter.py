import requests
from flask import Flask
from flask import request
from lib.tracing import init_tracer
from opentracing.ext import tags
from opentracing.propagation import Format


from time import sleep



app = Flask(__name__)
tracer = init_tracer('model')

def http_get(port, path, param, value, bug):
    url = 'http://app-zserv:%s/%s' % (port, path)

    span = tracer.active_span
    span.set_tag(tags.HTTP_METHOD, 'GET')
    span.set_tag(tags.HTTP_URL, url)
    span.set_tag(tags.SPAN_KIND, tags.SPAN_KIND_RPC_CLIENT)
    headers = {}
    tracer.inject(span, Format.HTTP_HEADERS, headers)

    r = requests.get(url, params={param: value, 'bug': bug}, headers=headers, timeout=1)
    assert r.status_code == 200
    return r.text

@app.route("/format")
def format():
    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_active_span('request', child_of=span_ctx, tags=span_tags) as scope:
        scope.span.log_kv({'event': 'yserv-server', 'value': 'line 32'})
        hello_to = request.args.get('helloTo')
        bug = request.args.get('bug')
    # fool
        scope.span.log_kv({'event': 'yserv-got bug', 'value': bug})
        scope.span.log_kv({'event': 'yserv-got bug', 'value': str(type(bug))})
        if bug == "True":
            bug = True
        elif bug == "False":
            bug = False
        scope.span.log_kv({'event': 'processed bug', 'taIp': str(type(bug))})
        scope.span.log_kv({'event': 'processed bug', 'value': str(type(bug))})

        if bug:
            scope.span.log_kv({'event': 'bug going', 'value': str(bug)})
            sleep(.05)



    # fool
        scope.span.log_kv({'event': 'yserv', 'bug status': str(bug)})
        hello_to = hello_to + ', model'
        scope.span.log_kv({'event': 'yserv-server', 'value': 'line 36'})
        try:
            scope.span.log_kv({'event': 'yserv-server', 'value': 'line 35'})
            hello_str = http_get(5000, 'format', 'helloTo', hello_to, bug)
            scope.span.log_kv({'event': 'yserv-server', 'value': 'line 40'})
        except:
            hello_str = hello_to

        return hello_str # two submissions to format servers


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

