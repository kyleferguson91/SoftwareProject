from pymongo import MongoClient

def createMongoDB():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["blosssomblueprint"]  # MongoDB creates this when a collection is added

    print("Mongo Database created!")
    #add collections
    plantinfocollection = db["plantinfo"]
    usergardenifo = db["usergarden"]
    userfavoriteinfo = db["userplants"]
    #insert data for creation
    user_data = {"id": "test", "plantid": [1,5,6,8]}
    plant_data = {"id": "test", "water":"moist","light":"full sun partial shade", "soil":"null", "height":"null",
                  "edible":"true", "growth":"null", "layer":"null", "edibleparts":"null"}
    insert_result_users = userfavoriteinfo.insert_one(user_data)
    insert_result_usergarden = usergardenifo.insert_one(user_data)
    insert_result_plantinfo = plantinfocollection.insert_one(plant_data)
    print("Databases:", client.list_database_names())
    print("Collections in my_database:", db.list_collection_names())