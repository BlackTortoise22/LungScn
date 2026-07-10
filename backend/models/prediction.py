from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Prediction:

    id: Optional[int] = None

    patient_id: Optional[int] = None

    disease: str = ""

    confidence: float = 0.0

    image_path: str = ""

    model_name: str = ""

    model_version: str = ""

    created_at: Optional[datetime] = None