import psycopg2
from config import load_config

conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book', 
    user='postgres', 
    password='Фныщ2005'
    )
cur = conn.cursor()
cur.execute("""DROP TABLE numbers_data;""")
conn.commit()
cur.execute("""CREATE TABLE numbers_data (
            № SERIAL PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(255),
            number VARCHAR(20)
);
""")
conn.commit()

import csv
filename = 'phones.csv'
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, category, number = row
        cur.execute(f"""INSERT INTO numbers_data (name, category, number) VALUES 
                    ('{name}', '{category}', '{number}');
        """)

        conn.commit()

def get_data(name):
    """ Get parts provided by a vendor specified by the vendor_id """
    parts = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_name', (name,))
                
                # process the result set
                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts
def add_contact(name, category, number):
    """ Add a new part """
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL add_new_contact(%s,%s,%s)', (name, category, number))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def add_contacts(names, categories, numbers):
    """ Add a new part """
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL add_new_contacts(%s,%s,%s)', (names, categories, numbers))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    parts = get_data("Damir")
    add_contact('Ernar', 'Friend', '2411414')
    add_contacts(['Father', 'Mother', 'Milena'], ['Family', 'Family', 'Friend'], ['24244', '242424', '242452'])
    print(parts)