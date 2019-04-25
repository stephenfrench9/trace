import requests
from flask import Flask
from flask import request
from lib.tracing import init_tracer
from time import sleep
from opentracing.ext import tags
from opentracing.propagation import Format
from random import randint
from elasticsearch import Elasticsearch

app = Flask(__name__)


def http_get(port, path, param, value):
    url = 'http://elasticsearch:%s/%s' % (port, path)

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
    # you can use RFC-1738 to specify the url
    url = 'http://elasticsearch:9200/_stats/indexing'
    r = requests.get(url, timeout=1)
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    # es = Elasticsearch(['https://user:secret@elasticsearch:443'])

    object = es

    object_methods = [method_name for method_name in dir(object)
                      if callable(getattr(object, method_name))]

    for index in es.indices.get('*'):
        app.logger.debug(index)

    app.logger.debug(str(type(es)))
    app.logger.debug(str(object_methods))
    app.logger.debug(str(es.info))
    app.logger.debug(" h ")
    app.logger.debug(str(es.count))
    app.logger.debug(r.text)


    return str(type(r)) + "somethin great, an expectation"
    # es = Elasticsearch(['http://elasticsearch:%s/%s'])
    #
    # # ... or specify common parameters as kwargs
    #
    # es = Elasticsearch(
    #     ['localhost', 'otherhost'],
    #     http_auth=('user', 'secret'),
    #     scheme="https",
    #     port=443,
    # )
    #
    # # SSL client authentication using client_cert and client_key
    #
    # from ssl import create_default_context
    #
    # context = create_default_context(cafile="path/to/cert.pem")
    # es = Elasticsearch(
    #     ['localhost', 'otherhost'],
    #     http_auth=('user', 'secret'),
    #     scheme="https",
    #     port=443,
    #     ssl_context=context,
    # )


if __name__ == "__main__":
    # app.run(port=8081)
    app.run(debug=True, host='0.0.0.0')
