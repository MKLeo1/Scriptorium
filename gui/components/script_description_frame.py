import os
import subprocess
import customtkinter as ctk
import json

class ScriptDescriptionFrame(ctk.CTkFrame):
    
    def __init__(self, parent, scripts_folder):
        super().__init__(parent, corner_radius=0, fg_color="gray10", border_width=0)
        self.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        self.scripts_folder = scripts_folder
        self.current_script = None
        
        self.title_label = ctk.CTkLabel(self, text="Description", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=(10, 5))
        
        self.description_text = ctk.CTkTextbox(self, wrap="word", width=400, height=300)
        self.description_text.pack(pady=5, padx=5, fill="both", expand=True)
        
        self.start_button = ctk.CTkButton(self, text="Start Script", command=self.start_script, fg_color="blue", hover_color="darkblue")
        self.start_button.pack(pady=10)
    
    def update_details(self, script_name):
       """
       Loads and displays the description for the selected script.
       """
       self.current_script = script_name
       script_folder = os.path.join(self.scripts_folder, script_name)
       description_file = os.path.join(script_folder, "main.json")

       if os.path.exists(description_file):
          with open(description_file, "r", encoding="utf-8") as f:
             try:
                data = json.load(f)
                description = f"Description: {data.get('description', 'Brak opisu')}\n\n"
                description += f"Author: {data.get('author', 'Nieznany')}\n"
                description += f"Created: {data.get('creation_date', 'Brak danych')}\n"
                description += f"Last Modified: {data.get('last_modified', 'Brak danych')}\n"
                description += f"Requirements: {', '.join(data.get('requirements', []))}\n"
                description += f"License: {data.get('license', 'Brak informacji')}\n"
                description += f"Tags: {', '.join(data.get('tags', []))}"
             except json.JSONDecodeError:
                description = "Błąd: Nieprawidłowy format JSON."
       else:
          description = "No description available for this script."

       self.title_label.configure(text=script_name)
    
       self.description_text.configure(state="normal")  # Odblokowanie edycji przed czyszczeniem
       self.description_text.delete("1.0", ctk.END)
       self.description_text.insert(ctk.END, description)
       self.description_text.configure(state="disabled")  # Zablokowanie edycji po wstawieniu tekstu

    
    def start_script(self):
       """
       Runs the selected script's main.py file.
       """
       if self.current_script:
          script_path = os.path.join(self.scripts_folder, self.current_script, "main.py")
          if os.path.exists(script_path):
              subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"python3 {script_path}; exec bash"])
              print(f"Started script: {self.current_script}")
          else:
           print("Error: main.py not found in the selected script folder.")
       else:
           print("No script selected.")