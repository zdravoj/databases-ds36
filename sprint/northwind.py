import sqlite3

# establish connection with database
connection = sqlite3.connect('northwind_small.sqlite3')


# execute query function
def execute_q(query, conn=connection):
    curs = conn.cursor()
    return curs.execute(query).fetchall()


# prints all tables in the database
def view_available_tables():
    print(execute_q(
        '''
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            ORDER BY name;
        '''
    ))


# prints schema of the selected table
def view_schema(table_name):
    print(execute_q(
        f'''
            SELECT sql
            FROM sqlite_master
            WHERE name="{table_name}";
        '''
    ))


# -----
# QUERIES
# -----

'''returns: 10 most expensive items by unit price (all columns)'''
expensive_items = '''
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

'''returns: average age at hire for all employees'''
avg_hire_age = '''
    SELECT AVG(age_at_hire) FROM
        (SELECT HireDate - BirthDate AS age_at_hire
        FROM Employee)
'''

'''returns: product name, unit price, and supplier for 10
   most expensive products in database
'''
ten_most_expensive = '''
    SELECT ProductName, UnitPrice, CompanyName FROM Product
    JOIN Supplier
    ON Product.SupplierId = Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10
'''

'''returns: largest category by distinct products'''
largest_category = '''
    SELECT CategoryName, num FROM (
        SELECT CategoryName, COUNT(*) as num
        FROM Product
        JOIN Category
        ON Product.CategoryId = Category.Id
        GROUP BY Category.Id
        )
    ORDER BY num DESC
    LIMIT 1
'''

if __name__ == '__main__':

    # view_available_tables()
    # view_schema('Supplier')
    # print(execute_q(expensive_items))
    # print(execute_q(avg_hire_age))
    # print(execute_q(ten_most_expensive))
    # print(execute_q(largest_category))
    print('northwind.py execution complete')
