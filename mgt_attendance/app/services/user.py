from mongodb import connectDb
from bson.json_util import dumps, loads

db = connectDb()
def findAllUsers():
    getAllUsers = db['users'].find({})
    return dumps(list(getAllUsers))

def findOneUser(options: object):
    user = db['users'].find_one(options)
    return dumps(user)