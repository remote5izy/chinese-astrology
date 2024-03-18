from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://01057031:Grace910922@astro.azuoap2.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server

class Mongodb():
    def __init__(self,dbname,tablename):
        client = MongoClient(uri, server_api=ServerApi("1"))

        # Send a ping to confirm a successful connection
        try:
            client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        db = client[dbname]
        self.table = db[tablename]

db = Mongodb("chinese_astronology","test")


# item = {"_id": 1, "value": "Your mainStar & name"}
# db.table.insert_one(item)
# table.replace_one({"_id": item["_id"]}, item)
# 检索文档的例子
# result = table.find_one({"value": "Your mainStar & name "})
# print(result)