import os
import subprocess
import threading
import shlex

class ScriptRunner:

    ##############################Initialize the ScriptRunner with the folder containing scripts.#############################
    
    def __init__(self, scripts_folder):

        self.scripts_folder = scripts_folder
        self.status_callback = None
        self.complete_callback = None

    ##############################Set callbacks for status updates and script completion.#############################

    def set_callbacks(self, status_callback, complete_callback):
        self.status_callback = status_callback
        self.complete_callback = complete_callback

    ##############################Start script execution in a Linux terminal.#############################

    def start_script(self, script_name):
        script_path = os.path.join(self.scripts_folder, script_name, "main.py")
        
        if not os.path.exists(script_path):
            self._update_status(f"Error: main.py not found in {script_name}")
            return False

        self._update_status(f"Executing: {script_name}...")
        
        thread = threading.Thread(target=self._run_linux, args=(script_path, script_name), daemon=True)
        thread.start()
        return True

    ##############################Run the script in a Linux terminal using GNOME Terminal.#############################

    def _run_linux(self, script_path, script_name):
        try:
            safe_script_path = shlex.quote(script_path)
            cmd = ['gnome-terminal', '--', 'bash', '-c', f'python3 {safe_script_path}; exec bash']
            print(f"Executing command: {' '.join(cmd)}")  # Debug output
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=self._clean_env(),
                start_new_session=True
            )
            
            # Wait briefly to check if terminal launched
            try:
                _, stderr = process.communicate(timeout=0.5)
                if process.returncode != 0:
                    error_msg = stderr.decode().strip()
                    print(f"Terminal failed with error: {error_msg}")  # Debug
                    raise subprocess.CalledProcessError(process.returncode, cmd, stderr=stderr)
            except subprocess.TimeoutExpired:
                # Terminal launched successfully and is still running
                print("Terminal launched successfully")  # Debug
                self._script_completed(script_name, True)
                return
                
        except Exception as e:
            print(f"Error executing terminal: {str(e)}")  # Debug
            self._script_completed(script_name, False, f"Failed to launch terminal: {str(e)}")

    ##############################Create a clean environment without Snap variables.#############################

    def _clean_env(self):
        env = os.environ.copy()
        snap_vars = [k for k in env if k.startswith(('SNAP_', 'snap'))]
        for var in snap_vars:
            del env[var]
        return env

    ##############################Update status through the callback.#############################

    def _update_status(self, message):
        if callable(self.status_callback):
            self.status_callback(message)

    ##############################Handle script completion.#############################

    def _script_completed(self, script_name, success, error_msg=None):
        status = "completed successfully" if success else f"failed: {error_msg or 'unknown error'}"
        result = f"Script {script_name} {status}"
        
        if callable(self.complete_callback):
            self.complete_callback(result)
        
        self._update_status(result)