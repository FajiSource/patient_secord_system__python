import tkinter as tk
from typing import Callable


# Class para sa welcome screen
class WelcomeScreen:
    
    # welcome screen
    def __init__(self, parent, on_continue: Callable):
        self.parent = parent
        self.on_continue = on_continue
        self._create_screen()
    
    # Create ng welcome screen interface
    def _create_screen(self):
        container = tk.Frame(self.parent, bg="#f0f4f8")
        container.pack(fill=tk.BOTH, expand=True)
        
        shadow_frame = tk.Frame(container, bg="#d0d0d0", width=650, height=380)
        shadow_frame.pack(expand=True)
        shadow_frame.pack_propagate(False)
        
        white_box = tk.Frame(shadow_frame, bg="white", width=640, height=370, 
                            relief=tk.RAISED, bd=3)
        white_box.pack(padx=5, pady=5)
        white_box.pack_propagate(False)
        
        content_frame = tk.Frame(white_box, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        icon_label = tk.Label(
            content_frame,
            text="🏥",
            font=("Arial", 60),
            bg="white"
        )
        icon_label.pack(pady=(20, 10))
        
        welcome_label = tk.Label(
            content_frame,
            text="Welcome Back!",
            font=("Arial", 24, "bold"),
            fg="#0066cc",
            bg="white"
        )
        welcome_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(
            content_frame,
            text="Ready to manage your patients today?",
            font=("Arial", 14),
            fg="#666666",
            bg="white"
        )
        subtitle_label.pack(pady=(0, 30))
        
        continue_btn = tk.Button(
            content_frame,
            text="CONTINUE",
            font=("Arial", 13, "bold"),
            bg="#0066cc",
            fg="white",
            activebackground="#0052a3",
            activeforeground="white",
            relief=tk.FLAT,
            padx=50,
            pady=12,
            cursor="hand2",
            command=self.on_continue
        )
        continue_btn.pack(pady=10)

