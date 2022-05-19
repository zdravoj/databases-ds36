import sqlite3
import pymongo

from itertools import groupby
from collections import OrderedDict

USER = 'austinjw'
PASSWORD = 'VHDTrvyb5ht7jxAO'
DBNAME = 'rpg_data'

# creates MongoDB connection
def create_mdb_conn(user, password, dbname, collection_name):
    client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@ds36-aw.5yffm.mongodb.net/{dbname}?retryWrites=true&w=majority')
    db = client[dbname]
    collection = db[collection_name]
    return db

# creates connection to SQLite database
def create_sl_conn(source_db='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(source_db)
    return sl_conn

# executes query
def execute_query(curs, query):
    return curs.execute(query).fetchall()


# gets characters and values
GET_CHARACTERS = '''
    SELECT *
    FROM charactercreator_character
'''

# gets item name by character_id
GET_ITEM_NAMES = '''
    SELECT cchar.character_id, arm.name
    FROM charactercreator_character AS cchar
    LEFT JOIN charactercreator_character_inventory AS inv
    ON cchar.character_id = inv.character_id
    LEFT JOIN armory_item AS arm
    ON inv.item_id = arm.item_id
'''

# gets weapon name by character_id
GET_WEAPON_NAMES = '''
    SELECT cchar.character_id, arm.name
    FROM charactercreator_character as cchar
    LEFT JOIN charactercreator_character_inventory AS inv
    ON cchar.character_id = inv.character_id
    LEFT JOIN armory_item AS arm
    ON inv.item_id = arm.item_id
    INNER JOIN armory_weapon as weap
    ON arm.item_id = weap.item_ptr_id
'''




# scripting
if __name__ == '__main__':
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    weap_arr = execute_query(sl_curs, GET_WEAPON_NAMES)
    weap_dict = dict()
    for key, val in groupby(sorted(list(weap_arr), 
                            key = lambda ele: ele[0]), 
                            key = lambda ele: ele[0]):
        weap_dict[key] = [ele[1] for ele in val]

    chars_w_weap = [weap_arr[i][0] for i in range(len(weap_arr))]
    chars_w_weap = list(set(chars_w_weap))

    char_arr = execute_query(sl_curs, GET_CHARACTERS)
    char_ids = [char_arr[i][0] for i in range(len(char_arr))]
    chars_wo_weap = char_ids

    for i in chars_w_weap:
        chars_wo_weap.remove(i)
    
    item_arr = execute_query(sl_curs, GET_ITEM_NAMES)
    item_dict = dict()
    for key, val in groupby(sorted(list(item_arr), 
                            key = lambda ele: ele[0]), 
                            key = lambda ele: ele[0]):
        item_dict[key] = [ele[1] for ele in val]

    for i in range(1, 302):
        if i not in weap_dict.keys():
            weap_dict[i] = []
    # od = OrderedDict(sorted(weap_dict.items()))
    # weap_dict_ord = {}
    # for k, v in od.items():
    #     weap_dict_ord[k] = v
    weap_dict_ord = dict(sorted(weap_dict.items()))

    # print(chars_wo_weap)
    # print(chars_w_weap)
    print(item_dict)
    print(weap_dict_ord)