# U3S2M1 Queries

# TOTAL_CHARACTERS: 302, Datatype: Integer
TOTAL_CHARACTERS = '''
    SELECT COUNT(*)
    FROM charactercreator_character;
'''

# TOTAL_SUBCLASS: 11, Datatype: Integer
TOTAL_NECROMANCERS = '''
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
'''

# TOTAL_ITEMS: 174, Datatype: Integer
TOTAL_ITEMS = '''
    SELECT COUNT(*)
    FROM armory_item;
'''

# total items existing (by character inventory)
# TOTAL_ITEMS: 898, Datatype: Integer
# TOTAL_ITEMS = '''
#     SELECT COUNT(*)
#     FROM charactercreator_character_inventory;
# '''

# TOTAL_WEAPONS: 37, Datatype: Integer
TOTAL_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_weapon;
'''

# total weapons existing (by character inventory)
# WEAPONS: 203, Datatype: Integer
# WEAPONS = '''
#     SELECT COUNT(*)
#     FROM charactercreator_character_inventory
#     LEFT JOIN armory_item
#     ON armory_item.item_id = 
#       charactercreator_character_inventory.item_id
#     LEFT JOIN armory_weapon
#     ON armory_weapon.item_ptr_id = armory_item.item_id
#     WHERE armory_weapon.item_ptr_id IS NOT NULL;
# '''

# NON_WEAPONS: 137, Datatype: Integer
NON_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_item
    LEFT JOIN armory_weapon
    ON armory_item.item_id = armory_weapon.item_ptr_id
    WHERE armory_weapon.item_ptr_id IS NULL;
'''

# total non-weapons existing (by character inventory)
# NON_WEAPONS: 695, Datatype: Integer
# NON_WEAPONS = '''
#     SELECT COUNT(*)
#     FROM charactercreator_character_inventory
#     LEFT JOIN armory_item
#     ON armory_item.item_id = 
#       charactercreator_character_inventory.item_id
#     LEFT JOIN armory_weapon
#     ON armory_weapon.item_ptr_id = armory_item.item_id
#     WHERE armory_weapon.item_ptr_id IS NULL;
# '''

# CHARACTER_ITEMS: N/A (table) Datatype: Integer Table
CHARACTER_ITEMS = '''
    SELECT character_id, COUNT(*)
    FROM charactercreator_character_inventory
    GROUP BY character_id
    LIMIT 20;
'''

# CHARACTER_WEAPONS: N/A (table), Datatype: Integer Table
CHARACTER_WEAPONS = '''
    SELECT character_id, COUNT(armory_weapon.item_ptr_id)
    FROM armory_item
    INNER JOIN armory_weapon
    ON armory_item.item_id = armory_weapon.item_ptr_id
    INNER JOIN charactercreator_character_inventory as cc_inv
    ON armory_item.item_id = cc_inv.item_id
    GROUP BY character_id
    LIMIT 20;
'''

# AVG_CHARACTER_ITEMS: 2.974, Datatype: Float
AVG_CHARACTER_ITEMS = '''
    SELECT AVG(item_count)
    FROM
    (SELECT COUNT(*) AS item_count
    FROM charactercreator_character_inventory
    LEFT JOIN armory_item
    ON armory_item.item_id = 
        charactercreator_character_inventory.item_id
    GROUP BY character_id
    );
'''

# AVG_CHARACTER_WEAPONS: 1.412, Datatype: Float
# does not account for characters with no weapons!
AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(weapon_count)
    FROM
    (SELECT COUNT(*) AS weapon_count
    FROM charactercreator_character_inventory
    LEFT JOIN armory_item
    ON armory_item.item_id = 
    charactercreator_character_inventory.item_id
    LEFT JOIN armory_weapon
    ON armory_weapon.item_ptr_id = armory_item.item_id
    GROUP BY character_id
    HAVING armory_weapon.item_ptr_id
    );
'''

# get character table
GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'

# create new table test_table with id, name, age
CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
        ("id" SERIAL NOT NULL PRIMARY KEY, 
        "name" VARCHAR(200) NOT NULL,
        "age" INT NOT NULL,
        "country_of_origin" VARCHAR(200) NOT NULL);
'''

# insert values into test_table
INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Austin Wood', 26, 'United States');
'''

# drop test_table
DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table;
'''

GET_TEST_TABLE = '''
    SELECT * FROM test_table;
'''

CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
'''

INSERT_AUSTIN = '''INSERT INTO characters (
    "name",
    "level",
    "exp",
    "hp",
    "strength",
    "intelligence",
    "dexterity",
    "wisdom"
    )
    VALUES ('Austin Wood', 3, 75, 9, 2, 7, 4, 5);
'''

DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS characters;
'''