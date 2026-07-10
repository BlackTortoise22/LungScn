from flask import Flask, render_template
from flask_bcrypt import Bcrypt

from backend.config import Config
from backend.utils.login_manager import login_manager

bcrypt = Bcrypt()


def create_app():
    Config.validate()

    app = Flask(__name__)
    app.config.from_object(Config)

    # -----------------------------
    # Initialize Extensions
    # -----------------------------
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # -----------------------------
    # Register Blueprints
    # -----------------------------
    from backend.routes.home import home_bp
    from backend.routes.auth import auth_bp
    from backend.routes.dashboard import dashboard_bp
    from backend.routes.patients import patient_bp
    from backend.routes.predictions import prediction_bp
    from backend.routes.report import report_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(report_bp)

    # -----------------------------
    # Error Pages
    # -----------------------------
    #@app.errorhandler(404)
    #def not_found(error):
        #return render_template("errors/404.html"), 404

    #@app.errorhandler(500)
    #def server_error(error):
        #return render_template("errors/500.html"), 500

    @app.route("/health")
    def health():
        print("HEALTH ROUTE ENTERED")
        return "OK", 200

    return app