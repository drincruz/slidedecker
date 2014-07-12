# Import the database object (db) from the main application module
from app import db


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

class Slide(Base):
    """
    Data class to model a Slide

    """
   
    __tablename__ = 'slide_data'

    # Slide title
    title = db.Column(db.String(256), nullable=True)

    # Background Image URI
    bg_image_uri = db.Column(db.String(256), nullable=True)
    
    # Background Color
    bg_color = db.Column(db.String(256), nullable=True)
    
    # Slide text
    text = db.Column(db.Text(1024), nullable=True)

    # New instance 
    def __init__(self,
            title=None,
            bg_image_uri=None,
            bg_color=None,
            text=None):
        self.title = title
        self.bg_image_uri = bg_image_uri
        self.bg_color = bg_color
        self.text = text

    def __repr__(self):
        return '<Slide %s>
