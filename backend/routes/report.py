from flask import Blueprint

report_bp = Blueprint(
    "report",
    __name__,
    url_prefix="/reports"
)


@report_bp.route("/")
def report_home():
    return "Report Module Working"