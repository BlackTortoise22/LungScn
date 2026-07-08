from flask import Flask

from backend.config import Config


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # Register Blueprints
    from backend.routes.auth import auth_bp
    from backend.routes.patients import patient_bp
    from backend.routes.predictions import prediction_bp
    from backend.routes.report import report_bp
    from backend.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(dashboard_bp)

    return app