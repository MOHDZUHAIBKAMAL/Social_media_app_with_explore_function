class UserView:
    @staticmethod
    def render_user(user):
        return {
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name,
            "bio": user.bio,
            "created_at": user.created_at
        }


    @staticmethod
    def render_users(users):
        # # List Comprehension in Python
        # l1 = []
        # for user in users:
        #     l1.append(UserView.render_user(user))

        return [ UserView.render_user(user) for user in users]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, user_id=None):
        response = {"message": message}
        if user_id:
            response["user_id"] = user_id
        return response
    

    @staticmethod
    def render_followed_id(Follow):
        return{
            "Follows":Follow.followed_id
        }
    @staticmethod
    def render_followed_ids(Follows):
        return [
            UserView.render_followed_id(Follow) for Follow in Follows
        ]
