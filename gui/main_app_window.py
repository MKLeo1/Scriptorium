import customtkinter as ctk
from gui.components.script_list_frame import ScriptListFrame


class MainAppWindow(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Scriptorium")
        self.geometry("800x600")

        # Create scripts list frame
        self.script_frame = ScriptListFrame(self, "scripts", self.on_script_selected)
        self.script_frame.pack(side="left", fill="y")
        # Create right frame
        self.main_content = ctk.CTkFrame(self)
        self.main_content.pack(side="right", fill="both", expand=True)

    def on_script_selected(self, script_name):
        print(f"Chosen script: {script_name}")