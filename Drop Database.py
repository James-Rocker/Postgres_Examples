import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("""DROP DATABASE income""")
conn.close()