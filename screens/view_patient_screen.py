import tkinter as tk
from tkinter import messagebox
from typing import Callable
from patient import Patient
from .patient_form import PatientForm
from utils import format_patient_name


# Class para sa view patient screen
class ViewPatientScreen:
    
    # Inisyalisasyon ng view patient screen
    def __init__(self, parent, patient: Patient, logo_image, nav_commands: dict,
                 on_save: Callable, on_delete: Callable, on_cancel: Callable):
        self.parent = parent
        self.patient = patient
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self.on_save = on_save
        self.on_delete = on_delete
        self.on_cancel = on_cancel
        self.form = None
        self.edit_mode = False
        self._create_screen()
    
    # Create ng view patient screen interface
    def _create_screen(self):
        main_container = tk.Frame(self.parent, bg="white")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        from ui_components import Sidebar
        Sidebar(main_container, self.logo_image, self.nav_commands)
        
        content_area = tk.Frame(main_container, bg="#f5f5f5")
        content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_frame = tk.Frame(content_area, bg="#f5f5f5")
        title_frame.pack(fill=tk.X, pady=(0, 15))
        patient_name = format_patient_name(self.patient)
        tk.Label(
            title_frame,
            text=f"View Patient: {patient_name}",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        ).pack(side=tk.LEFT)
        
        form_container = tk.Frame(content_area, bg="white", relief=tk.SOLID, bd=1)
        form_container.pack(fill=tk.BOTH, expand=True)
        
        self.form = PatientForm(form_container, patient=self.patient)
        
        # I-disable ang form sa simula (view mode)
        self.form.set_enabled(False)
        
        button_frame = tk.Frame(self.form.form_frame, bg="white")
        button_frame.pack(fill=tk.X, pady=20)
        
        # Function para i-toggle ang edit mode
        def toggle_edit():
            self.edit_mode = not self.edit_mode
            self.form.set_enabled(self.edit_mode)
        
        # Function para i-save ang updated na patient
        def save_patient():
            if not self.edit_mode:
                toggle_edit()
                return
            
            form_data = self.form.get_form_data()
            self.patient.first_name = form_data["first_name"]
            self.patient.last_name = form_data["last_name"]
            self.patient.middle_name = form_data["middle_name"]
            self.patient.birth_date = form_data["birth_date"]
            self.patient.gender = form_data["gender"]
            self.patient.contact = form_data["contact"]
            self.patient.address = form_data["address"]
            self.patient.blood_type = form_data["blood_type"]
            self.patient.status = form_data["status"]
            self.patient.allergies = form_data["allergies"]
            
            self.on_save(self.patient)
            toggle_edit()
        
        # Function para tanggalin ang patient
        def delete_patient():
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this patient?"):
                self.on_delete()
        
        save_btn = tk.Button(
            button_frame,
            text="SAVE",
            font=("Arial", 11, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            command=save_patient
        )
        save_btn.pack(side=tk.RIGHT, padx=5)
        
        delete_btn = tk.Button(
            button_frame,
            text="DELETE",
            font=("Arial", 11, "bold"),
            bg="#cc0000",
            fg="white",
            activebackground="#990000",
            activeforeground="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            command=delete_patient
        )
        delete_btn.pack(side=tk.RIGHT, padx=5)
        
        edit_btn = tk.Button(
            button_frame,
            text="EDIT",
            font=("Arial", 11, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor="hand2",
            command=toggle_edit
        )
        edit_btn.pack(side=tk.RIGHT, padx=5)

