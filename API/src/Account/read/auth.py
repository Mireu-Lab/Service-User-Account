from ...set import mongo
from ...error import Error

from .check import Check

def Auth(UserID : str, AuthType : str, Type : str):
    try:
        if Check(UserID=UserID) == True:
            return_date = mongo.account.find_one(
                {"Auth.UID" : UserID},
                {"_id" : 0, "Auth.Authority" : 1}
            )["Auth"]["Authority"][AuthType]

            if None not in return_date:
                if Type in return_date:
                    return True
                    
                else:
                    Status_Code = 403
            else:
                Status_Code = 403
        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)