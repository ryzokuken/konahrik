import time

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    nahkriin = requests.get('http://linkerd:9001').text
    return "Rahgot\n Nahkriin: {}".format(nahkriin)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)