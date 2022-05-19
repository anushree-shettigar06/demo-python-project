import hashlib
import psycopg2
from db.config_details import Details
from userinterface.encryption import encrypt_pass, decrypt_pass
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
        main_menu()
    elif user_login is None:
        print("Wrong UserId, Try again!")
        validate_user()
    elif flag == 1:
        print("Wrong Password, Try again!")
        validate_user()
    else:
        validate_user()


def view_all():
    postgresql_select_query = "select * from passmanage"
    try:
        cursor.execute(postgresql_select_query)
        all_entries = cursor.fetchall()
        print("{:<20} {:<25} {:<25}".format('Website', 'UserID', 'Password'))
        for row in all_entries:
            password = decrypt_pass(row[2].encode())
            print("{:<20} {:<25} {:<25}".format(row[0], row[1], password.decode()))
    except (Exception, psycopg2.DatabaseError) as error_2:
        print("Error occurred while fetching the data")


def add_entry():
    new_web = input("Please enter the Website: ")
    new_user = input("Please enter the UserId: ")
    new_pass = input("Please enter the Password: ")
    postgresql_select_query = """INSERT INTO passmanage(Website, UserID, Password) VALUES (%s, %s, %s);"""
    new_pass_enc = encrypt_pass(new_pass).decode()
    insert_values = [(new_web, new_user, new_pass_enc)]
    try:
        for record in insert_values:
            cursor.execute(postgresql_select_query, record)
            ps_connection.commit()
        print("New Entry inserted!!")
    except (Exception, psycopg2.DatabaseError) as error_3:
        # print(error)
        print("Error occurred while inserting the data!", error_3)


def edit_entry():
    view_all()
    new_user = input("Please enter the UserId of the entry you want to edit: ")
    new_web = input("Please enter the Website: ")
    new_user1 = input("Please enter the UserId: ")
    new_pass = input("Please enter the Password: ")
    new_pass_enc = encrypt_pass(new_pass).decode()
    try:
        cursor.execute("""UPDATE public.passmanage SET Website=%s, UserID=%s, Password=%s WHERE UserID = %s""",
                       (new_web, new_user1, new_pass_enc, new_user,))
        ps_connection.commit()
        print("Updated Successfully!!")
    except (Exception, psycopg2.DatabaseError) as error_1:
        # print(error_1)
        print("Error occurred while updating the data!")


def delete_entry():
    view_all()
    new_user = input("Please enter the UserId: ")
    try:
        cursor.execute("""DELETE FROM public.passmanage WHERE UserID = %s""", (new_user,))
        ps_connection.commit()
        print("Entry Deleted!!")
    except (Exception, psycopg2.DatabaseError) as error_2:
        # print(error)
        print("Error occurred while deleting the data!")


def close_db():
    if ps_connection:
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")
