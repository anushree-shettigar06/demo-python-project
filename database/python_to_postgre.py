import psycopg2
import psycopg2.extras  # when table is large and we need to specify only few columns

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'PASSWORD'
port_id = 5432
conn = None
cur = None
try:
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:  # returns data in dict format  # cursor
            cur.execute('DROP TABLE IF EXISTS employee')
            create_script = ''' CREATE TABLE IF NOT EXISTS employee(
            id int PRIMARY KEY,
            name varchar(40) NOT NULL,
            salary int,
            dept_id varchar(30))'''
            cur.execute(create_script)
            insert_data = 'INSERT INTO employee(id, name, salary, dept_id) VALUES( %s, %s, %s, %s)'
            insert_values = [(1, 'james', 12345, 'cloud tech'), (2, 'millie', 12345, 'cloud tech'),
                             (3, 'John', 12345, 'cloud tech')]
            for record in insert_values:
                cur.execute(insert_data, record)

            # update the data
            update_script = 'UPDATE employee SET salary = salary + (salary*0.5)'
            cur.execute(update_script)

            # delete record from employee
            delete_item = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('james',)
            cur.execute(delete_item, delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'], record['salary'])

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
