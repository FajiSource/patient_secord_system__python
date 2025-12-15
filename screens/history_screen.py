import tkinter as tk
from tkinter import ttk
from typing import List, Callable


# Class para sa history screen
class HistoryScreen:
    
    # Inisyalisasyon ng history screen
    def __init__(self, parent, history: List[dict], logo_image, 
                 nav_commands: dict, on_add_patient: Callable):
        self.parent = parent
        self.history = history
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self.on_add_patient = on_add_patient
        self._create_screen()
    
    # Create ng history screen interface
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
            text="History",
            font=("Arial", 20, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        ).pack(side=tk.LEFT)
        
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
        
        columns = ("Action", "Patient", "Date")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=300)
        
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Function para mag-filter ng Create
        def filter_history():
            search_query = search_entry.get().lower().strip()
            for item in tree.get_children():
                tree.delete(item)
            
            for record in reversed(self.history):
                action = record.get("action", "").lower()
                patient = record.get("patient", "").lower()
                date = record.get("date", "").lower()
                
                matches = (
                    search_query == "" or
                    search_query in action or
                    search_query in patient or
                    search_query in date
                )
                
                if matches:
                    tree.insert("", tk.END, values=(
                        record.get("action", ""),
                        record.get("patient", ""),
                        record.get("date", "")
                    ))
        
        search_entry.bind("<KeyRelease>", lambda e: filter_history())
        search_entry.bind("<Return>", lambda e: filter_history())
        
        # I-filter ang Create sa simula
        filter_history()

