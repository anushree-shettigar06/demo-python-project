import psycopg2
from db.config_details import Details

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
                                     port=database_port)
    
    ps_connection.autocommit = True
    
    cursor = ps_connection.cursor()

    sql = '''CREATE database TestDatabase''';

    # Creating a database

    cursor.execute(sql)
    print("Database created successfully........")
        
    cursor.close()
    ps_connection.close()
    print("PostgreSQL connection is closed")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error connecting to the Database",error)

