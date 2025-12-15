# Import ng mga kailangang modules
import tkinter as tk
from tkinter import messagebox
from data_manager import DataManager
from ui_components import LogoLoader
from utils import create_history_entry, get_patient_statistics
from screens import (
    WelcomeScreen,
    DashboardScreen,
    PatientsScreen,
    AddPatientScreen,
    ViewPatientScreen,
    HistoryScreen
)


# Main Clas
class PatientRecordSystem:
    
    # Constructor ng sistema
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Record System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#2b2b2b")
        
        # Load Logo
        self.logo_image = LogoLoader.load_logo()
        
        # mga Patient at History mula sa file
        self.patients = DataManager.load_patients()
        self.history = DataManager.load_history()
        
        self.current_screen = None
        
        # call welcome screen
        self.show_welcome_screen()
    
    # clear ang screen bago magpakita ng bagong screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # I save ang mga Patient at History sa file
    def save_data(self):
        DataManager.save_patients(self.patients)
        DataManager.save_history(self.history)
    
    # Ibalik ang mga navigation commands
    def _get_nav_commands(self):
        return {
            "Dashboard": self.show_dashboard,
            "Patients": self.show_patients,
            "New Patient": self.show_add_patient,
            "History": self.show_history
        }
    
    # Ipakita ang welcome screen
    def show_welcome_screen(self):
        self.clear_screen()
        self.current_screen = "welcome"
        WelcomeScreen(self.root, self.show_dashboard)
    
    # Ipakita ang dashboard screen
    def show_dashboard(self):
        self.clear_screen()
        self.current_screen = "dashboard"
        
        # Kunin ang statistics ng mga Patient
        statistics = get_patient_statistics(self.patients)
        nav_commands = self._get_nav_commands()
        
        DashboardScreen(
            self.root,
            self.patients,
            self.history,
            statistics,
            self.logo_image,
            nav_commands
        )
    
    # Ipakita ang listahan ng mga Patient
    def show_patients(self):
        self.clear_screen()
        self.current_screen = "patients"
        
        nav_commands = self._get_nav_commands()
        
        PatientsScreen(
            self.root,
            self.patients,
            self.logo_image,
            nav_commands,
            self.show_view_patient,
            self.show_add_patient
        )
    
    # Ipakita ang screen para magdagdag ng bagong Patient
    def show_add_patient(self):
        self.clear_screen()
        self.current_screen = "add_patient"
        
        nav_commands = self._get_nav_commands()
        
        # Function na tatawagin kapag na-save ang Patient
        def on_save(patient):
            # Bigyan ng ID ang bagong Patient
            patient.id = len(self.patients) + 1
            self.patients.append(patient)
            self.save_data()
            
            # Idagdag sa History
            self.history.append(create_history_entry("Added", patient))
            self.save_data()
            
            messagebox.showinfo("Success", "Patient added successfully!")
            self.show_patients()
        
        AddPatientScreen(
            self.root,
            self.logo_image,
            nav_commands,
            on_save,
            self.show_patients
        )
    
    # Ipakita ang detalye ng isang Patient
    def show_view_patient(self, patient):
        self.clear_screen()
        self.current_screen = "view_patient"
        
        nav_commands = self._get_nav_commands()
        
        # Function para i-update ang Patient
        def on_save(updated_patient):
            # Hanapin at i-update ang Patient sa listahan
            for i, p in enumerate(self.patients):
                if p.id == updated_patient.id:
                    self.patients[i] = updated_patient
                    break
            
            self.save_data()
            
            # Idagdag sa History
            self.history.append(create_history_entry("Updated", updated_patient))
            self.save_data()
            
            messagebox.showinfo("Success", "Patient updated successfully!")
        
        # Function para tanggalin ang Patient
        def on_delete():
            # Idagdag sa History bago tanggalin
            self.history.append(create_history_entry("Deleted", patient))
            
            # Tanggalin ang Patient mula sa listahan
            self.patients = [p for p in self.patients if p.id != patient.id]
            self.save_data()
            
            messagebox.showinfo("Success", "Patient deleted successfully!")
            self.show_patients()
        
        ViewPatientScreen(
            self.root,
            patient,
            self.logo_image,
            nav_commands,
            on_save,
            on_delete,
            self.show_patients
        )
    
    # Ipakita ang History ng mga operasyon
    def show_history(self):
        self.clear_screen()
        self.current_screen = "history"
        
        nav_commands = self._get_nav_commands()
        
        HistoryScreen(
            self.root,
            self.history,
            self.logo_image,
            nav_commands,
            self.show_add_patient
        )


# Pangunahing function para simulan ang application
def main():
    root = tk.Tk()
    app = PatientRecordSystem(root)
    root.mainloop()


# Simulan ang application kapag na-run ang file
if __name__ == "__main__":
    main()
