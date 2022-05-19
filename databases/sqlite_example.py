# step 0 - import sqlite
# also move database file into the folder where you're working.
import sqlite3
import queries

# DB Connect Function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# step 1 - connect to the DB
connection = sqlite3.connect('rpg_db.sqlite3')

# Make a cursor and execute query function
def execute_q(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# # step 2 - make the cursor (connection between you and database)
# cursor = connection.cursor()

# # step 3 - write a query
# query = 'SELECT * FROM charactercreator_character;'

# ensure that queries are only being run when
# the file is executed as a script
# # 'python sqlite_example.py'
# if __name__ == '__main__':
#     # step 4 - execute the query on the cursor
#     cursor.execute(query)
#     # step 5 - fetch final results from the cursor
#     results = cursor.fetchall()
#     print(results[:5])

# executing queries using functions
if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, queries.select_all)
    print(results[:5])