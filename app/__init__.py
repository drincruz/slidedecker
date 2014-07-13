# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import modules for Blueprint
from app.slides.controllers import slides
from app.admin.controllers import admin 

# Register blueprints
app.register_blueprint(slides)
app.register_blueprint(admin)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
