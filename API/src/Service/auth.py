from fastapi.responses import JSONResponse

from ..set import mongo
from ..error import Error

from ..Account.read.check import Check

def View(UID : str) -> (JSONResponse|dict):
    try:
        UserID_Check = Check(UserID=UID)
        if type(UserID_Check) == bool:
            if UserID_Check == True:
                ReturnInfo = mongo.account.find_one(
                    {"Auth.UID" : UID}, 
                    {"_id" : 0, "Auth.Authority" : 1}
                )

                del(ReturnInfo["Auth"]["Authority"]["Account"])

                return ReturnInfo
            else:
                Status_Code = 404
        else:
            return UserID_Check

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)