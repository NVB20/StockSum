from pymongo import MongoClient
import datetime


MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI, username='admin', password='adminpass')
db = client["results"]
collection = db["res1"]


def insert_res(result, username):
    date_time = datetime.datetime.now()
    result_save = {"username": username,  "date": date_time, "result": result}
    collection.insert_one(result_save)