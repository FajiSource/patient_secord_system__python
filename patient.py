from enums import Gender, PatientStatus, BloodType
from typing import List, Union

class Patient:
    def __init__(self, id: int, first_name: str, last_name: str, middle_name: str = "",
                 birth_date: str = "", gender: str = "", contact: str = "",
                 address: str = "", blood_type: str = "", status: str = "",
                 allergies: Union[str, List[str]] = ""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.gender = gender
        self.contact = contact
        self.address = address
        self.blood_type = blood_type
        self.status = status
        self.allergies = allergies if isinstance(allergies, list) else (allergies.split("\n") if allergies else [])
    
    def to_dict(self) -> dict:
        # Convert Patient object to dictionary for JSON serialization
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "contact": self.contact,
            "address": self.address,
            "blood_type": self.blood_type,
            "status": self.status,
            "allergies": self.allergies if isinstance(self.allergies, list) else []
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Patient':
        # Create Patient object from dictionary
        return Patient(
            id=data.get("id", 0),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            middle_name=data.get("middle_name", ""),
            birth_date=data.get("birth_date", ""),
            gender=data.get("gender", ""),
            contact=data.get("contact", ""),
            address=data.get("address", ""),
            blood_type=data.get("blood_type", ""),
            status=data.get("status", ""),
            allergies=data.get("allergies", [])
        )
    
    def get(self, key: str, default=None):
        # Dictionary-like get method for compatibility
        return getattr(self, key, default)
