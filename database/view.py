from database_1 import view_all, edit_entry, delete_entry
def main_menu():
    print("Main Menu:")
    print("1. View all Enteries")
    print("2. Add an Entry")
    print("3. Edit an Entry")
    print("4. Delete an Entry")
    print("5. Exit")
    choice = int(input("Please type the number of your choice as mentioned above: "))
    if choice==1:
        view_all()
    elif choice==2:
        add_entry()
    elif choice==3:
        edit_entry()
    elif choice==4:
        delete_entry()
    elif choice==5:
        return
    else:
        print("Please enter a valid choice!!")
        main_menu()
