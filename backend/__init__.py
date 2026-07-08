from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from backend.config import Config
from backend.models.user import User
from backend.repositories.auth_repository import AuthRepository

bcrypt = Bcrypt()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    user = AuthRepository.get_user_by_id(user_id)

    if user:
        return User(user)

    return None


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login first."
    login_manager.login_message_category = "warning"

    # Register Blueprints
    from backend.routes.auth import auth_bp
    from backend.routes.dashboard import dashboard_bp
    from backend.routes.patients import patient_bp
    from backend.routes.predictions import prediction_bp
    from backend.routes.report import report_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(report_bp)

    return app