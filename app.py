#!/usr/bin/env python3

import os
import sys
from components.app_config import AppConfig

############################## Ensure the script is running in the correct virtual environment #############################

def ensure_venv(config: AppConfig): 
    if sys.executable != config.venv_path:  
        os.execv(config.venv_path, [config.venv_path] + sys.argv)
 
def main():
    try:
        config = AppConfig()  # Load configuration
        ensure_venv(config)   # Check virtual environment
        
        from components.main_app_window import MainAppWindow
        app = MainAppWindow()  # Initialize the main application window
        app.mainloop()
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()