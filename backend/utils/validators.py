import re


class Validator:

    # -----------------------------
    # Authentication
    # -----------------------------
    @staticmethod
    def validate_login(email, password):

        if not email:
            return False, "Email is required."

        if not password:
            return False, "Password is required."

        return True, ""

    # -----------------------------
    # Patient
    # -----------------------------
    @staticmethod
    def validate_patient(data):

        required_fields = [
            "full_name",
            "age",
            "gender",
            "phone"
        ]

        for field in required_fields:

            if not data.get(field):
                return False, f"{field.replace('_', ' ').title()} is required."

        try:
            age = int(data["age"])

            if age <= 0 or age > 120:
                return False, "Please enter a valid age."

        except (TypeError, ValueError):
            return False, "Age must be a number."

        if data["gender"] not in [
            "Male",
            "Female",
            "Other"
        ]:
            return False, "Invalid gender."

        phone = data["phone"]

        if not re.fullmatch(r"[0-9+\-\s]{8,15}", phone):
            return False, "Invalid phone number."

        email = data.get("email", "").strip()

        if email:

            pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

            if not re.match(pattern, email):
                return False, "Invalid email address."

        return True, ""