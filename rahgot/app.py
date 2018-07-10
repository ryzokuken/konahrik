from flask import Flask
import requests
from grtracer import GrTracer

app = Flask(__name__)
tracer = GrTracer(app, 'rahgot', ['requests'])


@app.route('/')
def index_rahgot():
    nahkriin = requests.get('http://nahkriin:5000').text
    return "Rahgot\n Nahkriin: {}".format(nahkriin)


tracer.bootstrap()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
