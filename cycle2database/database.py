# Setting up connection with mongoDB
import pymongo
from pymongo import MongoClient

# Library to cast MQTT plain text data into a dictionary
import ast

client= MongoClient("mongodb+srv://lrosesmith23:Ziggyepq22@mystation.uoil79h.mongodb.net/?retryWrites=true&w=majority") #selects client

db = client.weatherStationData #Selects database

collection = db.weather #Select collection in database

# Recieve and decode message

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe("weather/station/data")
        else:
            print("Failed to connect, return code: "+ rc)
# Setting up connection with the MQTT broker


def on_message(client, userdata, message):
    weatherData = str((message.payload).decode())
    print ("Message received: "  + weatherData)

    #convert string to dictionary
    convertedWeatherData = ast.literal_eval(weatherData)

    # Upload data to database
    collection.insert_one(convertedWeatherData)

def on_subscribe(client, userdata, mid, granted_qos):
     print("Subscribed")

def on_connect_fail(stuff):
     print("Failed")



import paho.mqtt.client as mqtt


myBroker = "public.mqtthq.com"
client = mqtt.Client("Python")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_connect_fail = on_connect_fail

client.connect(myBroker, 1883) #Connect to broker

client.loop_forever()







