import os
import customtkinter as ctk
from components.script_list_frame import ScriptListFrame
from components.script_description_frame import ScriptDescriptionFrame
from components.script_runner import ScriptRunner

class MainAppWindow(ctk.CTk):    
    def __init__(self):
        super().__init__()
        self.title("Scriptorium")
        self.geometry("800x600")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.scripts_folder = os.path.join(base_dir, "..", "scripts")
        
        self.script_runner = ScriptRunner(self.scripts_folder)
        
        self.script_list_frame = ScriptListFrame(
            self, 
            self.scripts_folder, 
            self.on_script_selected
        )
        
        self.script_description_frame = ScriptDescriptionFrame(
            self,
            self.scripts_folder, 
            self.script_runner   
        )

    def on_script_selected(self, script_name):
        self.script_description_frame.update_details(script_name)