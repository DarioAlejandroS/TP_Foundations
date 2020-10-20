import pandas
import requests
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database

url = 'https://www.stats.govt.nz/assets/Uploads/International-migration/International-migration-June-2020/Download-data/international-migration-June-2020-citizenship-by-visa-by-country-of-last-permanent-residence2.csv'
r = requests.get(url, allow_redirects=True)

open('database.csv', 'w').write(r.content.decode("utf-8"))

db = pandas.read_csv("database.csv", error_bad_lines=False)

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

db_create('postgresql://root:pos@172.18.0.2:5432/db',db,"exo")