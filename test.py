import pymongo
from pymongo import MongoClient

client= MongoClient("mongodb+srv://lrosesmith23:Ziggyepq22@mystation.uoil79h.mongodb.net/?retryWrites=true&w=majority") #selects client

db = client.weatherStationData #Selects database

collection = db.weather #Select collection in database

#UPDATE DOCUMENT

#Adding a new field to one document
collection.update_one({"_id":1}, {"$set": {"humidity": 45}})

#Adding a new field to multiple documents
collection.update_many({"temperature": 27}, {"$set": {"pressure": 10000}})

#Updating an old field
collection.update_one({"_id": 5}, {"$set": {"airquality": "fresh air"}})