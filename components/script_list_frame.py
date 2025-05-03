import os
import customtkinter as ctk

class ScriptListFrame(ctk.CTkFrame):

    ############################## Initialize the ScriptListFrame with the parent and scripts folder #############################

    def __init__(self, parent, scripts_folder, on_script_selected):
        
        # parent: Parent widget
        # scripts_folder: Path to scripts directory
        # on_script_selected: Callback when script is selected
        
        super().__init__(parent, corner_radius=0, fg_color="gray20", border_width=0)
        self.pack(side="left", fill="y", padx=0, pady=0)

        self.scripts_folder = scripts_folder
        self.on_script_selected = on_script_selected

        # GUI Elements
        self.title_label = ctk.CTkLabel(
            self, 
            text="Available Scripts:", 
            font=("ubuntu", 16, "bold")
        )
        self.title_label.pack(pady=(10, 5))
        
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.update_scripts()

    ##############################S can the scripts folder and return valid script directories #############################

    def get_scripts(self):
        scripts = []
        
        # Create scripts folder if it doesn't exist
        if not os.path.exists(self.scripts_folder):
            os.makedirs(self.scripts_folder, exist_ok=True)
            return scripts

        for folder in os.listdir(self.scripts_folder):
            folder_path = os.path.join(self.scripts_folder, folder)
            main_script = os.path.join(folder_path, "main.py")

            # Only include folders with main.py
            if os.path.isdir(folder_path) and os.path.exists(main_script):
                scripts.append(folder)

        return sorted(scripts)  # Return alphabetically sorted

    ############################## Create buttons for each available script #############################

    def create_script_buttons(self):
        
        # Clear existing buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Create new buttons
        for script in self.get_scripts():
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=script,
                command=lambda s=script: self.on_script_selected(s),
                fg_color="gray30",
                hover_color="gray25",
                anchor="w",
                corner_radius=5,
                height=35
            )
            btn.pack(pady=2, fill="x", padx=5)
    
    ############################## Refresh the list of scripts #############################

    def update_scripts(self):
        self.create_script_buttons()