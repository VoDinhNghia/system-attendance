from pymongo import MongoClient
def connectDb():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['students_management']
    return db