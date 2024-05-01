import psycopg2
from config import load_config
conn = psycopg2.connect(
    host='localhost', 
    dbname='phone_book', 
    user='postgres', 
    password='Фныщ2005'
    )
#List for inserting
name_list = []
category_list = []
number_list = []


# Create a cursor to work with our DB
cur = conn.cursor()
def creating_contact():
    true = True
    while true:
        name = input('Insert the name of new contact: ')
        category = input('Insert the category of new contact: ')
        number = input('Insert the number of new contact: ')
        name_list.append(name)
        category_list.append(category)
        number_list.append(number)
        check = input('Do you want keep adding contacts? True/False ')
        if check == 'True':
            true = True
        elif check == 'False':
            true = False
        else:
            raise Exception('Phonebook cannot understand you, write correctly, instead of {0} you should write True/False'.format(check))
        
def insert_contact(names, categories, numbers):
    for i in range(len(names)):
        cur.execute(f"""SELECT № FROM numbers_data
                    WHERE name = '{names[i]}';""")
        row = cur.fetchone()
        if row:
            cur.execute(f"""UPDATE numbers_data
                    SET number = '{numbers[i]}'
                    WHERE № = '{row[0]}';
            """)
            conn.commit()
        if not row:
            cur.execute(f"""INSERT INTO numbers_data (name, category, number) VALUES
                    ('{names[i]}', '{categories[i]}', '{numbers[i]}');""")
            conn.commit()

def update_contact(id):
    if id !='0':
        to_change = input("""What do you want to change (name/number): """)
        if to_change == "name":
            replacement = input("Input new name: ")
        elif to_change == "number":
            replacement = input("Input new number: ")
        else:
            raise Exception('You cannot change {0}, try another option.'.format(to_change))
        cur.execute(f"""UPDATE numbers_data
                    SET {to_change} = '{replacement}'
                    WHERE № = '{id}';
        """)
        conn.commit()

def show_contact():
    cur.execute("""SELECT №, name, category, number FROM numbers_data""")
    row = cur.fetchone()
    while row is not None:
        print(row)
        row = cur.fetchone()
def delete_contact(id):
    if id!='0':
        to_change = input("""How would you like to find the contact to delete (name/number): """)
        if to_change == "name":
            replacement = input("Person to delete: ")
        elif to_change == "number":
            replacement = input("Number of person to delete: ")
        cur.execute(f"""DELETE FROM numbers_data WHERE {to_change} = '{replacement}';
                    """)
        
def querying_contact(filter):
    config = load_config()
    try: 
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT №, name, category, number FROM numbers_data ORDER BY {filter};""")
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
def searching_q_contact(filter):
    config = load_config()
    try: 
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if filter.isdigit():
                    cur.execute(f"""SELECT №, name, category, number FROM numbers_data 
                                WHERE number = {filter} ;""")
                else:
                    cur.execute(f"""SELECT №, name, category, number FROM numbers_data 
                                WHERE name = '{filter}' ;""")
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)