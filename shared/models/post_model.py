from datetime import datetime
from shared.utils.db_utils import db
from shared.models.user_model import User

class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    visibility = db.Column(db.String(50), default="public")
    
    user = db.relationship('User', back_populates='posts')
    