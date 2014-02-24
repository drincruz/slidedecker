#!/usr/bin/env python

"""
SlideDecker

Presentations for web browsers
"""

__version__ = '0.1.1'

from flask import Flask, flash, redirect, render_template, url_for

_SECRET_KEY = 'seethreepio' # TODO change this, if this will be used over the internet

app = Flask(__name__)

# TODO get rid of this for "production"-ready
app.debug = True

app.secret_key = _SECRET_KEY

@app.route('/')
def slides():
    return render_template("slide.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/admin/add', methods=['POST'])
def add_slide():
    # TODO store slide data
    flash('New slide was successfully posted')
    return redirect(url_for('admin'))

if "__main__" == __name__:
    app.run()
