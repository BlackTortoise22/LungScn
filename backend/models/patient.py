from dataclasses import dataclass
from typing import Optional


@dataclass
class Patient:

    patient_id: Optional[int] = None
    patient_code: str = ""
    full_name: str = ""
    age: int = 0
    gender: str = ""
    phone: str = ""
    email: str = ""
    address: str = ""
    symptoms: str = ""
    registered_by: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None