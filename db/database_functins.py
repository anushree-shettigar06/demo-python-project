from userinterface.encryption import encrypt_pass, decrypt_pass


def view_all(ps_connection):
    cursor = ps_connection.cursor()
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


def add_entry(ps_connection):
    cursor = ps_connection.cursor()
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


def edit_entry(ps_connection):
    view_all(ps_connection)
    cursor = ps_connection.cursor()
    new_user_web = input("Please enter the Website of the entry you want to edit: ")
    new_user_id = input("Please enter the UserId of the entry you want to edit: ")
    new_web = input("Please enter the Website: ")
    new_user1 = input("Please enter the UserId: ")
    new_pass = input("Please enter the Password: ")
    new_pass_enc = encrypt_pass(new_pass).decode()
    try:
        cursor.execute("""UPDATE public.passmanage SET Website=%s, UserID=%s, Password=%s WHERE Website = %s AND 
        UserID = %s""",
                       (new_web, new_user1, new_pass_enc, new_user_web, new_user_id,))
        ps_connection.commit()
        print("Updated Successfully!!")
    except (Exception, psycopg2.DatabaseError) as error_1:
        # print(error_1)
        print("Error occurred while updating the data!")


def delete_entry(ps_connection):
    view_all(ps_connection)
    cursor = ps_connection.cursor()
    new_user_web = input("Please enter the Website of the entry you want to delete: ")
    new_user_id = input("Please enter the UserId of the entry you want to delete: ")
    try:
        cursor.execute("""DELETE FROM public.passmanage WHERE Website = %s AND UserID = %s""", (new_user_web, new_user_id,))
        ps_connection.commit()
        print("Entry Deleted!!")
    except (Exception, psycopg2.DatabaseError) as error_2:
        # print(error)
        print("Error occurred while deleting the data!")
