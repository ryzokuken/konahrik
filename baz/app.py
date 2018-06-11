import time

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    foo = requests.get('http://linkerd:5001').text
    bar = requests.get('http://linkerd:3001').text
    return "foo: {}\nbar: {}\n".format(foo, bar)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)