#!/usr/bin/python3

"""
Default file to start a Flask web application running
on 0.0.0.0 using port 5000.
"""

from flask import Flask


app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Default route that returns a simple string"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
