import pandas as pd
import sqlite3

buddymove = pd.read_csv('buddymove_holidayiq.csv')

connection = sqlite3.connect("buddymove_holidayiq.sqlite3")

buddymove.to_sql('review', con=connection)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

if __name__ == '__main__':
    print(f'Database shape is: {buddymove.shape}')
    print(f'Total null values: {buddymove.isnull().sum().sum()}')
    # count of rows
    print(execute_q(connection, 'SELECT COUNT(*) FROM review'))
    # count of users who reviewed >= 100 in both nature and shopping categories
    print(execute_q(connection, '''SELECT COUNT(*)
                                   FROM review
                                   WHERE Nature >= 100 AND Shopping >= 100'''))
    # average reviews in each category
    print(execute_q(connection, '''SELECT AVG(Sports), 
                                        AVG(Religious), 
                                        AVG(Nature), 
                                        AVG(Theatre), 
                                        AVG(Shopping), 
                                        AVG(Picnic)
                                   FROM review'''))