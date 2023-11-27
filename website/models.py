from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://01057031:Grace910922@astro.azuoap2.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["chinese_astronology"]
table = db["data"]
item = {"value": "Your mainStar & name", "_id": 66}
# table.insert_one(item)
table.replace_one({"_id": item["_id"]}, item)
