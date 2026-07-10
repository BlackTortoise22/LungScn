from pathlib import Path
import uuid

from werkzeug.utils import secure_filename

from backend.ai.inference.predictor import predict
from backend.repositories.xray_scan_repository import XrayScanRepository
from backend.repositories.prediction_repository import PredictionRepository


class PredictionService:

    MODEL_NAME = "LungNN"
    MODEL_VERSION = "v1.0"

    @staticmethod
    def save_uploaded_image(uploaded_file, upload_directory):

        upload_directory = Path(upload_directory)

        upload_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        original_name = secure_filename(
            uploaded_file.filename
        )

        extension = Path(original_name).suffix.lower()

        filename = f"{uuid.uuid4().hex}{extension}"

        image_path = upload_directory / filename

        uploaded_file.save(image_path)

        return image_path

    @staticmethod
    def predict_image(image_path):

        image_path = Path(image_path)

        if not image_path.exists():

            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        prediction = predict(image_path)

        return prediction

    @staticmethod
    def process_prediction(
        uploaded_file,
        upload_directory,
        patient_id,
        uploaded_by
    ):

        image_path = PredictionService.save_uploaded_image(
            uploaded_file,
            upload_directory
        )

        scan_id = XrayScanRepository.create_scan(
            patient_id=patient_id,
            uploaded_by=uploaded_by,
            image_name=image_path.name,
            image_path=str(image_path).replace("\\", "/")
        )

        prediction = PredictionService.predict_image(
            image_path
        )

        prediction_id = PredictionRepository.create_prediction(
            scan_id=scan_id,
            disease=prediction["prediction"],
            confidence=prediction["confidence"],
            model_version=PredictionService.MODEL_VERSION
        )

        return {

            "prediction_id": prediction_id,

            "scan_id": scan_id,

            "patient": None,

            "disease": prediction["prediction"],

            "confidence": f"{prediction['confidence']:.2f}%",

            "probabilities": prediction["probabilities"],

            "model_name": PredictionService.MODEL_NAME,

            "model_version": PredictionService.MODEL_VERSION,

            "image_path": str(image_path).replace("\\", "/")
        }