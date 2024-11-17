from shared.models.user_model import User
from shared.models.user_model import Follow
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(username, email, password, full_name, bio):
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password, full_name=full_name, bio=bio)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def follow_user(follower_id,followed_id):
        existing_follow = Follow.query.filter_by(follower_id=follower_id, followed_id=followed_id).first()
        if existing_follow:
            return "Already following this user."
        new_follow=Follow(followed_id=followed_id,follower_id=follower_id)
        db.session.add(new_follow)
        db.session.commit()
        return new_follow
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def verify_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def get_all_followed(follower_id):
        return Follow.query.filter_by(follower_id=follower_id).all()
        