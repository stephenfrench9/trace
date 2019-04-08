import time
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

def http_get(port, path, param, value):
    url = 'http://app-aserv:%s/%s' % (port, path)

    print('making request to %s' % url)


    # r = requests.get(url, params={param: value}, headers=headers, timeout=1)

    session = requests.Session()
    print(type(session))
    session.trust_env = False
    # r = session.get(url, json=my_json)
    r = session.get(url)

    print("the request happened")
    assert r.status_code == 200
    return r.text

@app.route("/")
def format():
    start = time.time()
    hello_str = "suzan"
    hello_to = "suzanna"

    try:
        print("trying the request")
        hello_str = http_get(5000, 'format', 'helloTo', hello_to)
        print("the result is: ")
    except:
        print("front: The get request failed")

    end = time.time()
    duration = end - start
    hello_str = hello_str + ". time: " + str(duration) + " ms"
    return hello_str # two submissions to format servers


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 4999)

