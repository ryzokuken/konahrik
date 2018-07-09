from flask import Flask
import requests

from middleware import initialize, trace

app = Flask(__name__)
tracer, ftracer = initialize(app, 'vokun')


@app.route('/')
@trace(tracer, ftracer)
def index_vokun():
    krosis = requests.get('http://krosis:5000').text
    rahgot = requests.get('http://rahgot:5000').text
    return "Krosis: {}\nRahgot: {}\n".format(krosis, rahgot)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
