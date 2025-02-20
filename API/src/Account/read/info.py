from ...set import mongo
from ...error import Error, JSONResponse

from .check import Check

def Info(UserID : str) -> (dict | JSONResponse):
    try:
        if Check(UserID=UserID) == True:
            return mongo.account.find_one(
                {"Auth.UID" : UserID},
                {"_id" : 0, "Info" : 1}
            )
        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)