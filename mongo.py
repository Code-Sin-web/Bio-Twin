from pymongo import MongoClient
client = MongoClient("YOUR_MONGODB_URL")
db = client["biotwin"]
patient_collection = db["patients"]