import time
import requests
from flask import Flask
from flask import request

app = Flask(__name__)


def http_get(rooturl, port, path, param, value):
    url = rooturl % (port, path)
    # r = requests.get(url, params={param: value}, timeout=1)
    session = requests.Session()
    session.trust_env = False
    r = session.get(url, params={param: value}, timeout=1)
    assert r.status_code == 200
    return r.text


@app.route("/format")
def format():
    grand_result = ""

    rooturl = 'http://app-ios:%s/%s'
    try:
        warmup = http_get(rooturl, 5000, 'format', 'helloTo', hello_to)
    except:
        warmup = "(the warmup get failed)"

    for n in range(1):
        hello_to = "Bierman"

        start = time.time()
        try:
            android_url = 'http://app-android:%s/%s'
            android_response = http_get(android_url, 5000, 'format', 'helloTo', hello_to)
        except:
            android_response = hello_to + ". failed request"
        end = time.time()
        duration = round(end - start, 4)
        android_response = android_response + ". 'front' measures: " + str(duration) + " ms"

        start = time.time()
        try:
            start = time.time()
            web_url = 'http://app-web:%s/%s'
            web_response = http_get(web_url, 5000, 'format', 'helloTo', hello_to)
        except:
            web_response = hello_to + ". failed request"
        end = time.time()
        duration = round(end - start, 4)
        web_response = web_response + ". 'front' measures: " + str(duration) + " ms"

        start = time.time()
        try:
            start = time.time()
            api_url = 'http://app-api:%s/%s'
            api_response = http_get(api_url, 5000, 'format', 'helloTo', hello_to)
        except:
            api_response = hello_to + ". failed request"
        end = time.time()
        duration = round(end - start, 4)
        api_response = api_response + ". 'front' measures: " + str(duration) + " ms"

        start = time.time()
        try:
            ios_url = 'http://app-ios:%s/%s'
            ios_response = http_get(ios_url, 5000, 'format', 'helloTo', hello_to)
        except:
            ios_response = hello_to + ". failed request"
        end = time.time()
        duration = round(end - start, 4)
        ios_response = ios_response + ". 'front' measures: " + str(duration) + " ms"

        grand_result = grand_result + \
                       android_response + "<br/>" + \
                       web_response + "<br/>" + \
                       api_response + "<br/>" + \
                       ios_response + "<br/>"

    return warmup + "<br/>" + grand_result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
