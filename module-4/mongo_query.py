import pymongo
from os import getenv

# MongoDB connection variables
USER = getenv('MONGO_USER')
PASSWORD = getenv('MONGO_PASSWORD')
DBNAME = getenv('MONGO_DBNAME')
COLLECTION = getenv('MONGO_COLLECTION')

# connect to Mongo database and prepare collections variable
client = pymongo.MongoClient(f'''mongodb+srv://{USER}:{PASSWORD}@ds36-aw.5yffm.mongodb.net/{DBNAME}?retryWrites=true&w=majority''')
db = client[DBNAME]
cllctn = db[COLLECTION]

# -----
# QUERIES
# -----

# returns total characters
    # unnecessary to create a separate function here, but I wanted to keep
        # all of the query functions together in order
def count_docs():
    return cllctn.count_documents({})

# returns count of total items
def count_items_all():
    item_count = 0
    for i in range(302):
        char = cllctn.find()[i]
        char_items = len(char['items'])
        char_weapons = len(char['weapons'])
        item_count += char_items + char_weapons
    return item_count
    
# returns count of items (not including weapons)
def count_items():
    item_count = 0
    for i in range(302):
        char = cllctn.find()[i]
        char_items = len(char['items'])
        item_count += char_items
    return item_count

# returns count of weapons
def count_weapons():
    weapon_count = 0
    for i in range(302):
        char = cllctn.find()[i]
        char_weapons = len(char['weapons'])
        weapon_count += char_weapons
    return weapon_count

# returns list of integers, items per character (including weapons)
def items_per_char():
    count_list = []
    for i in range(302):
        char = cllctn.find()[i]
        char_items = len(char['items'])
        char_weapons = len(char['weapons'])
        items_per = char_items + char_weapons
        count_list.append(items_per)
    return count_list

# returns list of integers, items per character
def weapons_per_char():
    count_list = []
    for i in range(302):
        char = cllctn.find()[i]
        char_weapons = len(char['weapons'])
        count_list.append(char_weapons)
    return count_list

# returns float, average items per character (including weapons)
def average_char_items():
    item_counts = items_per_char()
    return sum(item_counts) / len(item_counts)

# returns float, average weapons per character
def average_char_weapons():
    weapon_counts = weapons_per_char()
    return sum(weapon_counts) / len(weapon_counts)


if __name__ == '__main__':

    # runs all queries
    print(count_docs())
    print(count_items_all())
    print(count_items())
    print(count_weapons())
    print(items_per_char()[:20])
    print(weapons_per_char()[:20])
    print(average_char_items())
    print(average_char_weapons())
