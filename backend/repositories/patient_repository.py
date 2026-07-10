from backend.database.db import db_cursor
from backend.models.patient import Patient


class PatientRepository:

    @staticmethod
    def get_all_patients():

        with db_cursor() as cursor:

            cursor.execute("""
                SELECT *
                FROM patients
                ORDER BY patient_id DESC
            """)

            rows = cursor.fetchall()

            return [
                Patient(**row)
                for row in rows
            ]
    
    @staticmethod
    def get_patient_details(patient_id):
        
        with db_cursor() as cursor:
            
            cursor.execute("""
                SELECT *
                FROM patients
                WHERE patient_id=%s
            """, (patient_id,))
            
            row = cursor.fetchone()
            
            if not row:
                return None
            
            return Patient(**row)

    @staticmethod
    def create_patient(patient):

        with db_cursor() as cursor:

            cursor.execute("""
                INSERT INTO patients
                (
                    patient_code,
                    full_name,
                    age,
                    gender,
                    phone,
                    email,
                    address,
                    symptoms,
                    registered_by
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s
                )
            """,
            (
                patient.patient_code,
                patient.full_name,
                patient.age,
                patient.gender,
                patient.phone,
                patient.email,
                patient.address,
                patient.symptoms,
                patient.registered_by
            ))

            return cursor.lastrowid

    @staticmethod
    def update_patient(patient):

        with db_cursor() as cursor:

            cursor.execute("""
                UPDATE patients
                SET
                    full_name=%s,
                    age=%s,
                    gender=%s,
                    phone=%s,
                    email=%s,
                    address=%s,
                    symptoms=%s
                WHERE patient_id=%s
            """,
            (
                patient.full_name,
                patient.age,
                patient.gender,
                patient.phone,
                patient.email,
                patient.address,
                patient.symptoms,
                patient.patient_id
            ))
    @staticmethod
    def get_patient_details(patient_id):
        return PatientRepository.get_patient_details(patient_id)

    @staticmethod
    def delete_patient(patient_id):

        with db_cursor() as cursor:

            cursor.execute("""
                DELETE FROM patients
                WHERE patient_id=%s
            """,
            (patient_id,))

    @staticmethod
    def search_patients(keyword):

        with db_cursor() as cursor:

            cursor.execute("""
                SELECT *
                FROM patients
                WHERE
                    full_name LIKE %s
                    OR patient_code LIKE %s
                    OR phone LIKE %s
                ORDER BY patient_id DESC
            """,
            (
                f"%{keyword}%",
                f"%{keyword}%",
                f"%{keyword}%"
            ))

            rows = cursor.fetchall()

            return [
                Patient(**row)
                for row in rows
            ]