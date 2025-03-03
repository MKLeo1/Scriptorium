import os
import json
import customtkinter as ctk

class ScriptListFrame(ctk.CTkFrame):
    
    def __init__(self, parent, scripts_folder, on_script_selected):
        
        """
        :param parent: Parent widget (e.g., main window)
        :param scripts_folder: Path to the folder containing subfolders with scripts
        :param on_script_selected: Function called when a script is selected
        """
        
        super().__init__(parent, corner_radius=0, fg_color="gray20", border_width=0)

        self.pack(side="left", fill="y", padx=0, pady=0)

        self.scripts_folder = scripts_folder
        self.on_script_selected = on_script_selected

        ctk.CTkLabel(self, text="Available Scripts:", font=("Open Sans", 16, "bold")).pack(pady=(10, 5))
        
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.update_scripts()

    # Searches for subfolders containing 'main.py' and returns their names
    def get_scripts(self):
        
        scripts = []
        if not os.path.exists(self.scripts_folder):
            os.makedirs(self.scripts_folder)  # Create folder if it doesn't exist

        for folder in os.listdir(self.scripts_folder):
            folder_path = os.path.join(self.scripts_folder, folder)
            main_script = os.path.join(folder_path, "main.py")

            if os.path.isdir(folder_path) and os.path.exists(main_script):
                scripts.append(folder)  # Store folder name instead of full path

        return scripts

    # Creates buttons for each detected script
    def create_script_buttons(self):
        
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()  # Remove old buttons before update

        for script in self.get_scripts():
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=script,  # Display script folder name
                command=lambda s=script: self.on_script_selected(s),  # Pass folder name
                fg_color="gray30"
            )
            btn.pack(pady=2, fill="x", padx=5)
    
    def update_scripts(self):     
        self.create_script_buttons()
