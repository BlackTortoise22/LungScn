from flask import Blueprint

patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/patients"
)


@patient_bp.route("/")
def patient_home():
    return "Patient Module Working"