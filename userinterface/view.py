from db.database_functins import view_all, add_entry, edit_entry, delete_entry


def main_menu(ps_connection):
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
            view_all(ps_connection)
        elif choice == 2:
            add_entry(ps_connection)
        elif choice == 3:
            edit_entry(ps_connection)
        elif choice == 4:
            delete_entry(ps_connection)
        else:
            print("Please enter a valid choice!!")
    ps_connection.close()
    print("PostgreSQL connection is closed")
