import hashlib
import psycopg2
from db.config_details import Details
from userinterface.view import main_menu


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
        postgresql_select_query = query
        try:
            cursor.execute(postgresql_select_query)
            all_entries = cursor.fetchall()
            return all_entries
        except (Exception, psycopg2.DatabaseError) as error_2:
            print("Error occurred while fetching the data")

    def validate_user(self):
        flag = 0
        valid_flag = 0
        while valid_flag == 0:
            user_id = input("Please enter userId: ")
            pass_wd = input("Please enter password: ")
            pass_wd = hashlib.sha1(pass_wd.encode()).hexdigest()
            postgresql_select_query = "select password from users where userid ='" + user_id + "'"
            try:
                self.cursor.execute(postgresql_select_query)
                user_login = self.cursor.fetchone()
                flag = 1
            except (Exception, psycopg2.DatabaseError) as error_1:
                print("Please enter valid UserId")

            if flag == 1 and user_login is not None and user_login[0] == pass_wd:
                print("Welcome")
                main_menu(self)
                valid_flag = 1
            elif user_login is None:
                print("Wrong UserId, Try again!")
                continue
            elif flag == 1:
                print("Wrong Password, Try again!")
                continue
            else:
                continue
