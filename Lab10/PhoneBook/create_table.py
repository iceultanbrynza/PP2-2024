import psycopg2
from config import load_config
from functions import *
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book', 
    user='postgres', 
    password='Фныщ2005'
    )



# Create a cursor to work with our DB
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

#inserting data using console
creating_contact()
insert_contact(name_list, category_list, number_list)

#inserting data using csv file
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

#updating data
id = input("""Do you want to make changes(0 if no)?
What is the id of the contact: """)
update_contact(id)
show_contact()
#deleting data
id = input("""Do you want to delete any contact(0 if no)?
What is the id of the contact: """)
delete_contact(id)
show_contact()
#querying data
filter = input("""Are you in search of some contact?
Set up filter(№/name/category/number): """)
querying_contact(filter)

cur.close()
conn.close()
