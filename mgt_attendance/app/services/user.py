from mongodb import connectDb
from bson.json_util import dumps, loads

def findAllUsers():
    db = connectDb()
    getAllUsers = db['users'].find({})

    return dumps(list(getAllUsers))