import pymongo
from pymongo import MongoClient

client= MongoClient("mongodb+srv://lrosesmith23:Ziggyepq22@mystation.uoil79h.mongodb.net/?retryWrites=true&w=majority") #selects client

db = client.weatherStationData #Selects database

collection = db.weather #Select collection in database

#UPDATE DOCUMENT

#

#Updating an old field
collection.delete_many({})