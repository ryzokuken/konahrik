import time

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    foo = requests.get('http://foo:5000').text
    bar = requests.get('http://bar:5000/').text
    return "foo: {}\nbar: {}\n".format(foo, bar)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)