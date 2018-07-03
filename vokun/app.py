import time

from flask import Flask
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    krosis = requests.get('http://krosis:5000').text
    rahgot = requests.get('http://rahgot:5000').text
    return "Krosis: {}\nRahgot: {}\n".format(krosis, rahgot)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)