#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "Not Found", 404


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', num=n)
    else:
        return "Not Found", 404


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if (n % 2) == 0:
        number_is = 'even'
    else:
        number_is = 'odd'
    context = {'num': n, 'n_is': number_is}
    return render_template("6-number_odd_or_even.html", **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
