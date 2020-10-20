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

db_version = cur.fetchone()
print(db_version)

cur = conn.cursor()
cur.execute("SELECT * FROM exo")
rows = cur.fetchall()
df = pd.DataFrame(rows, columns =['year_month', 'month_of_release', 'passenger_type', 'direction', 'citizenship', 'visa', 
'country_of_residence', 'estimate', 'standard_error', 'status'])

print("Operation done successfully")

cur.close()