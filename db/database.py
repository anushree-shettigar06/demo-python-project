import psycopg2
from db.config_details import Details


class Database:
    def __init__(self):
        details = Details()
        self.database_name = details.database_name
        self.database_user = details.database_user
        self.database_pwd = details.database_pwd
        self.database_host = details.database_host
        self.database_port = details.database_port
        try:
            self.ps_connection = psycopg2.connect(user=self.database_user,
                                                  password=self.database_pwd,
                                                  host=self.database_host,
                                                  port=self.database_port,
                                                  database=self.database_name)
            self.cursor = self.ps_connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error connecting to the Database")

    def fetch(self, query):
        cursor = self.ps_connection.cursor()
        try:
            cursor.execute(query)
            all_entries = cursor.fetchall()
            return all_entries
        except (Exception, psycopg2.DatabaseError) as error_2:
            print("Error occurred while fetching the data")

    def run_query(self, query, record):
        cursor = self.ps_connection.cursor()
        try:
            cursor.execute(query, record)
            self.ps_connection.commit()
        except (Exception, psycopg2.DatabaseError) as error_3:
            print("Error occurred while inserting the data!", error_3)


