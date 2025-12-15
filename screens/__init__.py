"""Screens package for Patient Record System."""
# Import ng lahat ng screen classes
from .welcome_screen import WelcomeScreen
from .dashboard_screen import DashboardScreen
from .patients_screen import PatientsScreen
from .add_patient_screen import AddPatientScreen
from .view_patient_screen import ViewPatientScreen
from .history_screen import HistoryScreen

__all__ = [
    'WelcomeScreen',
    'DashboardScreen',
    'PatientsScreen',
    'AddPatientScreen',
    'ViewPatientScreen',
    'HistoryScreen'
]

