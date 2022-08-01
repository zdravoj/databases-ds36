import pandas as pd
import psycopg2
from os import getenv

# PostgreSQL Connection Credentials
DBNAME = getenv('ELEPHANT_DBNAME')
USER = getenv('ELEPHANT_USER')
PASSWORD = getenv('ELEPHANT_PASSWORD')
HOST = getenv('ELEPHANT_HOST')

# Establish connection and cursor
pg_conn = psycopg2.connect(dbname=DBNAME,
                           user=USER,
                           password=PASSWORD,
                           host=HOST)
pg_curs = pg_conn.cursor()

# csv to pandas
df = pd.read_csv('https://raw.githubusercontent.com/bloominstituteoftechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
# replace single quote characters within name
df['Name'] = df['Name'].str.replace("'", "")
# to numpy array
t_tab = df.to_numpy()

# modify or create table in PostgreSQL
def modify_table(curs, conn, query):
    curs.execute(query)
    conn.commit()

# create titanic_table query
CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic_table (
    "passenger_id" SERIAL NOT NULL PRIMARY KEY,
    "survived" INT NOT NULL,
    "pclass" INT NOT NULL,
    "name" VARCHAR(85) NOT NULL,
    "sex" VARCHAR(6) NOT NULL,
    "age" INT NOT NULL,
    "siblings/spouses aboard" INT NOT NULL,
    "parents/children aboard" INT NOT NULL,
    "fare" FLOAT NOT NULL
    );
'''

modify_table(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

# populate titanic_table query
for passenger in t_tab:
    pg_curs.execute(
        f'''
            INSERT INTO titanic_table (
                "survived",
                "pclass",
                "name",
                "sex",
                "age",
                "siblings/spouses aboard",
                "parents/children aboard",
                "fare"
            )
            VALUES (
                {passenger[0]},
                {passenger[1]},
                '{passenger[2]}',
                '{passenger[3]}',
                {passenger[4]},
                {passenger[5]},
                {passenger[6]},
                {passenger[7]}
            );
        '''
    )
pg_conn.commit()

if __name__ == '__main__':
    print('completed without python errors')