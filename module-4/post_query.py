import psycopg2
import titanic_queries
from os import getenv

# PostgreSQL connection variables
DBNAME = getenv('ELEPHANT_DBNAME')
USER = getenv('ELEPHANT_USER')
PASSWORD = getenv('ELEPHANT_PASSWORD')
HOST = getenv('ELEPHANT_HOST')

# connection and cursor for database
pg_conn = psycopg2.connect(dbname=DBNAME, 
                            user=USER, 
                            password=PASSWORD, 
                            host=HOST)
# pg_curs = pg_conn.cursor()

# execute query function
def execute_q(query):
    curs = pg_conn.cursor()
    result = curs.execute(query)
    return result.fetchall()


if __name__ == '__main__':
    for q in titanic_queries.QUERY_LIST:
        print(execute_q(q))