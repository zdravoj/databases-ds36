# MongoDB queries
from mongo_query import cllctn

COUNT_DOCUMENTS = cllctn.count_documents({})

FIND_ONE = cllctn.find_one({'hp': 10})

QUERY_LIST = [FIND_ONE]

if __name__ == '__main__':
    cllctn.count_documents({})