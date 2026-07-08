from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, user):

        self.id = user["user_id"]
        self.full_name = user["full_name"]
        self.email = user["email"]
        self.role = user["role"]