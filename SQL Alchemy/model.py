"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from correlation import pearson
import math
# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


class User(db.Model):
    """User of ratings website."""

    __tablename__ = "Users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    @classmethod
    def user_auth(cls, email, password):
        """Get ID of User whoes email and password is given in the arguments"""
        current_user_id = db.session.query(cls.user_id, cls.email).filter(cls.email==email, cls.password==password).first()
        return current_user_id



    def user_deets(self):
        """Get user details to load onto page"""
        pass


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id= %s email= %s>" % (self.user_id, self.email)


class Movie(db.Model):
    """Movie Table of ratings website."""
    
    __tablename__ = "Movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    released_at = db.Column(db.DateTime, nullable=False)
    imdb_url = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Movie Title= %s Release Date= %s>" % (self.title, self.released_at)


class Rating(db.Model):
    """User Ratings of ratings website."""
    
    __tablename__ = "Ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    score = db.Column(db.Integer, nullable=False)

     # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("Ratings", order_by=rating_id))

    # Define relationship to movie
    movie = db.relationship("Movie",
                            backref=db.backref("Ratings", order_by=rating_id))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Movie ID= %s User ID= %s Score= %s>" % (self.movie_id, self.user_id, self.score)

    # @classmethod
    # def add_rating_to_db(cls, score, user_id, movie_id):
    #     score_to_add = cls(movie_id, user_id, score)
    #     db.session.add(score_to_add)


# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."