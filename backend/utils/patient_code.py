from backend.database.db import db_cursor


def generate_patient_code():
    """
    Generate patient codes like:
    LS-1001
    LS-1002
    LS-1003
    """

    with db_cursor() as cursor:

        cursor.execute(
            """
            SELECT patient_code
            FROM patients
            ORDER BY patient_id DESC
            LIMIT 1
            """
        )

        row = cursor.fetchone()

    if not row:
        return "LS-1001"

    last_code = row["patient_code"]

    last_number = int(last_code.split("-")[1])

    return f"LS-{last_number + 1}"