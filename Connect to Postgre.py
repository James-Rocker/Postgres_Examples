import psycopg2

try:
    conn = psycopg2.connect(dbname="postgre", user="user", host="127.0.0.1",
                            password="test", port="5432")
    cur = conn.cursor()
    cur.execute("CREATE DATABASE %s  ;" % "Dummy db")
    print(cur.get_dsn_parameters(), "\n")
    # closing database connection.
    cur.close()
    conn.close()
    print("PostgreSQL connection is closed")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
