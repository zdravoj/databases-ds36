import sqlite3

# create connection to database
connection = sqlite3.connect('demo_data.sqlite3')


# execute query function
def execute_q(query, conn=connection):
    curs = conn.cursor()
    return curs.execute(query).fetchall()


# modify table function
def modify_table(query, conn=connection):
    curs = conn.cursor()
    curs.execute(query)
    conn.commit()


# table to enter into database
table_data = [
    ['g', 3, 9],
    ['v', 5, 7],
    ['f', 8, 7]
]


# create table query text
CREATE_DEMO_TABLE = '''
    CREATE TABLE IF NOT EXISTS demo (
        "s" VARCHAR(1),
        "x" INT,
        "y" INT
    );
'''


# template text for entering each data row into database
def row_entry_query(s, x, y):
    return f'''
        INSERT INTO demo (
            "s",
            "x",
            "y"
        ) VALUES (
            '{s}', {x}, {y}
        );
    '''


# uses template text to make database entries for each row in data table
def enter_demo_data(table, conn=connection):
    curs = conn.cursor()
    for row in table:
        q = row_entry_query(row[0], row[1], row[2])
        curs.execute(q)
    conn.commit()


# 'row count' query text & execution
ROW_COUNT = '''SELECT COUNT(*) FROM demo'''
row_count = execute_q(ROW_COUNT)

# 'x&y at least 5' query text & execution
XY_AT_LEAST_5 = '''
    SELECT COUNT(*) FROM demo
    WHERE x >= 5
    AND y >= 5
'''
xy_at_least_5 = execute_q(XY_AT_LEAST_5)

# 'unique y' query text & execution
UNIQUE_Y = '''SELECT COUNT(DISTINCT(y)) FROM demo'''
unique_y = execute_q(UNIQUE_Y)

# scripting
if __name__ == '__main__':

    # modify_table(CREATE_DEMO_TABLE)
    # enter_demo_data(table_data)
    # print(row_count)
    # print(xy_at_least_5)
    # print(unique_y)
    print('demo_data.py execution complete')
