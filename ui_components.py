import tkinter as tk
from typing import Callable, Optional
import os
from PIL import Image, ImageTk


class Sidebar:
    
    def __init__(self, parent, logo_image: Optional[tk.PhotoImage], 
                 nav_commands: dict[str, Callable]):
        self.parent = parent
        self.logo_image = logo_image
        self.nav_commands = nav_commands
        self._create_sidebar()
    
    def _create_sidebar(self):
        sidebar = tk.Frame(self.parent, bg="#f5f5f5", width=220, relief=tk.RAISED, bd=1)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        logo_frame = tk.Frame(sidebar, bg="#ffffff", height=100, relief=tk.FLAT)
        logo_frame.pack(fill=tk.X, pady=0)
        logo_frame.pack_propagate(False)
        
        if self.logo_image:
            logo_label = tk.Label(logo_frame, image=self.logo_image, bg="#ffffff")
            logo_label.pack(expand=True, pady=15)
        else:
            logo_canvas = tk.Canvas(logo_frame, width=60, height=60, bg="#ffffff", highlightthickness=0)
            logo_canvas.pack(expand=True, pady=15)
            logo_canvas.create_oval(5, 5, 55, 55, fill="#00cc66", outline="#00cc66")
            logo_canvas.create_text(30, 30, text="+", font=("Arial", 30, "bold"), fill="white")
        
        nav_container = tk.Frame(sidebar, bg="#f5f5f5")
        nav_container.pack(fill=tk.BOTH, expand=True, pady=10)
        
        for text, command in self.nav_commands.items():
            btn = tk.Button(
                nav_container,
                text=text,
                font=("Arial", 12),
                bg="#0066cc",
                fg="white",
                activebackground="#0052a3",
                activeforeground="white",
                relief=tk.FLAT,
                anchor=tk.W,
                padx=25,
                pady=18,
                cursor="hand2",
                command=command
            )
            btn.pack(fill=tk.X, padx=15, pady=3)
        
        return sidebar


class LogoLoader:
    
    @staticmethod
    def load_logo(logo_path: str = None) -> Optional[tk.PhotoImage]:
        if logo_path is None:
            logo_path = os.path.join("assets", "logo.png")
        
        try:
            if os.path.exists(logo_path):
                img = Image.open(logo_path)
                img = img.resize((60, 60), Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Could not load logo: {e}")
        return None


class FormField:
    
    @staticmethod
    def create_labeled_entry(parent, label_text: str, default_value: str = "", 
                            row_frame: tk.Frame = None) -> tuple[tk.Label, tk.Entry]:
        if row_frame is None:
            row_frame = tk.Frame(parent, bg="white")
            row_frame.pack(fill=tk.X, pady=12)
        
        label = tk.Label(row_frame, text=label_text, font=("Arial", 11, "bold"), 
                        bg="white", fg="#333333")
        label.pack(side=tk.LEFT, padx=5)
        
        entry = tk.Entry(row_frame, font=("Arial", 11), bg="#f9f9f9", 
                        relief=tk.FLAT, bd=1, insertbackground="#333333")
        if default_value:
            entry.insert(0, default_value)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipady=6)
        
        return label, entry

