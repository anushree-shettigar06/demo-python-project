import configparser

config=configparser.RawConfigParser()
config.read('demo-python-project\properties\config.properties')

class Details:
    def __init__(self):
        self.database_name=config.get('DB_DETAILS','DB_NAME')
        self.database_user=config.get('DB_DETAILS','USER_NAME')
        self.database_pwd=config.get('DB_DETAILS','PASSWORD')
        self.database_host=config.get('DB_DETAILS','HOST')
        self.database_port=config.get('DB_DETAILS','PORT')

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