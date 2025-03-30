from pymongo import ASCENDING, MongoClient
import datetime


MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI, username='admin', password='adminpass')
db = client["results"]
collection = db["res1"]
collection.create_index([("createdAt", ASCENDING)], expireAfterSeconds=3600)



def insert_res(result, username):
    date_time = datetime.datetime.now()
    result_save = {"username": username,  "createdAt": date_time, "result": result}
    collection.insert_one(result_save)

def get_history(username):
    results = collection.find({"username": username}).sort("createdAt", 1)  # Sort by date in ascending order
    history = list(results)  # Convert cursor to list
    return history
 
def get_result_by_index(username, index):
    history = get_history(username)
    if index < 0 or index >= len(history):
        return None  # Index out of bounds
    return history[index]