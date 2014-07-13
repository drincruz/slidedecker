from app import db
from app.slides.models import Slide
from flask import Blueprint, render_template

slides = Blueprint('slides', __name__, url_prefix='/slides')

@slides.route('/')
def slide_viewer():
    return render_template("slides/slide.html")
