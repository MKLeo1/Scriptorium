import customtkinter as ctk
from gui.components.script_list_frame import ScriptListFrame
from gui.components.script_description_frame import ScriptDescriptionFrame


class MainAppWindow(ctk.CTk):

     def __init__(self, scripts_folder="scripts"):
        
        super().__init__()
        self.title("Scriptorium")
        self.geometry("800x600")
        self.scripts_folder = scripts_folder

        # Left: Script list frame
        self.script_list_frame = ScriptListFrame(self, self.scripts_folder, self.on_script_selected)
        # Right: Script description frame
        self.script_description_frame = ScriptDescriptionFrame(self)

     def on_script_selected(self, script_name):
        self.script_description_frame.update_description(script_name, self.scripts_folder)
