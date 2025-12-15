import tkinter as tk
from tkinter import messagebox
from typing import Callable
from patient import Patient
from .patient_form import PatientForm


# Class para sa add patient screen
class AddPatientScreen:
    
    # Inisyalisasyon ng add patient screen
    def __init__(self, parent, logo_image, nav_commands: dict,
                 on_save: Callable, on_cancel: Callable):
        self.parent = parent
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.form = None
        self._create_screen()
    
    # Create ng add patient screen interface
    def _create_screen(self):
        main_container = tk.Frame(self.parent, bg="white")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        from ui_components import Sidebar
        Sidebar(main_container, self.logo_image, self.nav_commands)
        
        content_area = tk.Frame(main_container, bg="#f5f5f5")
        content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_frame = tk.Frame(content_area, bg="#f5f5f5")
        title_frame.pack(fill=tk.X, pady=(0, 15))
        tk.Label(
            title_frame,
            text="Add New Patient",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        ).pack(side=tk.LEFT)
        
        form_container = tk.Frame(content_area, bg="white", relief=tk.SOLID, bd=1)
        form_container.pack(fill=tk.BOTH, expand=True)
        
        self.form = PatientForm(form_container)
        
        button_frame = tk.Frame(self.form.form_frame, bg="white")
        button_frame.pack(fill=tk.X, pady=20)
        
        # Function para i-save ang bagong patient
        def save_patient():
            form_data = self.form.get_form_data()
            patient = Patient(
                id=0,
                **form_data
            )
            self.on_save(patient)
        
        add_btn = tk.Button(
            button_frame,
            text="ADD PATIENT",
            font=("Arial", 11, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=40,
            pady=10,
            cursor="hand2",
            command=save_patient
        )
        add_btn.pack(side=tk.RIGHT)

