import time

import redis
from flask import Flask

from jaeger_client import Config
from flask_opentracing import FlaskTracer

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def initialize_tracer():
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'local_agent': {'reporting_host': 'jaeger'}
        },
        service_name='krosis'
    )
    return config.initialize_tracer()


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def index_krosis():
    count = get_hit_count()
    return 'Krosis {}\n'.format(count)

if __name__ == "__main__":
    flask_tracer = FlaskTracer(initialize_tracer, True, app)
    app.run(host="0.0.0.0", debug=True)
