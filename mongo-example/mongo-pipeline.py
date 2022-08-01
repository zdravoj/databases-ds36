import pymongo
import sqlite3
from os import getenv

# MongoDB connection variables
USER = getenv('MONGO_USER')
PASSWORD = getenv('MONGO_PASSWORD')
DBNAME = getenv('MONGO_DBNAME')
COLLECTION = getenv('MONGO_COLLECTION')

# create connection to MongoDB database
def create_mdb_connection(user, password, dbname):
    client = pymongo.MongoClient(f'''mongodb+srv://{user}:{password}@ds36-aw.5yffm.mongodb.net/{dbname}?retryWrites=true&w=majority''')
    return client

# create connection to SQLite
def create_sl_connection(dbname='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(dbname)
    return sl_conn

# execute query function
def execute_query(curs, query):
    return curs.execute(query).fetchall()

# creates and adds documents to MongoDB database
def doc_creation(db, sl_curs, character_table, item_table, weapon_table):
    weapons = execute_query(sl_curs, weapon_table)
    characters = execute_query(sl_curs, character_table)
    for character in characters:
        item_character_query = item_table.format("\'%s\'" % character[1])
        item_names = execute_query(sl_curs, item_character_query)
        weapon_names = []
        for item in item_names:
            if item in weapons:
                weapon_names.append(item[0])
        
        document = {
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8],
            'items': item_names,
            'weapons': weapon_names
        }

        db.insert_one(document)

# returns documents from MongoDB database (for printing in script)
def show_all(db):
    all_docs = list(db.find())
    return all_docs

GET_CHARACTER_TABLE = '''
    SELECT *
    FROM charactercreator_character;
'''

GET_ITEM_TABLE = '''
    SELECT arm.name as item_name
    FROM (
        SELECT *
        FROM charactercreator_character AS cchar
        INNER JOIN charactercreator_character_inventory AS inv
        ON cchar.character_id = inv.character_id
        ) as char_ci
    INNER JOIN armory_item AS arm
    WHERE arm.item_id = char_ci.item_id
    AND char_ci.name = {};
'''

GET_WEAPON_TABLE = '''
    SELECT arm.name
    FROM charactercreator_character AS cchar
    INNER JOIN charactercreator_character_inventory AS inv
    ON cchar.character_id = inv.character_id
    INNER JOIN armory_item AS arm
    ON arm.item_id = inv.item_id
    INNER JOIN armory_weapon AS weap
    ON arm.item_id = weap.item_ptr_id
'''

if __name__ == '__main__':
    sl_conn = create_sl_connection()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(USER, PASSWORD, DBNAME)
    
    col = client['rpg_data']
    db = col['characters']
    db.drop({})
    doc_creation(db, sl_curs, GET_CHARACTER_TABLE, GET_ITEM_TABLE, GET_WEAPON_TABLE)

    print(show_all(db))