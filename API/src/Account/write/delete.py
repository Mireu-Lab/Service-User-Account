from ...set import mongo
from ...error import Error, ErrorMassage


from ..read.check import Check

from fastapi.responses import JSONResponse

def Delete(UserID : str):
    try:
        if Check(UserID=UserID) == True:
            mongo.account.delete_one({"Auth.UID" : UserID})
            Status_Code = 200
            
        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500
    
    return Error.return_error(Status_Code)