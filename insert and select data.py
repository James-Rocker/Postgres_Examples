import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("""CREATE TABLE notes(id integer PRIMARY KEY, head text, body text)""")
cur.execute("INSERT INTO notes VALUES (1, 'some head text', 'some body text')")
cur.execute("SELECT * FROM notes;")
rows = cur.fetchall()
print(rows)
