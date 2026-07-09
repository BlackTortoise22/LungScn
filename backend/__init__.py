from flask import Flask, render_template
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
    Config.validate()

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

    @app.route("/")
    def home():
        return render_template("home/index.html")

    @app.route("/about")
    def about():
        return render_template("about/about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact/contact.html")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html"), 500

    return app
