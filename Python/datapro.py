import pandas
import requests
import csv, re
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets'
r = requests.get(url, allow_redirects=True)

orig = r.content

# Split the long string into a list of lines
data = orig.decode('utf-8').splitlines()

# Open the file for writing
with open("database.csv", "w") as csv_file:
# Create the writer object with tab delimiter
    writer = csv.writer(csv_file, delimiter = '\t')
    for line in data:
        # Writerow() needs a list of data to be written, so split at all empty spaces in the line
        writer.writerow(re.split('\s+',line))
        
db = pandas.read_csv("database.csv")

db = db.rename(columns={"dec": "deci"})

def db_create(engine_url, dataframe, table_name):
    """
    Check if postgres db exists, if not creates it
    """
    engine = create_engine(engine_url)
    if not database_exists(engine.url):
        print("Database does not exist, creating...")
        create_database(engine.url)
    print("Does it exist now?", database_exists(engine.url))
    if database_exists(engine.url):
        data_type = table_name
        print('Populating database with', data_type)
        dataframe.to_sql(data_type, engine)
#db_create('postgresql://root:pos@localhost:5432/db',db,"exo")
db_create('postgresql://root:pos@172.18.0.2:5432/db',db,"exo")