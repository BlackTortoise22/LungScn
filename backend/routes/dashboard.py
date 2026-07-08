from flask import Blueprint, render_template

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)

from flask_login import login_required

@dashboard_bp.route("/")
@login_required
def dashboard():

    return render_template(
        "dashboard/dashboard.html"
    )