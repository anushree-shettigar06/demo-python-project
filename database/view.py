import database_1 
def main_menu():
    print("Main Menu:")
    print("1. View all Enteries")
    print("2. Add an Entry")
    print("3. Update an Entry")
    print("4. Delete an Entry")
    print("5. Exit")
    choice = int(input("Please type the number of your choice as mentioned above: "))
    if choice==1:
        database_1.view_all()
        main_menu()
    elif choice==2:
        database_1.add_entry()
        main_menu()
    elif choice==3:
        database_1.edit_entry()
        main_menu()
    elif choice==4:
        database_1.delete_entry()
        main_menu()
    elif choice==5:
        database_1.close_db()
    else:
        print("Please enter a valid choice!!")
        main_menu()
