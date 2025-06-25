import customtkinter as ctk
import os
import json

class ScriptDescriptionFrame(ctk.CTkFrame):
    def __init__(self, parent, scripts_folder, script_runner):
        super().__init__(parent, corner_radius=0, fg_color="gray15", border_width=0)
        self.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        
        self.scripts_folder = scripts_folder
        self.script_runner = script_runner
        self.current_script = None

        # GUI Elements
        self.title_label = ctk.CTkLabel(
            self,
            text="Script Description",
            font=("ubuntu", 16, "bold"),
            anchor="center",
            justify="center"
        )
        self.title_label.pack(pady=(10, 5), padx=10, fill="x")

        self.description_text = ctk.CTkTextbox(
            self,
            wrap="word",
            font=("ubuntu", 12),
            state="disabled",
            fg_color="gray20",
            text_color="white",
            border_width=0
        )
        self.description_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Button directly use script_runner
        self.start_button = ctk.CTkButton(
            self, 
            text="START SCRIPT",
            font=("ubuntu", 16), 
            command=self.button_script_execution,
            fg_color="olive drab", 
            hover_color="darkblue"
        )
        self.start_button.pack(pady=10)

################################ Update the description text area with script details #############################

    def update_details(self, script_name):
        self.current_script = script_name
        script_folder = os.path.join(self.scripts_folder, script_name)
        description_file = os.path.join(script_folder, "main.json")

        self.description_text.configure(state="normal") 
        self.description_text.delete("1.0", "end")
        
        if os.path.exists(description_file):

            with open(description_file, "r", encoding="utf-8") as f:
              
                try:

                    data = json.load(f)

                    description = f"Description: {data.get('description', 'No data')}\n\n"

                    description += f"Author: {data.get('author', 'Unknown')}\n"
                    description += f"Created: {data.get('creation_date', 'No data')}\n"
                    description += f"Last Modified: {data.get('last_modified', 'No data')}\n"
                    description += f"Requirements: {', '.join(data.get('requirements', []))}\n"
                    description += f"License: {data.get('license', 'No data')}\n"
                    description += f"Tags: {', '.join(data.get('tags', []))}"
                except json.JSONDecodeError:
 
                    description = "Error: invalid JSON format."
        else:

            description = "No description available for this script."
 
        self.title_label.configure(text=script_name)
        self.description_text.delete("1.0", ctk.END)
        self.description_text.insert(ctk.END, description)

############################### Start script execution via start script button #############################################

    def button_script_execution(self):
        if self.current_script:
            self.script_runner.start_script(self.current_script)