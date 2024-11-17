from shared.models.post_model import Post
from shared.utils.db_utils import db
from shared.models.user_model import Follow
import random

class PostService:
    @staticmethod
    def create_post(user_id, content,visibility):
        new_post = Post(user_id=user_id, content=content,visibility=visibility)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def explore(user_id):
        posts = Post.query.filter(
        (Post.visibility == 'public') | 
        (Post.visibility == 'followers only' and Follow.query.filter_by(follower_id=user_id, followed_id=Post.user_id).exists())).all()

    
        if posts:
            random_post = random.choice(posts)
            return random_post


    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            post.content = new_content
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        return post


