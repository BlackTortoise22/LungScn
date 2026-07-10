from backend.models.patient import Patient
from backend.repositories.patient_repository import PatientRepository
from backend.utils.patient_code import generate_patient_code
from backend.utils.validators import Validator


class PatientService:

    @staticmethod
    def get_all_patients():
        return PatientRepository.get_all_patients()

    @staticmethod
    def get_patient(patient_id):
        return PatientRepository.get_patient_by_id(patient_id)

    @staticmethod
    def create_patient(data, registered_by):

        valid, message = Validator.validate_patient(data)

        if not valid:
            return False, message

        patient = Patient(
            patient_code=generate_patient_code(),
            full_name=data["full_name"],
            age=int(data["age"]),
            gender=data["gender"],
            phone=data["phone"],
            email=data.get("email", ""),
            address=data.get("address", ""),
            symptoms=data.get("symptoms", ""),
            registered_by=registered_by
        )

        patient_id = PatientRepository.create_patient(patient)

        return True, patient_id

    @staticmethod
    def update_patient(patient_id, data):

        valid, message = Validator.validate_patient(data)

        if not valid:
            return False, message

        patient = Patient(
            patient_id=patient_id,
            full_name=data["full_name"],
            age=int(data["age"]),
            gender=data["gender"],
            phone=data["phone"],
            email=data.get("email", ""),
            address=data.get("address", ""),
            symptoms=data.get("symptoms", "")
        )

        PatientRepository.update_patient(patient)

        return True, "Patient updated successfully."

    @staticmethod
    def delete_patient(patient_id):

        PatientRepository.delete_patient(patient_id)

        return True

    @staticmethod
    def search_patients(keyword):

        if not keyword:
            return PatientRepository.get_all_patients()

        return PatientRepository.search_patients(keyword)