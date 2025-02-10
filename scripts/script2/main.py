import os
import subprocess

def start_script(self):
    """
    Opens a new terminal window and runs the selected script.
    """
    if self.current_script:
        script_path = os.path.join(self.scripts_folder, self.current_script, "main.py")

        if os.path.exists(script_path):
            subprocess.Popen(["gnome-terminal", "--", "python3", script_path])
            print(f"Started script in new terminal: {self.current_script}")
        else:
            print("Error: main.py not found in the selected script folder.")
    else:
        print("No script selected.")
