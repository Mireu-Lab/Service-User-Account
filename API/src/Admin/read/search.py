from ...set import mongo
from ...error import Error

import pymongo

def Search(SearchText : str = None):
    try:
        mongo.account.create_index(
            [("Info.FirstName", pymongo.TEXT),
            ("Info.LastName", pymongo.TEXT),
            ("Info.Nickname", pymongo.TEXT),
            ("Info.Phone", pymongo.TEXT),
            ("Info.Email", pymongo.TEXT)],
            name = "Account_Root_Search_Index"
        )

        SearchDict = {}
        if SearchText != None:
            SearchDict.update({'$text' : {'$search' : SearchText}})

        return list(mongo.account.find(SearchDict, {"_id" : 0, "Auth.Password" : 0, "Auth.SNS" : 0}).sort("_id", -1))

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)