from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user,
)

from backend.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:

            flash(
                "Please enter email and password.",
                "danger",
            )

            return render_template("auth/login.html")

        user = AuthService.authenticate(
            email,
            password,
        )

        if user:

            remember = request.form.get("remember") == "on"

            login_user(
                user,
                remember=remember,
            )

            flash(
                f"Welcome back, {user.full_name}!",
                "success",
            )

            return redirect(
                url_for("dashboard.dashboard")
            )

        flash(
            "Invalid email or password.",
            "danger",
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success",
    )

    return redirect(
        url_for("auth.login")
    )