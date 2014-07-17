"""
Admin interface controllers

"""

from app import db
from app.slides.models import Slide
from flask import Blueprint, flash, redirect, request, render_template, url_for

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_home():
    return render_template("admin/admin.html")

@admin.route('/add', methods=['POST'])
def add_slide():
    # TODO store slide data
    title = request.form['title']
    bg_image = request.form['bg-image']
    bg_color = request.form['bg-color']
    text = request.form['text']
    flash('New slide was successfully posted')
    return redirect(url_for('admin.admin_home'))
