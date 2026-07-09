from flask_login import LoginManager

from backend.repositories.auth_repository import AuthRepository
from backend.models.user import User

# Shared Login Manager instance
login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Please login first."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    user = AuthRepository.get_user_by_id(user_id)

    if user:
        return User(user)

    return None