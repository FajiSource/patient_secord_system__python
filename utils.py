from datetime import datetime
from typing import List
from patient import Patient
from enums import PatientStatus


def create_history_entry(action: str, patient: Patient) -> dict:
    return {
        "action": action,
        "patient": f"{patient.first_name} {patient.last_name}",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def get_patient_statistics(patients: List[Patient]) -> dict:
    patient_count = len(patients)
    active_patient_count = sum(
        1 for p in patients 
        if p.status == PatientStatus.ACTIVE.value
    )
    
    return {
        "patient_count": patient_count,
        "active_patient_count": active_patient_count
    }


def format_patient_name(patient: Patient) -> str:
    name = f"{patient.first_name} {patient.last_name}".strip()
    return name if name else "Unnamed Patient"

