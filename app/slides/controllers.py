"""
Slide Viewer controllers

"""

from app import db
from app.slides.models import Slide
from flask import Blueprint, render_template

slides = Blueprint('slides', __name__, url_prefix='/slides')

@slides.route('/')
def slide_viewer():
    """
    Main slide viewer controller

    """
    # Get all slides from the database
    slides = db.session().query(Slide).all()
    return render_template("slides/slide.html", slides=slides)
