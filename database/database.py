import psycopg2

try:
    flag = 0
    ps_connection = psycopg2.connect(user="postgres",
                                     password="postgres1",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="TestDatabase")
    cursor = ps_connection.cursor()

    userId = input("Please enter userId: ")
    passWd = input("Please enter password: ")

    flag = 1
    postgreSQL_select_Query = "select password from users where userid ='"+userId+"'"
    cursor.execute(postgreSQL_select_Query)
    user_login = cursor.fetchone()
    
    if(user_login[0]==passWd):
        print("Welcome")
    else:
        print("Wrong Password")
    print(user_login)

except (Exception, psycopg2.DatabaseError) as error:
    if flag==0:
        print("Error connecting to the Database")
    elif flag==1:
        print("Please enter valid UserId")

finally:
    # closing database connection.
    if ps_connection:
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")