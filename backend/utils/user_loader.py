from backend.utils.login_manager import login_manager
from backend.models.user import User
from backend.repositories.auth_repository import AuthRepository


@login_manager.user_loader
def load_user(user_id):

    user = AuthRepository.get_user_by_id(user_id)

    if user:
        return User(user)

    return None