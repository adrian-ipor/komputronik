import os
import yaml
from yaml import SafeLoader


class ConfigurationParser:

    def __init__(self):
        self.config_path = 'configuration/config.yml'

    def get_config(self) -> dict:
        if os.path.isfile(self.config_path):
            with open(self.config_path) as conf:
                data = yaml.load(conf, Loader=SafeLoader)
            return data
        else:
            print(f"No such file {self.config_path}")
            exit(2)
