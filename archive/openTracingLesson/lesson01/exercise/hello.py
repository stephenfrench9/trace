import sys
import time

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


def say_hello(hello_to, tracer):
    with tracer.start_span('say-hello') as span:
        hello_str = 'Hello, %s!' % hello_to
        span.log_kv({"event": "format", "value": hello_str})
        span.set_tag("name", hello_str)
        print(hello_str)
        span.log_kv({"event": "println"})


assert len(sys.argv) == 2
tracer = init_tracer('hello-world-3')
hello_to = sys.argv[1]

say_hello(hello_to, tracer)

time.sleep(2)
tracer.close()
