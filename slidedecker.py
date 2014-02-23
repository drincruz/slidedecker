#!/usr/bin/env python

"""
SlideDecker

Presentations for web browsers
"""

__version__ = '0.1'

from flask import Flask, render_template


app = Flask(__name__)

# TODO get rid of this for "production"-ready
app.debug = True

@app.route('/')
def slides():
    return render_template("slide.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

if "__main__" == __name__:
    app.run()
