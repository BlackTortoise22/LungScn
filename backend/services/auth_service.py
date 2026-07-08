from backend import bcrypt
from backend.models.user import User
from backend.repositories.auth_repository import AuthRepository


class AuthService:

    @staticmethod
    def authenticate(email, password):

        user = AuthRepository.get_user_by_email(email)

        if user is None:
            return None

        if not bcrypt.check_password_hash(
            user["password"],
            password
        ):
            return None

        return User(user)
   