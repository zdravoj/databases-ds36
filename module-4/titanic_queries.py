# titanic PostgreSQL database queries

SURVIVED = '''
    SELECT survived, COUNT(*) FROM titanic_table
    GROUP BY survived;
'''
PASSENGERS_BY_CLASS = '''
    SELECT pclass AS passenger_class, COUNT(*) FROM titanic_table
    GROUP BY pclass;
'''

SURVIVED_BY_CLASS = '''
    SELECT survived, pclass, COUNT(*) FROM titanic_table
    GROUP BY survived, pclass;
'''

AVG_AGE_BY_SURVIVAL = '''
    SELECT survived, AVG(age) AS average_age FROM titanic_table
    GROUP BY survived;
'''

AVG_AGE_BY_PCLASS = '''
    SELECT pclass, AVG(age) AS average_age FROM titanic_table
    GROUP BY pclass;
'''

AVG_FARE_BY_PCLASS = '''
    SELECT pclass, AVG(fare) AS average_fare FROM titanic_table
    GROUP BY pclass;
'''

AVG_FARE_BY_SURVIVAL = '''
    SELECT survived, AVG(fare) AS average_fare FROM titanic_table
    GROUP BY survived;
'''

AVG_SIB_SP_BY_PCLASS = '''
    SELECT pclass, AVG("siblings/spouses aboard") FROM titanic_table
    GROUP BY pclass;
'''

AVG_SIB_SP_BY_SURVIVAL = '''
    SELECT survived, AVG("siblings/spouses aboard") FROM titanic_table
    GROUP BY survived;
'''

AVG_PAR_CH_BY_PCLASS = '''
    SELECT pclass, AVG("parents/children aboard") FROM titanic_table
    GROUP BY pclass;
'''

AVG_PAR_CH_BY_SURVIVAL = '''
    SELECT survived, AVG("parents/children aboard") FROM titanic_table
    GROUP BY survived;
'''

PASSENGERS_WITH_SAME_NAME = '''
    SELECT * FROM (
        SELECT name, COUNT(*) AS num FROM titanic_table
        GROUP BY name
        ) AS name_count
    WHERE num > 1;
'''

# queries collected to run via script in a .py file connected to PostgreSQL
QUERY_LIST = [SURVIVED, 
              PASSENGERS_BY_CLASS, 
              SURVIVED_BY_CLASS, 
              AVG_AGE_BY_SURVIVAL, 
              AVG_AGE_BY_PCLASS,
              AVG_FARE_BY_PCLASS,
              AVG_FARE_BY_SURVIVAL,
              AVG_SIB_SP_BY_PCLASS,
              AVG_SIB_SP_BY_SURVIVAL,
              AVG_PAR_CH_BY_PCLASS,
              AVG_PAR_CH_BY_SURVIVAL,
              PASSENGERS_WITH_SAME_NAME
              ]