from ....set import mongo,  Set
from ....error import Error

from ...read.check import Check

def Update(UserID : str, Input_Date : dict):
    try:
        UserInfo_Change = {}
        
        # Auth 
        if Input_Date.Password != None:
            UserInfo_Change.update({"Auth.Password" : Set.Hash_Build(Input_Date.Password)})
        if Input_Date.Sns != None:
            UserInfo_Change.update({"Auth.SNS" : Input_Date.Sns})
        
        if Check(UserID=UserID) == True:
            mongo.company.update_one(
                {"Auth.UID" : UserID}, 
                {"$set" : UserInfo_Change}
            )
            Status_Code = 200

        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)