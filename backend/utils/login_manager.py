from flask_login import LoginManager

from backend.repositories.auth_repository import AuthRepository

from backend.models.user import User

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.login_message = "Please login first."


@login_manager.user_loader
def load_user(user_id):

    user = AuthRepository.get_user_by_id(user_id)

    if user:

        return User(user)

    return None
@staticmethod
def get_user_by_id(user_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE user_id=%s
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()

    connection.close()

    return user