import time

from flask import Flask, abort


app = Flask(__name__)


@app.route('/')
def hello():
    abort(500)
    return "Nahkriin\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)