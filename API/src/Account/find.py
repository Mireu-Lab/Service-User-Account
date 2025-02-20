from ..set import mongo
from ..error import Error, JSONResponse

from .read.check import Check

def IDFind(Input_Date : dict) -> JSONResponse:
    try:
        IDCheck = Check(Email=Input_Date.Email)

        if type(IDCheck) == bool:
            ReturnText = {Input_Date.Email : IDCheck}
            Status_Code = 200

        else:
            return IDCheck

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code, ReturnText)


def PasswordFind(Email : str, Input_Date : dict) -> JSONResponse:
    try:
        IDCheck = Check(Email=Email)

        if IDCheck == True:
            mongo.account.update_one(
                {"Info.Email" : Email}, 
                {"$set" : {"Info.Password" : Input_Date.Password}})
            
            Status_Code = 200

        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)