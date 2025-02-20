from ...set import mongo, Set
from ...error import Error, JSONResponse

def Signin(Input_Date : dict, Email : str) -> (str | JSONResponse):
    try:
        find = {"Info.Email" : Email}

        if Input_Date.Password != None:
            find.update({"Auth.Password" : Set.Hash_Build(Input_Date.Password)})
        
        if Input_Date.Sns != None:
            find.update({f"Auth.{Input_Date.Sns.SNS_Service}" : Input_Date.Sns.UID})

        find = mongo.account.find_one(find, {"Auth.UID" : 1})
        
        if find:
            return find["Auth"]

        else:
            Status_Code = 404

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)   
