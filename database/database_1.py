import psycopg2
from configdetails import Details

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
    elif user_login==None:
        print("Wrong UserId, Try again!")
        validate_user()
    elif flag==1:
        print("Wrong Password, Try again!")
        validate_user()
    else:
        validate_user()

def view_all():
    pass
def add_entry():
    pass
def edit_entry():
    pass
def delete_entry():
    pass