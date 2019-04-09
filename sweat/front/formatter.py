import time
import requests
from flask import Flask
from flask import request

app = Flask(__name__)


def http_get(port, path, param, value):
    url = 'http://app-aserv:%s/%s' % (port, path)
    # r = requests.get(url, params={param: value}, headers=headers, timeout=1)
    session = requests.Session()
    session.trust_env = False
    r = session.get(url)
    assert r.status_code == 200
    return r.text


@app.route("/format")
def format():
    start = time.time()
    grand_result = ""

    for n in range(20):
        hello_to = "suzanna"
        try:
            print("Before request: " + hello_str)
            hello_str = http_get(5000, 'format', 'helloTo', hello_to)
            print("After request: " + hello_str)
        except:
            print("front: The get request failed")
            hello_str = hello_to + "failed request"

        end = time.time()
        duration = round(end - start, 4)
        hello_str = hello_str + ". 'front' measures: " + str(duration) + " ms"
        grand_result = grand_result + hello_str + "<br/>"

    return grand_result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
