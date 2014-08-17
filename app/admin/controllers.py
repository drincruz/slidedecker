"""
Admin interface controllers

"""

from app import db
from app.slides.models import Slide
from flask import Blueprint, flash, jsonify, redirect, request, render_template, url_for

admin = Blueprint('admin', __name__, url_prefix='/admin')

# Slide data keys 
_SLIDE_KEYS = ['bg_color', 'bg_image', 'text', 'title']

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
    # Since we do not require any of the fields, we'll set them to None
    for key in _SLIDE_KEYS:
        if key not in slide_data:
            slide_data[key] = None
    title = slide_data['title']
    bg_image = slide_data['bg_image']
    bg_color = slide_data['bg_color']
    text = slide_data['text']

    # Save the form data in the Slide object
    slide = Slide(
            slide_data['title'],
            slide_data['bg_image'],
            slide_data['bg_color'],
            slide_data['text'])

    # Add the records in the database
    db.session.add(slide)
    db.session.commit()

    # Since we're sending back the slide_data, 
    # let's update the object with it's new id
    slide_data['id'] = slide.id

    return jsonify(
            status='success',
            message='Successfully saved slide: {}'.format(slide.id),
            slide_data=slide_data
            )

@admin.route('/update', methods=['POST'])
def update_slide(slide_data):
    """
    Update a slide entry

    """

    slide = db.session.query(Slide).get(slide_data['slide_id'])
    if slide is None:
        return jsonify(
                status='error',
                message='No slide with id: {} was found'.format(slide_id)
                )

    # Update the record in the database
    slide.title = slide_data['title']
    slide.bg_image_uri = slide_data['bg_image']
    slide.bg_color = slide_data['bg_color']
    slide.text = slide_data['text']
    db.session.commit()

    return jsonify(
            status='success',
            message='Successfully saved slide: {}'.format(slide_data['slide_id'])
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
    
    if 'slide_id' in post:
        return update_slide(post)
    else:
        return add_slide(post)

@admin.route('/slide/delete', methods=['POST'])
def slide_delete():
    """
    Delete a slide

    """
    try:
        post = request.get_json()
    except:
        return jsonify(error='Expecting a JSON POST')
    
    if 'slide_id' not in post:
        return jsonify(
                status='error',
                message='Delete slide requires slide_id'
                )
    return _delete_slide(post['slide_id'])

def _delete_slide(slide_id):
    """
    Helper function to delete a slide in SQLAlchemy

    """
    db_session = db.session()
    # Get the slide if it exists first
    try:
        slide = db_session.query(Slide).get(slide_id)
    except Exception as ex:
        return jsonify(
                status='error',
                message='Delete slide exception: {}'.format(ex.message)
                )

    # Delete the slide now
    db_session.delete(slide)
    return jsonify(
            status='success',
            message='Deleted slide successfully'
            )
