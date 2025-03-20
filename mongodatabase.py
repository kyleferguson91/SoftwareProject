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
       
    except Exception as e:
        print("error adding plant details")
        
        
        
        
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
        #print("collection here ", collection)
        json_data = json.loads(json_util.dumps(collection))

        return json_data
    
    except Exception as e:
        print("error retreiving plant details")
        
        
        
def removePlant(where, plant_id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  
    #decide if these are removing from favs/ garden
    if where == "favs":
        plantinfocollection = db["userplants"]
    elif where == "garden":
        plantinfocollection = db["usergarden"]
    try: 
        
        userid = get_user_id()
        plant_id = int(plant_id)
        print("remove plant called", "userid", userid, "where", where, "plantid", plant_id)
        if not userid:
            return None
        #check plant exists
        plant = plantinfocollection.find_one({ "id": userid, "plants.id": plant_id })
        if not plant:
            print("Plant not found for user:", userid)
            return None
        # perform the remove o
        result = plantinfocollection.update_one(
            { "id": userid, "plants.id": plant_id },  #
            { "$pull": { "plants": { "id": plant_id } } } 
        )
        if result.modified_count > 0:
            print("plant removed")
        else: 
            print("plant not removed")
    except Exception as e:
        print("error removing plant", e)
    return "result"
        