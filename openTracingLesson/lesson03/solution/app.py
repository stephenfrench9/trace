from flask import Flask
from flask import request
# from lib.tracing import init_tracer
from opentracing.ext import tags
from opentracing.propagation import Format

import logging
from jaeger_client import Config


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

app = Flask(__name__)
tracer = init_tracer('formatter')

@app.route('/')
def hello_whale():
    return "Whale, Hello there!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
