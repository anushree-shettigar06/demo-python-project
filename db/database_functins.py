from userinterface.encryption import encrypt_pass, decrypt_pass
import hashlib
from userinterface.view import main_menu


class DatabaseFunctions:

    def __init__(self, database_obj):
        self.database_obj = database_obj

    def validate_user(self):
        valid_flag = 0
        while valid_flag == 0:
            user_id = input("Please enter userId: ")
            pass_wd = input("Please enter password: ")
            pass_wd = hashlib.sha1(pass_wd.encode()).hexdigest()
            postgresql_select_query = "select password from users where userid ='" + user_id + "'"
            user_login = self.database_obj.fetch(postgresql_select_query)
            if user_login is not None and user_login[0][0] == pass_wd:
                print("Welcome")
                main_menu(self)
                valid_flag = 1
            elif user_login is None:
                print("Wrong UserId or Password, Please try again!")
                continue
            else:
                continue

    def view_all(self):
        postgresql_select_query = "select * from passmanage"
        all_entries = self.database_obj.fetch(postgresql_select_query)
        print("{:<20} {:<25} {:<25}".format('Website', 'UserID', 'Password'))
        for row in all_entries:
            password = decrypt_pass(row[2].encode())
            print("{:<20} {:<25} {:<25}".format(row[0], row[1], password.decode()))

    def add_entry(self):
        new_web = input("Please enter the Website: ")
        new_user = input("Please enter the UserId: ")
        new_pass = input("Please enter the Password: ")
        postgresql_select_query = """INSERT INTO passmanage(Website, UserID, Password) VALUES (%s, %s, %s);"""
        new_pass_enc = encrypt_pass(new_pass).decode()
        insert_values = [(new_web, new_user, new_pass_enc)]
        for record in insert_values:
            self.database_obj.run_query(postgresql_select_query, record)
        print("New Entry inserted!!")

    def edit_entry(self):
        self.view_all()
        new_user_web = input("Please enter the Website of the entry you want to edit: ")
        new_user_id = input("Please enter the UserId of the entry you want to edit: ")
        new_web = input("Please enter the Website: ")
        new_user1 = input("Please enter the UserId: ")
        new_pass = input("Please enter the Password: ")
        new_pass_enc = encrypt_pass(new_pass).decode()
        self.database_obj.run_query("""UPDATE public.passmanage SET Website=%s, UserID=%s, Password=%s WHERE Website = %s AND 
        UserID = %s""", (new_web, new_user1, new_pass_enc, new_user_web, new_user_id,))
        print("Updated Successfully!!")

    def delete_entry(self):
        self.view_all()
        new_user_web = input("Please enter the Website of the entry you want to delete: ")
        new_user_id = input("Please enter the UserId of the entry you want to delete: ")
        self.database_obj.run_query("""DELETE FROM public.passmanage WHERE Website = %s AND UserID = %s""",
                               (new_user_web, new_user_id,))
        print("Entry Deleted!!")
