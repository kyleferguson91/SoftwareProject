from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import session, jsonify
from bson import json_util
import json

def get_user_id(): 
    return session.get("userid")  

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
        usergardeninfo.update_one({"id": userid}, {"$setOnInsert": user_data}, upsert=True)
        userfavoriteinfo.update_one({"id": userid}, {"$setOnInsert": user_data}, upsert=True)
        print("user favorite and garden keys made")
    except DuplicateKeyError:
        print("duplicate key for ", username, "and user id ", id, "skipping" )
        
        
def addPlantDetailstoMongo(plantid, plantobj, where):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  
    #decide if these are going to favorites, or to garden
    if where == "usergarden":
        plantinfocollection = db["userplants"]
    elif where == "garden":
        plantinfocollection = db["usergarden"]
    #need to add other parameters to plant data, pass an object like this!
    #add the userid here 

    try: 
        id = get_user_id()
        plantinfocollection.update_one(
        {"id": id},
        {"$addToSet": {"plants": plantobj}},  # add to plant array
        upsert=True
)
       
    except DuplicateKeyError:
        print("duplicate key for plant ", plantid )
        
        
        
        
def returnPlantDetails(where):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  
    #decide if these are going to favorites, or to garden
    if where == "favs":
        plantinfocollection = db["userplants"]
    elif where == "garden":
        plantinfocollection = db["usergarden"]
    #need to add other parameters to plant data, pass an object like this!
    #add the userid here 
    
    try: 
        print("returnplantdetailscalled")
        id = get_user_id()
        if not id:
            return None
        collection = plantinfocollection.find_one({"id": id}, {"_id": 0, "id":0})
        if collection is None:
            return None
        print("collection here ", collection)
        json_data = json.loads(json_util.dumps(collection))

        return json_data
    
    except DuplicateKeyError:
        print("duplicate key for plant ")