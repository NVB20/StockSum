from pymongo import MongoClient

client = MongoClient("mongodb://admin:adminpass@mongodb:27017/")
db = client.position_sizing
collection = db.results