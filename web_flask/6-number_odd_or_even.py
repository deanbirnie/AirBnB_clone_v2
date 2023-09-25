#!/usr/bin/python3

"""
Start a Flask web application running
on 0.0.0.0 using port 5000 with routes.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Default route that returns a simple string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cVariable(text):
    """Display 'C' followed by value of text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonVariable(text="is cool"):
    """Display 'Python' followed by the value of text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """Display n followed by a string"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n=None):
    """Display an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEven(n=None):
    """Display an HTML page only if n is an integer"""
    if n % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=None)
