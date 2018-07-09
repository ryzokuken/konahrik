import time

import redis
from flask import Flask

from middleware import initialize, trace

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
tracer, ftracer = initialize(app, 'krosis')


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
@trace(tracer, ftracer)
def index_krosis():
    count = get_hit_count()
    return 'Krosis {}\n'.format(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
