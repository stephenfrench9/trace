from flask import Flask
from flask import request
from lib.tracing import init_tracer
from time import sleep
from opentracing.ext import tags
from opentracing.propagation import Format
from random import randint

app = Flask(__name__)
tracer = init_tracer('zserv')


@app.route("/check")
def check():
    return str(slow)


@app.route("/format")
def format():
    global slow
    if randint(1, 5) == 5:
        slow = True

    span_ctx = tracer.extract(Format.HTTP_HEADERS, request.headers)
    span_tags = {tags.SPAN_KIND: tags.SPAN_KIND_RPC_SERVER}
    with tracer.start_active_span('end-chain', child_of=span_ctx, tags=span_tags) as scope:
        scope.span.log_kv({'event': 'zserv starts', 'slow': str(slow)})
        if (slow):
            print("The server is slow")
            sleep(.1)
            print("done sleeping")
        else:
            print("the server is fast")
        hello_to = request.args.get('helloTo')
        scope.span.log_kv({'event': 'one-server', 'value': 'line 16'})
        return 'Hello, %s!' % hello_to

if __name__ == "__main__":
    # app.run(port=8081)
    slow = False
    app.run(debug=True, host='0.0.0.0')