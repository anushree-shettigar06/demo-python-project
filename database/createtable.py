import psycopg2
from configdetails import Details
from encryption import encrypt_pass
import hashlib

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
                                     port=database_port,
                                     database=database_name)
                                     
    ps_connection.autocommit = True
    cursor = ps_connection.cursor()
    create_script = ''' CREATE TABLE IF NOT EXISTS users(
            userid varchar(40) PRIMARY KEY,
            password varchar(40) NOT NULL)'''

    cursor.execute(create_script)
    insert_data = '''INSERT INTO users(userid, password) VALUES( %s, %s)'''
    insert_values = [('admin', hashlib.sha1("admin1".encode()).hexdigest()), ('master', hashlib.sha1("master1".encode()).hexdigest())]
    for record in insert_values:
        cursor.execute(insert_data, record)
    print("created table users successfully....")

    cursor = ps_connection.cursor()
    create_script = ''' CREATE TABLE IF NOT EXISTS passmanage(
            Website varchar(40) PRIMARY KEY,
            UserID varchar(40) NOT NULL,
            Password varchar(500) NOT NULL)'''

    cursor.execute(create_script)
    pass1 = encrypt_pass('admin1').decode()
    pass2 = encrypt_pass('master1').decode()
    insert_data = '''INSERT INTO passmanage(Website, UserID, Password) VALUES( %s, %s, %s)'''
    insert_values = [('gmail.com','admin', pass1), ('google.com','master', pass2)]
    for record in insert_values:
        cursor.execute(insert_data, record)
    print("created table passmanage successfully....")
    
    cursor.close()
    ps_connection.close()
    print("PostgreSQL connection is closed")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error connecting to the Database",error)

