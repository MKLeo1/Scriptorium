import json
import os


class AppConfig:

########################## Initialize the AppConfig with the virtual environment path from config.json #############################

    def __init__(self):
        with open('config.json') as config_file:
            self.venv_path = json.load(config_file)["virtual_environment"]