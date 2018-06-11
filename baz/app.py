import time

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    krosis = requests.get('http://linkerd:5001').text
    rahgot = requests.get('http://linkerd:3001').text
    return "Krosis: {}\nRahgot: {}\n".format(krosis, rahgot)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)