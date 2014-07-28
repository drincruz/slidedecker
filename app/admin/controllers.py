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
def add_slide(slide_data):
    """
    Adds a slide to the database

    """
    title = slide_data['title']
    bg_image = slide_data['bg_image']
    bg_color = slide_data['bg_color']
    text = slide_data['text']

    # Save the form data in the Slide object
    slide = Slide(title, bg_image, bg_color, text)

    # Add the records in the database
    db.session.add(slide)
    db.session.commit()

    flash('New slide was successfully posted')
    return redirect(url_for('admin.admin_home'))

@admin.route('/update', methods=['POST'])
def update_slide(slide_data):
    """
    Update a slide entry

    """
    slide_id = slide_data['slide_id']

    title = slide_data['title']
    bg_image = slide_data['bg_image']
    bg_color = slide_data['bg_color']
    text = slide_data['text']

    slide = db.session.query(Slide).filter_by(id=slide_id)
    #slide = Slide.query.get(id==slide_id)
    print("[DEBUG] slide query %d" % slide_id)
    print(slide)
    if slide is None:
        return jsonify(
                status='error',
                message='No slide with id: {} was found'.format(slide_id)
                )

    # Update the record in the database
    slide.title = title
    slide.bg_image_uri = bg_image
    slide.bg_color = bg_color
    slide.text = text
    db.session.commit()

    return jsonify(
            status='success',
            message='Successfully saved slide: {}'.format(slide_id)
            )

@admin.route('/slide/edit', methods=['POST'])
def slide_edit():
    """
    Route an add/update to a controller

    """
    try:
        post = request.get_json()
    except:
        return jsonify(error='Expecting a JSON POST')
        post['slide_id']
    if 'slide_id' in post:
        return update_slide(post)
    else:
        return add_slide(post)
