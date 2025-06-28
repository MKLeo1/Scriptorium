import os
import subprocess
import threading
import shlex
import json

class ScriptRunner:

    ############################## Initialize the ScriptRunner with the folder containing scripts #############################
    
    def __init__(self, scripts_folder):
        self.scripts_folder = scripts_folder
        self.status_callback = None
        self.complete_callback = None

    ############################## Set callbacks for status updates and script completion #############################

    def set_callbacks(self, status_callback, complete_callback):
        self.status_callback = status_callback
        self.complete_callback = complete_callback

    ############################## Start script execution in a Linux terminal #############################

    def start_script(self, script_name):
        script_dir = os.path.join(self.scripts_folder, script_name)
        script_path = os.path.join(script_dir, "main.py")
        config_path = os.path.join(script_dir, "main.json")
        
        if not os.path.exists(script_path):
            self._update_status(f"Error: main.py not found in {script_name}")
            return False

        try:
            # Load venv configuration
            venv_python = self._get_venv_python(config_path)
        except Exception as e:
            self._update_status(f"Error loading config: {str(e)}")
            return False

        self._update_status(f"Executing: {script_name}...")
        
        thread = threading.Thread(
            target=self._run_terminal,
            args=(script_path, script_name, venv_python),
            daemon=True
        )
        thread.start()
        return True

    ############################## Run the script in a Linux terminal using GNOME Terminal ############################

    def _run_terminal(self, script_path, script_name, venv_python=None):
        try:
            safe_script_path = shlex.quote(script_path)
            python_cmd = venv_python if venv_python else "python3"
            cmd = ['gnome-terminal', '--', 'bash', '-c', f'{python_cmd} {safe_script_path}; exec bash']
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=self._clean_env(),
                start_new_session=True
            )
            
            try:
                _, stderr = process.communicate(timeout=0.1)
                if process.returncode != 0:
                    error_msg = stderr.decode().strip()
                    print(f"Terminal failed with error: {error_msg}")  # Debug
                    raise subprocess.CalledProcessError(process.returncode, cmd, stderr=stderr)
            except subprocess.TimeoutExpired:
                # Terminal launched successfully and is still running
                self._script_completed(script_name, True)
                return
                
        except Exception as e:
            print(f"Error executing terminal: {str(e)}")  # Debug
            self._script_completed(script_name, False, f"Failed to launch terminal: {str(e)}")

    ############################## Get Python path from virtualenv config #############################

    def _get_venv_python(self, config_path):
        if not os.path.exists(config_path):
            return None

        with open(config_path) as f:
            config = json.load(f)
        
        if "virtualenv" in config and "path" in config["virtualenv"]:
            venv_path = config["virtualenv"]["path"]
            if os.path.exists(venv_path):
                return venv_path
        return None

    ############################## Create a clean environment without Snap variables #############################

    def _clean_env(self):
        env = os.environ.copy()
        snap_vars = [k for k in env if k.startswith(('SNAP_', 'snap'))]
        for var in snap_vars:
            del env[var]
        return env

    ############################## Update status through the callback #############################

    def _update_status(self, message):
        if callable(self.status_callback):
            self.status_callback(message)

    ############################## Handle script completion #############################

    def _script_completed(self, script_name, success, error_msg=None):
        status = "completed successfully" if success else f"failed: {error_msg or 'unknown error'}"
        result = f"Script {script_name} {status}"
        
        if callable(self.complete_callback):
            self.complete_callback(result)
        
        self._update_status(result)