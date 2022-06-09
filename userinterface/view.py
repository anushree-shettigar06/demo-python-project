
def main_menu(db_func_obj):
    choice = 0
    while choice != 5:
        print("Main Menu:")
        print("1. View all Entries")
        print("2. Add an Entry")
        print("3. Update an Entry")
        print("4. Delete an Entry")
        print("5. Exit")
        choice = int(input("Please type the number of your choice as mentioned above: "))
        if choice == 1:
            db_func_obj.view_all()
        elif choice == 2:
            db_func_obj.add_entry()
        elif choice == 3:
            db_func_obj.edit_entry()
        elif choice == 4:
            db_func_obj.delete_entry()
        else:
            print("Please enter a valid choice!!")
    db_func_obj.database_obj.ps_connection.close()
    print("PostgreSQL connection is closed")
