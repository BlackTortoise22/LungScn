from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_user, logout_user

from backend.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":

        return render_template(
            "auth/login.html"
        )

    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:

        flash(
            "Please enter Email and Password.",
            "danger"
        )

        return redirect(
            url_for("auth.login")
        )

    user = AuthService.authenticate(
        email,
        password
    )

    if user is None:

        flash(
            "Invalid Email or Password.",
            "danger"
        )

        return redirect(
            url_for("auth.login")
        )

    login_user(user)

    flash(
        f"Welcome {user.full_name}",
        "success"
    )

    return redirect(
        url_for("dashboard.dashboard")
    )


@auth_bp.route("/logout")
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )