from db.database import Database


def main():
    print("***********************Welcome to Password Manager***********************")
    database = Database()
    database.validate_user()


if __name__ == "__main__":
    main()
