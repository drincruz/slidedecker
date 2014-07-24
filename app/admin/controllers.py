"""
Admin interface controllers

"""

from app import db
from app.slides.models import Slide
from flask import Blueprint, flash, jsonify, redirect, request, render_template, url_for

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_home():
    """
    Admin home

    """
    return render_template("admin/admin.html")

@admin.route('/get/slides')
def get_slides():
    """
    Gets all slides stored in the database
    and returns them in json format

    """
    db_session = db.session()
    slides = db_session.query(Slide).all()
    json_ret = []
    for slide in slides:
        json_ret.append(
                {
                    'id': slide.id,
                    'title': slide.title,
                    'bg_image': slide.bg_image_uri,
                    'bg_color': slide.bg_color,
                    'text': slide.text,
                })
    return jsonify(slides=json_ret)

@admin.route('/add', methods=['POST'])
def add_slide(request):
    """
    Adds a slide to the database

    """
    title = request.form['title']
    bg_image = request.form['bg-image']
    bg_color = request.form['bg-color']
    text = request.form['text']

    # Save the form data in the Slide object
    slide = Slide(title, bg_image, bg_color, text)

    # Add the records in the database
    db.session.add(slide)
    db.session.commit()

    flash('New slide was successfully posted')
    return redirect(url_for('admin.admin_home'))

@admin.route('/update', methods=['POST'])
def update_slide(request):
    """
    Update a slide entry

    """
    slide_id = request.form['slide_id']

    title = request.form['title']
    bg_image = request.form['bg-image']
    bg_color = request.form['bg-color']
    text = request.form['text']

    try:
        slide = Slide.query.get(id==slide_id)
    except NoResultFound:
        flash('ERROR: No Slide was found.')
        return redirect(url_for('admin.admin_home'))

    # Update the record in the database
    slide.title = title
    slide.bg_image_uri = bg_image
    slide.bg_color = bg_color
    slide.text = text
    db.session.commit()

    flash('Slide was successfully updated')
    return redirect(url_for('admin.admin_home'))

@admin.route('/slide/edit', methods=['POST'])
def slide_edit():
    """
    Route an add/update to a controller

    """
    # TODO properly get json post data
    try:
        request = request.get_json()
    except:
        pass
    print(request.get_json()) # TODO DELETE
    print(request.slide_id) # TODO DELETE
    if request.slide_id:
        return update_slide(request)
    else:
        return add_slide(request)
