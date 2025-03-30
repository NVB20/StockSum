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


def get_previous_result(username, date_time):
    """
    Get the previous result based on the given date and username.
    """
    # Convert date_time string to datetime object if necessary
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S") if isinstance(date_time, str) else date_time
    
    # Query the collection for a result with a date earlier than the given date
    result = collection.find_one(
        {"username": username, "date": {"$lt": date_time}},
        sort=[("date", -1)]  # Sort by date in descending order to get the closest previous date
    )
    
    return result


def get_next_result(username, date_time):
    """
    Get the next result based on the given date and username.
    """
    # Convert date_time string to datetime object if necessary
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S") if isinstance(date_time, str) else date_time
    
    # Query the collection for a result with a date later than the given date
    result = collection.find_one(
        {"username": username, "date": {"$gt": date_time}},
        sort=[("date", 1)]  # Sort by date in ascending order to get the closest next date
    )
    
    return result