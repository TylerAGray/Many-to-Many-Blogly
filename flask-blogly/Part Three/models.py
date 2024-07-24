import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy for the app
db = SQLAlchemy()

# Default image URL for users without a specified image
DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """Site user model."""

    __tablename__ = "users"

    # Define columns for the user table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    first_name = db.Column(db.Text, nullable=False)  # User's first name
    last_name = db.Column(db.Text, nullable=False)  # User's last name
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)  # User's profile image URL

    # Establish a one-to-many relationship with posts
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return the full name of the user."""
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Blog post model."""

    __tablename__ = "posts"

    # Define columns for the post table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each post
    title = db.Column(db.Text, nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Content of the post
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)  # Timestamp for when the post was created
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key linking to the user

    @property
    def friendly_date(self):
        """Return the date in a user-friendly format."""
        return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")

class PostTag(db.Model):
    """Associative table for tags on posts."""

    __tablename__ = "posts_tags"

    # Define composite primary key for post and tag associations
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)  # Foreign key linking to post
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)  # Foreign key linking to tag

class Tag(db.Model):
    """Tag model that can be associated with posts."""

    __tablename__ = 'tags'

    # Define columns for the tag table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each tag
    name = db.Column(db.Text, nullable=False, unique=True)  # Name of the tag

    # Establish a many-to-many relationship with posts
    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        backref="tags",
    )

def connect_db(app):
    """Connect this database to the provided Flask app.
    
    """
    db.app = app
    db.init_app(app)
