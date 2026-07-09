from flask import Blueprint, render_template
from flask_login import login_required

report_bp = Blueprint(
    "report",
    __name__,
    url_prefix="/reports"
)


@report_bp.route("/")
@login_required
def report_home():
    reports = [
        {
            "id": "RPT-2048",
            "patient": "Jane Smith",
            "finding": "Normal",
            "generated_at": "Today",
        },
        {
            "id": "RPT-2047",
            "patient": "John Doe",
            "finding": "COVID-19",
            "generated_at": "Yesterday",
        },
    ]

    return render_template("reports/history.html", reports=reports)
