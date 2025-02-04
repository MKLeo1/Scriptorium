import os
import customtkinter as ctk

# class that displays a list of scripts automatically loaded from a folder.

class ScriptListFrame(ctk.CTkFrame):
    def __init__(self, parent, scripts_folder, on_script_selected):
    
        """
          :param parent: Parent (e.g., main window)  
          :param scripts_folder: Path to the folder containing .py files  
          :param on_script_selected: Function called when a script is selected 
        """
        super().__init__(parent, corner_radius=0, fg_color="gray20", border_width=0)
        self.pack(side="left", fill="y", padx=0, pady=0) 

        self.scripts_folder = scripts_folder
        self.on_script_selected = on_script_selected

        ctk.CTkLabel(self, text="Avalible scripts:", font=("Arial", 16, "bold")).pack(pady=(10, 5))

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.update_scripts()
    def get_scripts(self):
        # Looking files .py in scripts folder and return name list
        if not os.path.exists(self.scripts_folder):
            os.makedirs(self.scripts_folder)  # Create directory if not exist
        return [f for f in os.listdir(self.scripts_folder) if f.endswith(".py")]

    def create_script_buttons(self):
        # Create buttons for all scripts
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()  # Delete old buttons before update

        for script in self.get_scripts():
            btn = ctk.CTkButton(
                self.buttons_frame, text=script, 
                command=lambda s=script: self.on_script_selected(s),
                fg_color="gray30"
            )
            btn.pack(pady=2, fill="x", padx=5)

    def update_scripts(self):
        self.create_script_buttons()
