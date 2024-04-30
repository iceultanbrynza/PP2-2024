import psycopg2
scores = []
conn = psycopg2.connect(
    host='localhost', 
    dbname='snake', 
    user='postgres', 
    password='Фныщ2005'
    )
cur = conn.cursor()
cur.execute("""DROP TABLE snake;""")
conn.commit()

cur.execute("""CREATE TABLE snake (
            Username VARCHAR(255),
            Score INTEGER
);
""")
conn.commit()

def insert_data(username, score, cur):
    cur.execute(f"""INSERT INTO snake (Username, Score) VALUES
                ('{username}', {score});""")
def selecting_data(username, scores):
    cur.execute(f"""SELECT Score FROM snake
                WHERE Username = '{username}';""")
    rows = cur.fetchall()
    for row in rows:
        scores.append(row[0])  