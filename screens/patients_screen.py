import tkinter as tk
from tkinter import ttk
from typing import List, Callable
from patient import Patient


# Class para sa patients list screen
class PatientsScreen:
    
    # Inisyalisasyon ng patients screen
    def __init__(self, parent, patients: List[Patient], logo_image, 
                 nav_commands: dict, on_view_patient: Callable, 
                 on_add_patient: Callable):
        self.parent = parent
        self.patients = patients
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self.on_view_patient = on_view_patient
        self.on_add_patient = on_add_patient
        self._create_screen()
    
    # Create ng patients screen interface
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
            text="Patients",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        ).pack(side=tk.LEFT)
        
        # Frame para sa search at add button
        search_frame = tk.Frame(content_area, bg="white", relief=tk.SOLID, bd=1)
        search_frame.pack(fill=tk.X, pady=(0, 15))
        
        search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            bg="#f9f9f9",
            relief=tk.FLAT,
            bd=0,
            insertbackground="#333333"
        )
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=15, pady=12, ipady=5)
        
        add_btn = tk.Button(
            search_frame,
            text="ADD PATIENT",
            font=("Arial", 11, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=25,
            pady=8,
            cursor="hand2",
            command=self.on_add_patient
        )
        add_btn.pack(side=tk.RIGHT, padx=15, pady=8)
        
        table_container = tk.Frame(content_area, bg="white", relief=tk.SOLID, bd=1)
        table_container.pack(fill=tk.BOTH, expand=True)
        
        table_frame = tk.Frame(table_container, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        columns = ("Name", "Birth Date", "Gender", "Contact", "Blood Type", "Status")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Function para mag-filter ng mga patient
        def filter_patients():
            search_query = search_entry.get().lower().strip()
            for item in tree.get_children():
                tree.delete(item)
            
            for patient in self.patients:
                name = f"{patient.first_name} {patient.last_name}".lower()
                full_name = f"{patient.first_name} {patient.middle_name} {patient.last_name}".lower()
                
                matches = (
                    search_query == "" or
                    search_query in name or
                    search_query in full_name or
                    search_query in patient.birth_date.lower() or
                    search_query in patient.gender.lower() or
                    search_query in patient.contact.lower() or
                    search_query in patient.blood_type.lower() or
                    search_query in patient.status.lower() or
                    search_query in patient.address.lower()
                )
                
                if matches:
                    display_name = f"{patient.first_name} {patient.last_name}"
                    tree.insert("", tk.END, values=(
                        display_name,
                        patient.birth_date,
                        patient.gender,
                        patient.contact,
                        patient.blood_type,
                        patient.status
                    ), tags=(str(patient.id),))
        
        search_entry.bind("<KeyRelease>", lambda e: filter_patients())
        search_entry.bind("<Return>", lambda e: filter_patients())
        
        # I-filter ang mga patient sa simula
        filter_patients()
        
        # Function kapag nag-double click sa patient
        def on_double_click(event):
            selection = tree.selection()
            if selection:
                item = tree.item(selection[0])
                patient_id = item["tags"][0] if item["tags"] else None
                if patient_id:
                    patient = next((p for p in self.patients if str(p.id) == str(patient_id)), None)
                    if patient:
                        self.on_view_patient(patient)
        
        tree.bind("<Double-1>", on_double_click)

