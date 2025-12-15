import tkinter as tk
from typing import List, Callable
from patient import Patient
from utils import format_patient_name


# Class para sa dashboard screen
class DashboardScreen:
    
    # Inisyalisasyon ng dashboard screen
    def __init__(self, parent, patients: List[Patient], history: List[dict],
                 statistics: dict, logo_image, nav_commands: dict):
        self.parent = parent
        self.patients = patients
        self.history = history
        self.statistics = statistics
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self._create_screen()
    
    # Create ng dashboard interface
    def _create_screen(self):
        main_container = tk.Frame(self.parent, bg="white")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        from ui_components import Sidebar
        Sidebar(main_container, self.logo_image, self.nav_commands)
        
        content_area = tk.Frame(main_container, bg="white")
        content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create ng statistics cards
        self._create_statistics_cards(content_area)
        
        # Create ng recent patients section
        self._create_recent_patients(content_area)
    
    # Create ng mga statistics cards
    def _create_statistics_cards(self, parent):
        cards_frame = tk.Frame(parent, bg="white")
        cards_frame.pack(fill=tk.X, pady=(0, 20))
        
        self._create_card(
            cards_frame,
            "#00b8d4",
            "👥",
            str(self.statistics.get('patient_count', 0)),
            "Total Patients"
        )
        
        self._create_card(
            cards_frame,
            "#e91e63",
            "✓",
            str(self.statistics.get("active_patient_count", 0)),
            "Active Patients"
        )
        
        self._create_card(
            cards_frame,
            "#4caf50",
            "📋",
            str(len(self.history)),
            "Recent Visits"
        )
    
    # Create ng isang statistics card
    def _create_card(self, parent, bg_color, icon, value, label):
        card_shadow = tk.Frame(parent, bg="#e0e0e0", width=240, height=160)
        card_shadow.pack(side=tk.LEFT, padx=15, pady=5)
        card_shadow.pack_propagate(False)
        
        card = tk.Frame(card_shadow, bg=bg_color, width=230, height=150, 
                       relief=tk.RAISED, bd=2)
        card.pack(padx=5, pady=5)
        card.pack_propagate(False)
        
        card_content = tk.Frame(card, bg=bg_color)
        card_content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        icon_frame = tk.Frame(card_content, bg=bg_color)
        icon_frame.pack(side=tk.LEFT, padx=(0, 15))
        tk.Label(icon_frame, text=icon, font=("Arial", 40), bg=bg_color, 
                fg="white").pack()
        
        text_frame = tk.Frame(card_content, bg=bg_color)
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(text_frame, text=value, font=("Arial", 36, "bold"), 
                bg=bg_color, fg="white", anchor="w").pack(anchor="w")
        tk.Label(text_frame, text=label, font=("Arial", 12), bg=bg_color, 
                fg="white", anchor="w").pack(anchor="w", pady=(5, 0))
    
    # Create ng recent patients section
    def _create_recent_patients(self, parent):
        recent_container = tk.Frame(parent, bg="white")
        recent_container.pack(fill=tk.BOTH, expand=True)
        
        title_frame = tk.Frame(recent_container, bg="white")
        title_frame.pack(fill=tk.X, pady=(0, 15))
        tk.Label(
            title_frame,
            text="Recent Patients",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#333333"
        ).pack(side=tk.LEFT)
        
        recent_frame = tk.Frame(recent_container, bg="#f5f5f5", relief=tk.SOLID, bd=1)
        recent_frame.pack(fill=tk.BOTH, expand=True)
        
        # Ipakita ang huling 5 na patient
        if self.patients:
            recent_patients = self.patients[-5:] if len(self.patients) > 5 else self.patients
            recent_patients.reverse()
            
            scroll_frame = tk.Frame(recent_frame, bg="#f5f5f5")
            scroll_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            for patient in recent_patients:
                patient_card = tk.Frame(scroll_frame, bg="white", relief=tk.RAISED, bd=1)
                patient_card.pack(fill=tk.X, pady=8, padx=5)
                
                info_frame = tk.Frame(patient_card, bg="white")
                info_frame.pack(fill=tk.X, padx=15, pady=12)
                
                name = format_patient_name(patient)
                
                tk.Label(
                    info_frame,
                    text=name,
                    font=("Arial", 14, "bold"),
                    bg="white",
                    fg="#333333"
                ).pack(side=tk.LEFT)
                
                details = f" • {patient.gender or 'N/A'} • {patient.blood_type or 'N/A'} • {patient.status or 'N/A'}"
                tk.Label(
                    info_frame,
                    text=details,
                    font=("Arial", 11),
                    bg="white",
                    fg="#666666"
                ).pack(side=tk.LEFT, padx=(10, 0))
        else:
            empty_frame = tk.Frame(recent_frame, bg="#f5f5f5")
            empty_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(
                empty_frame,
                text="No patients yet",
                font=("Arial", 14),
                bg="#f5f5f5",
                fg="#999999"
            ).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

