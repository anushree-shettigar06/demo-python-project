import psycopg2
from configdetails import Details
import pandas as pd
import database_1 

details= Details()
database_name=details.get_database_name()
database_user=details.get_database_user()
database_pwd=details.get_database_password()
database_host=details.get_database_host()
database_port=details.get_database_port()

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
    userId = input("Please enter userId: ")
    passWd = input("Please enter password: ")

    postgreSQL_select_Query = "select password from users where userid ='"+userId+"'"
    try:
        cursor.execute(postgreSQL_select_Query)
        user_login = cursor.fetchone()
        global flag
        flag = 1
    except (Exception, psycopg2.DatabaseError) as error:
        print("Please enter valid UserId")
validate_user()

def delete_entry():
    database_1.view_all()
    newUser = input("Please enter the UserId: ")
    try:
        print(cursor.execute("""DELETE FROM public.passmanage WHERE "UserID" = %s""", (newUser,)))
        ps_connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        # print("Error occured while deleting the data!")

delete_entry()