#!/usr/bin/env python

"""
SlideDecker

Presentations for web browsers
"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello you"


if "__main__" == __name__:
    app.run()
