import requests
from flask import Flask
from flask import request
from lib.tracing import init_tracer
from time import sleep
from opentracing.ext import tags
from opentracing.propagation import Format
from random import randint
from elasticsearch import Elasticsearch
import pprint

app = Flask(__name__)


def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item


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
    # url = 'http://elasticsearch:9200/_stats/indexing'
    # r = requests.get(url, timeout=1)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    size = 1000
    threshold = 10000
    # # es = Elasticsearch(['https://user:secret@elasticsearch:443'])
    #
    # object = es
    #
    # object_methods = [method_name for method_name in dir(object)
    #                   if callable(getattr(object, method_name))]
    #
    print("***************************Indices****************************")
    for index in es.indices.get('*'):
        print(index)
    print("\n\n\n\n")
    pp = pprint.PrettyPrinter(indent=0)
    res = es.search(index='jaeger-span-2019-04-26', size = size)

    # pp.pprint(res)
    print("***************************Elasticsearch Query****************************")
    a = res['hits']['hits']
    print("Number of hits: %d" % len(a))
    pp.pprint(a[0])
    print("\nStats\n")

    print("***************************Processed Query****************************")
    services = []
    traces = []
    spans = []
    for trace in a:
        service = trace['_source']['process']['serviceName']
        traceID = trace['_source']['traceID']
        spanID = trace['_source']['spanID']
        if service not in services:
            services.append(service)
        if traceID not in traces:
            traces.append(traceID)
        if spanID not in spans:
            spans.append(spanID)

        if (traceID == spanID):
            print("these are the same")

    print("num services: %d" % len(services))
    print("num traces: %d" % len(traces))
    print("num spans: %d" % len(spans))

    print(spans)
    print(traces)

    print("***************************Search By Span****************************")

    # build events dictionary
    events = {}
    for i in range(len(traces)):
        search = {"query": {"match": {'traceID': traces[i]}}}
        res = es.search(index='jaeger-span-2019-04-26', body=search, size = size)
        a = res['hits']['hits']  # all the spans to do with this trace

        for trace in a:
            service = trace['_source']['process']['serviceName']
            traceID = trace['_source']['traceID']
            spanID = trace['_source']['spanID']
            duration = trace['_source']['duration']
            if traceID not in events.keys():
                events[traceID] = {}
            events[traceID][service] = duration

    # total number of events
    events_num = len(events)

    # identify slow traces
    for trace in events.keys():
        slow = False
        for service in events[trace].keys():
            if events[trace][service] > threshold:
                slow = True
        events[trace]['slow'] = slow

    # see all the trace dictionaries
    for trace in events.keys():
        print(events[trace])

    # trim the events dictionary to only include slow events
    deletes = []
    for trace in events.keys():
        if not events[trace]['slow']:
            deletes.append(trace)
    for delete in deletes:
        del events[delete]
        traces.remove(delete)

    print()

    # see all the trace dictionaries
    for trace in events.keys():
        print(events[trace])

    print("***************************One Trace****************************")

    dist = {}
    for trace in traces:
        # find all the marginal arguments for ONE trace
        traces_in_span = []
        traces = list(events.keys())
        for key in events[trace].keys():
            if key != 'slow':
                traces_in_span.append(key)

        traces_in_span = sorted(traces_in_span)

        # see all the powersets
        powersets = powerset(traces_in_span)
        marginals_args = []
        marginalargset = "whatever"
        while(marginalargset != "donee"):
            marginalargset = next(powersets, 'donee')
            if marginalargset != [] and marginalargset != 'donee':
                marginals_args.append(marginalargset)

        # print("HERE ARE THE MARGINAL ARGS")
        # print(marginals_args)
        # print(len(events))
        # print(events_num)

        # Add all the marginal_args to the distribution

        for args in marginals_args:
            print("processing ", end='')
            print(args)
            # print(dist.keys())
            if ",".join(args) not in list(dist.keys()):
                dist[",".join(args)] = 1
                print("new args")
            else:
                dist[",".join(args)] += 1
                print("old args")
            print()

    print(dist)
    print(len(traces))

    return "somethin great, an expectation"


if __name__ == "__main__":
    # app.run(port=8081)
    # app.run(debug=True, host='0.0.0.0')
    format()
