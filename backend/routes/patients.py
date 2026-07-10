from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from backend.services.patient_service import PatientService


patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/patients"
)


# ============================================================
# Patient List
# ============================================================

@patient_bp.route("/")
@login_required
def patient_home():

    patients = PatientService.get_all_patients()

    return render_template(
        "patients/list.html",
        patients=patients
    )


# ============================================================
# Add Patient
# ============================================================

@patient_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_patient():

    if request.method == "POST":

        success, result = PatientService.create_patient(
            request.form,
            current_user.id
        )

        if success:

            flash(
                "Patient added successfully.",
                "success"
            )

            return redirect(
                url_for("patient.patient_home")
            )

        flash(
            result,
            "danger"
        )

        return render_template(
            "patients/add.html",
            form=request.form
        )

    return render_template(
        "patients/add.html"
    )


# ============================================================
# Patient Details
# ============================================================

@patient_bp.route("/<int:patient_id>")
@login_required
def patient_details(patient_id):

    patient = PatientService.get_patient_details(
        patient_id
    )

    if not patient:

        flash(
            "Patient not found.",
            "danger"
        )

        return redirect(
            url_for("patient.patient_home")
        )

    return render_template(
        "patients/details.html",
        patient=patient
    )


# ============================================================
# Edit Patient
# ============================================================

@patient_bp.route("/<int:patient_id>/edit", methods=["GET", "POST"])
@login_required
def edit_patient(patient_id):

    patient = PatientService.get_patient(
        patient_id
    )

    if not patient:

        flash(
            "Patient not found.",
            "danger"
        )

        return redirect(
            url_for("patient.patient_home")
        )

    if request.method == "POST":

        success, result = PatientService.update_patient(
            patient_id,
            request.form
        )

        if success:

            flash(
                "Patient updated successfully.",
                "success"
            )

            return redirect(
                url_for(
                    "patient.patient_details",
                    patient_id=patient_id
                )
            )

        flash(
            result,
            "danger"
        )

    return render_template(
        "patients/edit.html",
        patient=patient
    )


# ============================================================
# Delete Patient
# ============================================================

@patient_bp.route("/<int:patient_id>/delete")
@login_required
def delete_patient(patient_id):

    success = PatientService.delete_patient(
        patient_id
    )

    if success:

        flash(
            "Patient deleted successfully.",
            "success"
        )

    else:

        flash(
            "Unable to delete patient.",
            "danger"
        )

    return redirect(
        url_for("patient.patient_home")
    )


# ============================================================
# Search Patients
# ============================================================

@patient_bp.route("/search")
@login_required
def search_patients():

    keyword = request.args.get(
        "q",
        ""
    ).strip()

    patients = PatientService.search_patients(
        keyword
    )

    return render_template(
        "patients/list.html",
        patients=patients,
        keyword=keyword
    )