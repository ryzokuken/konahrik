from flask import Flask
from grtracer import GrTracer

app = Flask(__name__)
tracer = GrTracer(app, 'nahkriin')


@app.route('/')
def hello():
    return "Nahkriin\n"


tracer.bootstrap()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
