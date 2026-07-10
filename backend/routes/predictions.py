from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from backend.services.patient_service import PatientService
from backend.services.prediction_service import PredictionService


prediction_bp = Blueprint(
    "prediction",
    __name__,
    url_prefix="/prediction"
)


@prediction_bp.route("/", methods=["GET", "POST"])
@login_required
def prediction_home():

    patients = PatientService.get_all_patients()

    if request.method == "POST":

        if "xray" not in request.files:

            flash(
                "Please choose an X-ray image.",
                "warning"
            )

            return render_template(
                "prediction/upload.html",
                patients=patients
            )

        image = request.files["xray"]

        if image.filename == "":

            flash(
                "No image selected.",
                "warning"
            )

            return render_template(
                "prediction/upload.html",
                patients=patients
            )

        upload_dir = (
            Path(current_app.static_folder)
            / "uploads"
        )

        result = PredictionService.process_prediction(
            uploaded_file=image,
            upload_directory=upload_dir,
            patient_id=int(request.form["patient_id"]),
            uploaded_by=current_user.id
        )

        return render_template(
            "prediction/result.html",
            result=result
        )

    return render_template(
        "prediction/upload.html",
        patients=patients
    )


@prediction_bp.route("/result")
@login_required
def prediction_result():

    return render_template(
        "prediction/result.html",
        result=None
    )