from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, user):

        self.id = user["user_id"]
        self.full_name = user["full_name"]
        self.email = user["email"]
        self.role = user["role"]

        # Optional information
        self.phone = user.get("phone")
        self.created_at = user.get("created_at")
        self.updated_at = user.get("updated_at")

    def is_admin(self):
        return self.role == "Admin"

    def is_doctor(self):
        return self.role == "Doctor"

    def __repr__(self):
        return f"<User {self.email}>"