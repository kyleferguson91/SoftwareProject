from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

def createMongoDB():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"] 

    print("Mongo Database created!")
    #add collections
    plantinfocollection = db["plantinfo"]
    usergardeninfo = db["usergarden"]
    userfavoriteinfo = db["userplants"]
    existing_indexes = usergardeninfo.index_information()
    if "id_1" not in existing_indexes:
        usergardeninfo.create_index([("id", 1)], unique=True)

    existing_indexes = userfavoriteinfo.index_information()
    if "id_1" not in existing_indexes:
        userfavoriteinfo.create_index([("id", 1)], unique=True)

    existing_indexes = plantinfocollection.index_information()
    if "id_1" not in existing_indexes:
        plantinfocollection.create_index([("id", 1)], unique=True)
    
    '''
    #insert data for creation
    user_data = {"id": "test", "plantid": [1,5,6,8]}
    plant_data = {"id": "test", "water":"moist","light":"full sun partial shade", "soil":"null", "height":"null",
                  "edible":"true", "growth":"null", "layer":"null", "edibleparts":"null"}
    #unique id's for user and plant id's

    try:
        usergardeninfo.update_one({"id": user_data["id"]}, {"$set": user_data}, upsert=True)
        userfavoriteinfo.update_one({"id": user_data["id"]}, {"$set": user_data}, upsert=True)
        plantinfocollection.update_one({"id": plant_data["id"]}, {"$set": plant_data}, upsert=True)

            
        print("Databases:", client.list_database_names())
        print("Collections in my_database:", db.list_collection_names())
    
    except DuplicateKeyError:
        print("Duplicate entry skipping insert")
    
'''
    
def addUserToMongo(username, userid):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  
    user_data = {"id": userid, "username": username, "plants":[]}
    usergardeninfo = db["usergarden"]
    userfavoriteinfo = db["userplants"]
    try:
        usergardeninfo.update_one({"id": userid}, {"$set": user_data}, upsert=True)
        userfavoriteinfo.update_one({"id": userid}, {"$set": user_data}, upsert=True)
        print("user favorite and garden keys made")
    except DuplicateKeyError:
        print("duplicate key for ", username, "and user id ", id, "skipping" )
        
        
def addPlantDetailstoMongo(plantid):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  
    plantinfocollection = db["plantinfo"]
    #need to add other parameters
    plant_data = {"id": "test", "water":"moist","light":"full sun partial shade", "soil":"null", "height":"null",
                  "edible":"true", "growth":"null", "layer":"null", "edibleparts":"null"}
    try:
        plantinfocollection.update_one({"id": plantid}, {"$set": plant_data}, upsert=True)
        print("user favorite and garden keys made")
    except DuplicateKeyError:
        print("duplicate key for plant ", plantid )