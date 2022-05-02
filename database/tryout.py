import psycopg2
from configdetails import Details
import pandas as pd
import database_1 
from encryption import decrypt_pass

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

postgreSQL_select_Query = "select * from passmanage"
# try:
cursor.execute(postgreSQL_select_Query)
allEnteries = cursor.fetchall()
print ("{:<20} {:<25} {:<25}".format('Website','UserID','Password'))
for row in allEnteries:
    password = decrypt_pass(row[2].encode())
    print ("{:<20} {:<25} {:<25}".format( row[0], row[1], password.decode()))
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error occured while fetching the data", error)