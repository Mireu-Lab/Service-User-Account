from pymongo import MongoClient
from hashlib import sha256
from json import load

Setup_Data = load(open("data/Setup_Data.json", "r"))

url = f"""mongodb://{Setup_Data["MONGODB_INFO"]["Account"]["USER"]}:{Setup_Data["MONGODB_INFO"]["Account"]["PASSWORD"]}@{Setup_Data["MONGODB_INFO"]["Server"]["HOST"]}:{Setup_Data["MONGODB_INFO"]["Server"]["PORT"]}/"""
mongo = MongoClient(url)[Setup_Data["MONGODB_INFO"]["Server"]["DATEBASE"]]

class Set:
    def Hash_Build(text : str):
        return sha256(str(text).encode('utf8')).hexdigest()