import json
import os
from typing import List
from patient import Patient


class DataManager:
    
    PATIENTS_FILE = "patients.json"
    HISTORY_FILE = "history.json"
    
    @staticmethod
    def load_patients() -> List[Patient]:
        if os.path.exists(DataManager.PATIENTS_FILE):
            try:
                with open(DataManager.PATIENTS_FILE, "r") as f:
                    patients_data = json.load(f)
                    return [Patient.from_dict(p) for p in patients_data]
            except Exception:
                return []
        return []
    
    @staticmethod
    def save_patients(patients: List[Patient]) -> None:
        with open(DataManager.PATIENTS_FILE, "w") as f:
            patients_dicts = [p.to_dict() for p in patients]
            json.dump(patients_dicts, f)
    
    @staticmethod
    def load_history() -> List[dict]:
        if os.path.exists(DataManager.HISTORY_FILE):
            try:
                with open(DataManager.HISTORY_FILE, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []
    
    @staticmethod
    def save_history(history: List[dict]) -> None:
        with open(DataManager.HISTORY_FILE, "w") as f:
            json.dump(history, f)

