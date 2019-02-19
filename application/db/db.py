from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient('localhost', 27017)
    db = client.innodream_finance
    return db
