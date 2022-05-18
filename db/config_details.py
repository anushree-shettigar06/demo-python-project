import configparser
import yaml

# # config=configparser.RawConfigParser()
# # config.read('D:\projectsss\demo-python-project\db\configuration_properties.yaml')


with open("db/configuration_properties.yaml", "r") as configfile:
    config = yaml.safe_load(configfile)

class Details:
    def __init__(self):
        self.database_name=config['DB_DETAILS']['DB_NAME']
        self.database_user=config['DB_DETAILS']['USER_NAME']
        self.database_pwd=config['DB_DETAILS']['PASSWORD']
        self.database_host=config['DB_DETAILS']['HOST']
        self.database_port=config['DB_DETAILS']['PORT']

    def get_database_name(self):
        return self.database_name
    
    def get_database_user(self):
        return self.database_user

    def get_database_password(self):
        return self.database_pwd
  
    def get_database_host(self):
        return self.database_host

    def get_database_port(self):
        return self.database_port