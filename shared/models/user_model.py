from datetime import datetime
from shared.utils.db_utils import db



class Follow(db.Model):
    __tablename__ = 'follows'

    follow_id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships for accessing follower and followed user details
    follower = db.relationship('User', foreign_keys=[follower_id], back_populates='following')
    followed = db.relationship('User', foreign_keys=[followed_id], back_populates='followers')


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    following = db.relationship('Follow', foreign_keys=[Follow.follower_id], back_populates='follower')
    followers = db.relationship('Follow', foreign_keys=[Follow.followed_id], back_populates='followed')
    posts = db.relationship('Post', back_populates='user', lazy=True)

