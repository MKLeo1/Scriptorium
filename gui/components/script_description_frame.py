import os
import customtkinter as ctk

# class that displays automatically loaded script description from a specific script folder.
class ScriptDescriptionFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="gray10", border_width=0)
        # Place the frame on the right side, filling the remaining space
        self.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.title_label = ctk.CTkLabel(self, text="", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=(10, 5))

        self.description_text = ctk.CTkTextbox(self, wrap="word", width=400, height=300)
        self.description_text.pack(pady=5, padx=5, fill="both", expand=True)

        # "Start Script" button
        self.start_button = ctk.CTkButton(self, text="Start Script", command=self.start_script, fg_color="blue", hover_color="darkblue")
        self.start_button.pack(pady=10)

        self.current_script = None

    def update_details(self, script_name, scripts_folder):
        """
        Loads and displays the description for the selected script.
        Assumes the description is stored in a file with the same name as the script but with a .description extension.
        """
        self.current_script = script_name
        base_name = os.path.splitext(script_name)[0]
        description_file = os.path.join(scripts_folder, f"{base_name}.description")
        if os.path.exists(description_file):
            with open(description_file, "r", encoding="utf-8") as f:
                description = f.read()
        else:
            description = "No description available for this script."
        self.title_label.configure(text=script_name)
        self.description_text.delete("1.0", ctk.END)
        self.description_text.insert(ctk.END, description)

    def start_script(self):
        """Placeholder function to start the selected script."""
        if self.current_script:
            print(f"Starting script: {self.current_script}")
            # Add your script execution logic here (e.g., using subprocess)
        else:
            print("No script selected.")
