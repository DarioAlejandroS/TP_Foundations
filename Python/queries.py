import pandas
import psycopg2

conn = psycopg2.connect(
    host="172.18.0.2",
    database="db",
    user="root",
    password="pos")
    
cur = conn.cursor()
    
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

cur = conn.cursor()
cur.execute("SELECT * FROM exo")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")

# close the communication with the PostgreSQL
cur.close()