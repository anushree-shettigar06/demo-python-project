from db.database import Database
from db.database_functins import DatabaseFunctions


def main():
    print("***********************Welcome to Password Manager***********************")
    database = Database()
    db_func = DatabaseFunctions(database)
    db_func.validate_user()


if __name__ == "__main__":
    main()
