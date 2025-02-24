import os
import subprocess

class ScriptRunner:
    """Handles execution of scripts."""

    def __init__(self, scripts_folder):
        self.scripts_folder = scripts_folder

    def start_script(self, script_name):
        """Runs the selected script in the background."""
        script_path = os.path.join(self.scripts_folder, script_name, "main.py")
        if not os.path.exists(script_path):
            print("Error: main.py not found in the selected script folder.")
            return

        try:
            # Uruchom skrypt w tle
            subprocess.Popen(["python3", script_path])
            print(f"Started script: {script_name}")
        except Exception as e:
            print(f"Error running script: {e}")