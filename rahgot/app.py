import time

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Rahgot\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)