from flask import Blueprint, render_template
from flask_login import login_required

patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/patients"
)


@patient_bp.route("/")
@login_required
def patient_home():
    patients = [
        {
            "code": "LS-1001",
            "name": "John Doe",
            "age": 52,
            "gender": "Male",
            "phone": "+1 555 0101",
            "last_scan": "COVID-19",
        },
        {
            "code": "LS-1002",
            "name": "Jane Smith",
            "age": 43,
            "gender": "Female",
            "phone": "+1 555 0102",
            "last_scan": "Normal",
        },
        {
            "code": "LS-1003",
            "name": "Alex Johnson",
            "age": 61,
            "gender": "Other",
            "phone": "+1 555 0103",
            "last_scan": "Tuberculosis",
        },
    ]

    return render_template("patients/list.html", patients=patients)


@patient_bp.route("/add")
@login_required
def add_patient():
    return render_template("patients/add.html")
