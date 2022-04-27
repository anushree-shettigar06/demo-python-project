import psycopg2
from configdetails import Details
from view import main_menu
import pandas as pd

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

    if(flag==1 and user_login != None and user_login[0]==passWd):
        print("Welcome")
        main_menu()
    elif user_login==None:
        print("Wrong UserId, Try again!")
        validate_user()
    elif flag==1:
        print("Wrong Password, Try again!")
        validate_user()
    else:
        validate_user()

def view_all():
    postgreSQL_select_Query = "select * from passmanage"
    try:
        cursor.execute(postgreSQL_select_Query)
        allEnteries = cursor.fetchall()
        print ("{:<20} {:<25} {:<25}".format('Website','UserID','Password'))
        for row in allEnteries:
            print ("{:<20} {:<25} {:<25}".format( row[0], row[1], row[2]))
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error occured while fetching the data")

def add_entry():
    newWeb = input("Please enter the Website: ")
    newUser = input("Please enter the UserId: ")
    newPass = input("Please enter the Password: ")
    postgreSQL_select_Query = """INSERT INTO passmanage(Website, UserID, Password) VALUES (%s, %s, %s);"""
    insert_values = [(newWeb,newUser,newPass)]
    try:
        for record in insert_values:
            cursor.execute(postgreSQL_select_Query, record)
            ps_connection.commit()
        print("New Entry inserted!!")
    except (Exception, psycopg2.DatabaseError) as error:
        # print(error)
        print("Error occured while inserting the data!",error)

def edit_entry():
    view_all()
    newUser = input("Please enter the UserIdof the entry you want to edit: ")
    newWeb = input("Please enter the Website: ")
    newUser1 = input("Please enter the UserId: ")
    newPass = input("Please enter the Password: ")
    try:
        cursor.execute("""UPDATE public.passmanage SET Website=%s, UserID=%s, Password=%s WHERE UserID = %s""", (newWeb, newUser1, newPass, newUser,))
        ps_connection.commit()
        print("Updated Successfully!!")
    except (Exception, psycopg2.DatabaseError) as error:
        # print(error)
        print("Error occured while updating the data!")

def delete_entry():
    view_all()
    newUser = input("Please enter the UserId: ")
    try:
        cursor.execute("""DELETE FROM public.passmanage WHERE UserID = %s""", (newUser,))
        ps_connection.commit()
        print("Entry Deleted!!")
    except (Exception, psycopg2.DatabaseError) as error:
        # print(error)
        print("Error occured while deleting the data!")

def close_db():
    if ps_connection:
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")