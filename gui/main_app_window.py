import os
import customtkinter as ctk
from gui.components.script_list_frame import ScriptListFrame
from gui.components.script_description_frame import ScriptDescriptionFrame

class MainAppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scriptorium")
        self.geometry("800x600")

        # dynamically determine the scripts folder (relative to the location of the app.py file)
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Directory, where is app.py (app entry point)
        self.scripts_folder = os.path.join(base_dir,  "..","scripts")  # path to "scripts" directory

        # Left: Script list frame
        self.script_list_frame = ScriptListFrame(self, self.scripts_folder, self.on_script_selected)
        # Right: Script description frame
        self.script_description_frame = ScriptDescriptionFrame(self, self.scripts_folder)

    def on_script_selected(self, script_name):
        self.script_description_frame.update_details(script_name)
