import configparser
import yaml

with open("C:/Users/Hari Priya/Desktop/pythondemo/demo-python-project/db/configuration_properties.yaml", "r") as configfile:
    config = yaml.safe_load(configfile)


class Details:
    def __init__(self):
        self.database_name = config['DB_DETAILS']['DB_NAME']
        self.database_user = config['DB_DETAILS']['USER_NAME']
        self.database_pwd = config['DB_DETAILS']['PASSWORD']
        self.database_host = config['DB_DETAILS']['HOST']
        self.database_port = config['DB_DETAILS']['PORT']
