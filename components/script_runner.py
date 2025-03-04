import os
import subprocess
import threading

class ScriptRunner:
    
    def __init__(self, scripts_folder):
        
        self.scripts_folder = scripts_folder
        self.status_callback = None  # Callback status update GUI
        self.complete_callback = None  # Callback after completed script run

    def set_callbacks(self, status_callback, complete_callback):

        self.status_callback = status_callback
        self.complete_callback = complete_callback

    def start_script(self, script_name):
        script_path = os.path.join(self.scripts_folder, script_name, "main.py")
        if not os.path.exists(script_path):
            print("Error: main.py not found in the selected script folder.")
            return

        if self.status_callback:
            self.status_callback(f"Uruchamianie: {script_name}...")

        def run_process():
            try:    # pkexec responsible for sudo password authentication
                process = subprocess.Popen(["pkexec", "python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.wait() 
                
                success = process.returncode == 0
                self._script_completed(script_name, success)
            except Exception as e:
                print(f"Error running script: {e}")
                self._script_completed(script_name, False)

        threading.Thread(target=run_process, daemon=True).start()

    def _script_completed(self, script_name, success):
        result_text = f"Skrypt {script_name} zakończony pomyślnie!" if success else f"Skrypt {script_name} zakończony z błędami."
        if self.status_callback:
            self.status_callback(result_text)
        if self.complete_callback:
            self.complete_callback(result_text)
