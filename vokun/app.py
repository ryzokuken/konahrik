import time

from flask import Flask
import requests

from jaeger_client import Config
from flask_opentracing import FlaskTracer

app = Flask(__name__)

@app.route('/')
def index_vokun():
    krosis = requests.get('http://krosis:5000').text
    rahgot = requests.get('http://rahgot:5000').text
    return "Krosis: {}\nRahgot: {}\n".format(krosis, rahgot)

def initialize_tracer():
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {'reporting_host': 'jaeger'}
        },
        service_name='vokun'
    )
    return config.initialize_tracer()

if __name__ == "__main__":
    flask_tracer = FlaskTracer(initialize_tracer, True, app)
    app.run(host='0.0.0.0')
