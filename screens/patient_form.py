import tkinter as tk
from tkinter import ttk
from datetime import datetime
from enums import Gender, PatientStatus, BloodType

# check kung available ang calendar
try:
    from tkcalendar import DateEntry
    CALENDAR_AVAILABLE = True
except ImportError:
    CALENDAR_AVAILABLE = False


# Class para sa patient form
class PatientForm:
    
    # Inisyalisasyon ng patient form
    def __init__(self, parent, patient=None):
        self.parent = parent
        self.patient = patient
        self.form_frame = None
        self.entries = {}
        self.allergies_list = []
        self.allergies_text = None
        self._create_form()
    
    # Create ng form fields
    def _create_form(self):
        self.form_frame = tk.Frame(self.parent, bg="white")
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        # Unang row: Pangalan
        row1 = tk.Frame(self.form_frame, bg="white")
        row1.pack(fill=tk.X, pady=12)
        
        self._create_entry_field(row1, "First Name", "first_name", 
                                self.patient.first_name if self.patient else "")
        self._create_entry_field(row1, "Last Name", "last_name", 
                                self.patient.last_name if self.patient else "")
        self._create_entry_field(row1, "Middle Name", "middle_name", 
                                self.patient.middle_name if self.patient else "")
        
        # Ikalawang row: Birth date, Gender, Contact
        row2 = tk.Frame(self.form_frame, bg="white")
        row2.pack(fill=tk.X, pady=12)
        
        self._create_birth_date_field(row2)
        self._create_combobox_field(row2, "Gender", "gender", 
                                   [g.value for g in Gender],
                                   self.patient.gender if self.patient else "")
        self._create_entry_field(row2, "Contact", "contact", 
                                self.patient.contact if self.patient else "")
        
        # Ikatlong row: Address
        row3 = tk.Frame(self.form_frame, bg="white")
        row3.pack(fill=tk.X, pady=12)
        
        self._create_entry_field(row3, "Address", "address", 
                                self.patient.address if self.patient else "")
        
        # Ikaapat na row: Blood Type, Status
        row4 = tk.Frame(self.form_frame, bg="white")
        row4.pack(fill=tk.X, pady=12)
        
        self._create_combobox_field(row4, "Blood Type", "blood_type", 
                                   [bt.value for bt in BloodType],
                                   self.patient.blood_type if self.patient else "")
        self._create_combobox_field(row4, "Status", "status", 
                                   [ps.value for ps in PatientStatus],
                                   self.patient.status if self.patient else "")
        
        # Ikalimang row: Allergies
        row5 = tk.Frame(self.form_frame, bg="white")
        row5.pack(fill=tk.X, pady=12)
        
        tk.Label(row5, text="Allergies", font=("Arial", 11, "bold"), 
                bg="white", fg="#333333").pack(side=tk.LEFT, padx=5)
        
        allergies_entry = tk.Entry(row5, font=("Arial", 11), bg="#f9f9f9", 
                                   relief=tk.FLAT, bd=1, insertbackground="#333333")
        allergies_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=6)
        
        # I-load ang existing allergies kung may patient
        self.allergies_list = (self.patient.allergies.copy() 
                              if self.patient and isinstance(self.patient.allergies, list) 
                              else [])
        
        # Function para magdagdag ng allergy
        def add_allergy():
            allergy = allergies_entry.get().strip()
            if allergy:
                self.allergies_list.append(allergy)
                allergies_entry.delete(0, tk.END)
                self._update_allergies_display()
        
        add_allergy_btn = tk.Button(
            row5,
            text="ADD",
            font=("Arial", 10, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=20,
            pady=6,
            cursor="hand2",
            command=add_allergy
        )
        add_allergy_btn.pack(side=tk.LEFT, padx=5)
        
        # Text area para ipakita ang listahan ng allergies
        self.allergies_text = tk.Text(
            self.form_frame,
            font=("Arial", 11),
            bg="#f9f9f9",
            relief=tk.FLAT,
            bd=1,
            height=8,
            wrap=tk.WORD,
            insertbackground="#333333"
        )
        self.allergies_text.pack(fill=tk.BOTH, expand=True, pady=12)
        self._update_allergies_display()
    
    # Create ng entry field
    def _create_entry_field(self, parent, label_text, key, default_value=""):
        tk.Label(parent, text=label_text, font=("Arial", 11, "bold"), 
                bg="white", fg="#333333").pack(side=tk.LEFT, padx=5)
        
        entry = tk.Entry(parent, font=("Arial", 11), bg="#f9f9f9", 
                        relief=tk.FLAT, bd=1, insertbackground="#333333")
        if default_value:
            entry.insert(0, default_value)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=6)
        
        self.entries[key] = entry
    
    # Create ng birth date field (may calendar kung available)
    def _create_birth_date_field(self, parent):
        tk.Label(parent, text="Birth Date", font=("Arial", 11, "bold"), 
                bg="white", fg="#333333").pack(side=tk.LEFT, padx=5)
        
        if CALENDAR_AVAILABLE:
            birth_date_entry = DateEntry(
                parent,
                width=12,
                background='#0066cc',
                foreground='white',
                borderwidth=1,
                date_pattern='mm/dd/yyyy',
                font=("Arial", 11)
            )
            if self.patient and self.patient.birth_date:
                try:
                    birth_date_str = self.patient.birth_date
                    if "/" in birth_date_str:
                        parts = birth_date_str.split("/")
                        if len(parts) == 3:
                            month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
                            birth_date_entry.set_date(datetime(year, month, day))
                except:
                    pass
            birth_date_entry.pack(side=tk.LEFT, padx=5, ipady=6)
        else:
            birth_date_entry = tk.Entry(parent, font=("Arial", 11), bg="#f9f9f9", 
                                       relief=tk.FLAT, bd=1, insertbackground="#333333")
            if self.patient and self.patient.birth_date:
                birth_date_entry.insert(0, self.patient.birth_date)
            else:
                birth_date_entry.insert(0, "MM/DD/YYYY")
            birth_date_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=6)
        
        self.entries["birth_date"] = birth_date_entry
    
    # Create ng combobox field
    def _create_combobox_field(self, parent, label_text, key, values, default_value=""):
        tk.Label(parent, text=label_text, font=("Arial", 11, "bold"), 
                bg="white", fg="#333333").pack(side=tk.LEFT, padx=5)
        
        combobox = ttk.Combobox(parent, font=("Arial", 11), values=values, 
                               state="readonly", width=17)
        if default_value:
            combobox.set(default_value)
        combobox.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=6)
        
        self.entries[key] = combobox
    
    # I-update ang display ng allergies
    def _update_allergies_display(self):
        if self.allergies_text:
            self.allergies_text.delete("1.0", tk.END)
            if self.allergies_list:
                self.allergies_text.insert("1.0", "\n".join(self.allergies_list))
                self.allergies_text.config(fg="black")
            else:
                self.allergies_text.insert("1.0", "List existing allergies here")
                self.allergies_text.config(fg="#666666")
    
    # Kunin ang birth date mula sa form
    def get_birth_date(self) -> str:
        birth_date_entry = self.entries.get("birth_date")
        if CALENDAR_AVAILABLE and hasattr(birth_date_entry, 'get_date'):
            try:
                date_obj = birth_date_entry.get_date()
                return date_obj.strftime("%m/%d/%Y")
            except:
                return ""
        else:
            birth_date_str = birth_date_entry.get()
            if birth_date_str == "MM/DD/YYYY":
                return ""
            return birth_date_str
    
    # Kunin ang lahat ng data mula sa form
    def get_form_data(self) -> dict:
        return {
            "first_name": self.entries["first_name"].get(),
            "last_name": self.entries["last_name"].get(),
            "middle_name": self.entries["middle_name"].get(),
            "birth_date": self.get_birth_date(),
            "gender": self.entries["gender"].get(),
            "contact": self.entries["contact"].get(),
            "address": self.entries["address"].get(),
            "blood_type": self.entries["blood_type"].get(),
            "status": self.entries["status"].get(),
            "allergies": self.allergies_list
        }
    
    # I-enable o i-disable ang form fields
    def set_enabled(self, enabled: bool):
        state = tk.NORMAL if enabled else tk.DISABLED
        combobox_state = "readonly" if enabled else "disabled"
        
        for key, widget in self.entries.items():
            if isinstance(widget, ttk.Combobox):
                widget.config(state=combobox_state)
            else:
                widget.config(state=state)
        
        if self.allergies_text:
            self.allergies_text.config(state=state)

