#!/usr/bin7python3
""" script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return a hello string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return a hbnb string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ returns a string depending on the text they give us as an argument """
    new_text = text.replace('_', ' ')
    return f"C {new_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ returns a string depending on the text they give us as an argument """
    new_text = text.replace('_', ' ')
    return f"Python {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
