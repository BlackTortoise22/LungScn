from flask import Blueprint, render_template
from flask_login import login_required

prediction_bp = Blueprint(
    "prediction",
    __name__,
    url_prefix="/prediction"
)


@prediction_bp.route("/")
@login_required
def prediction_home():
    return render_template("prediction/upload.html")


@prediction_bp.route("/result")
@login_required
def prediction_result():
    result = {
        "patient": "Jane Smith",
        "disease": "Normal",
        "confidence": "99.2%",
        "model_version": "demo-1.0",
        "explanation": "No acute abnormality is highlighted in this demo result.",
    }

    return render_template("prediction/result.html", result=result)
