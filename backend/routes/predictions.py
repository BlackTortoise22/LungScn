from flask import Blueprint

prediction_bp = Blueprint(
    "prediction",
    __name__,
    url_prefix="/prediction"
)


@prediction_bp.route("/")
def prediction_home():
    return "Prediction Module Working"