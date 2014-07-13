from app import db
from app.slides.models import Slide
from flask import (Blueprint, Flask, flash, redirect, render_template,
        url_for)

slides = Blueprint('slides', __name__, url_prefix='/slides')

@slides.route('/')
def slides():
    return render_template("slides/slide.html")
