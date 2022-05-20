import hashlib
import psycopg2
from db.config_details import Details
from userinterface.view import main_menu

details = Details()
database_name = details.get_database_name()
database_user = details.get_database_user()
database_pwd = details.get_database_password()
database_host = details.get_database_host()
database_port = details.get_database_port()

try:
    ps_connection = psycopg2.connect(user=database_user,
                                     password=database_pwd,
                                     host=database_host,
                                     port=database_port,
                                     database=database_name)
    cursor = ps_connection.cursor()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error connecting to the Database")

flag = 0


def validate_user():
    user_id = input("Please enter userId: ")
    pass_wd = input("Please enter password: ")
    pass_wd = hashlib.sha1(pass_wd.encode()).hexdigest()
    postgresql_select_query = "select password from users where userid ='" + user_id + "'"
    try:
        cursor.execute(postgresql_select_query)
        user_login = cursor.fetchone()
        global flag
        flag = 1
    except (Exception, psycopg2.DatabaseError) as error_1:
        print("Please enter valid UserId")

    if flag == 1 and user_login is not None and user_login[0] == pass_wd:
        print("Welcome")
        main_menu(ps_connection)
    elif user_login is None:
        print("Wrong UserId, Try again!")
        validate_user()
    elif flag == 1:
        print("Wrong Password, Try again!")
        validate_user()
    else:
        validate_user()

