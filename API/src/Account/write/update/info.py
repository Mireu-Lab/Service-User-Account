from ....set import mongo,  Set
from ....error import Error, ErrorMassage

from ...read.check import Check
from fastapi.responses import JSONResponse


def Update(UserID : str, Input_Date : dict):
    try:
        UserInfo_Change = {}

        # Info Name Update
        if Input_Date.Info.FirstName != None:
            UserInfo_Change.update({"Info.FirstName" : Input_Date.Info.FirstName})
        if Input_Date.Info.LastName != None:
            UserInfo_Change.update({"Info.LastName" : Input_Date.Info.LastName})
        if Input_Date.Info.Nickname != None:
            UserInfo_Change.update({"Info.Nickname" : Input_Date.Info.Nickname})

        # Info Phone Update
        if Input_Date.Info.Phone != None:
            UserInfo_Change.update({"Info.Phone" : Input_Date.Info.Phone})
        
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