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
import datetime

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


@app.route("/")
def format():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    size = 1000
    threshold = 60000

    d = str(datetime.datetime.today()).split()[0]
    d = "2019-04-30"
    # get list of all traces
    res = es.search(index='jaeger-span-' + d, size=size)
    a = res['hits']['hits']
    # pp = pprint.PrettyPrinter(indent=0)
    # pp.pprint(a[0])

    # get useful lists
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

    # build events dictionary
    events = {}
    for i in range(len(traces)):
        search = {"query": {"match": {'traceID': traces[i]}}}
        res = es.search(index='jaeger-span-' + d, body=search, size=size)
        a = res['hits']['hits']  # all the spans to do with this trace

        for trace in a:
            service = trace['_source']['process']['serviceName']
            traceID = trace['_source']['traceID']
            spanID = trace['_source']['spanID']
            duration = trace['_source']['duration']
            if traceID not in events.keys():
                events[traceID] = {}
            events[traceID][service] = duration

    # for trace in events.keys():
    #     print(events[trace])

    # identify slow traces
    for trace in events.keys():
        slow = False
        for service in events[trace].keys():
            if events[trace][service] > threshold:
                slow = True
        events[trace]['slow'] = slow

    # Get counts for (path, speed)
    slow_counts = {}
    fast_counts = {}
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
        while (marginalargset != "donee"):
            marginalargset = next(powersets, 'donee')
            if marginalargset != [] and marginalargset != 'donee':
                marginals_args.append(marginalargset)

        # Add all the marginal_args to the distribution
        for args in marginals_args:
            if events[trace]['slow']:
                if ",".join(args) not in list(slow_counts.keys()):
                    slow_counts[",".join(args)] = 1
                else:
                    slow_counts[",".join(args)] += 1
            elif not events[trace]['slow']:
                if ",".join(args) not in list(fast_counts.keys()):
                    fast_counts[",".join(args)] = 1
                else:
                    fast_counts[",".join(args)] += 1

    # Calculate conditional distributions
    cond_dist = {}
    for slow_args, slow_count in slow_counts.items():
        if slow_args in list(fast_counts.keys()):
            cond_dist[slow_args] = slow_count / (slow_count + fast_counts[slow_args])
        else:
            cond_dist[slow_args] = slow_count / slow_count

    keys = []
    for k, v in cond_dist.items():
        keys.append(k.split(','))
        keys[-1].append(v)

    diagnosis = sorted(keys, key=len)

    result = ""
    for diagnosis in diagnosis:
        services = ' & '.join(diagnosis[:-1])
        result = result + "P(" + str(services) + ") = " + str(round(diagnosis[-1], 2)) + "<br/>"

    print(result)
    return '<font size="22">' + result + '</font>'


if __name__ == "__main__":
    # app.run(port=8081)
    app.run(debug=True, host='0.0.0.0', port=5000)
    # format()
