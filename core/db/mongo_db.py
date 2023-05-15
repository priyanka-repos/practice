from pymongo import MongoClient
from scripts.config import DBConf

mongo_uri = DBConf.MONGO_URI
try:
    client = MongoClient(mongo_uri)
    print("Connected to database")
except Exception as e:
    print(e.args) 
db = client['interns_b2_23']
lib = db['priyanka_sh'] 
# client.close()
    