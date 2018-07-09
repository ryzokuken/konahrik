from flask import Flask
import requests

from middleware import GrTracer

app = Flask(__name__)
tracer = GrTracer(app, 'vokun')


@app.route('/')
def index_vokun():
    krosis = requests.get('http://krosis:5000').text
    rahgot = requests.get('http://rahgot:5000').text
    return "Krosis: {}\nRahgot: {}\n".format(krosis, rahgot)


tracer.bootstrap()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
