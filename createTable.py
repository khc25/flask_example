import psycopg2

conn = psycopg2.connect("dbpostgres://obbyumtp:McdTVFblMMvaFMEgp9FaC44jS7j7ZwX1@suleiman.db.elephantsql.com:5432/obbyumtp")
cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, usernmae varchar, password varchar);")