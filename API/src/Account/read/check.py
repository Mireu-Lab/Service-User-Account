from ...set import mongo
from ...error import Error, ErrorMassage


from fastapi.responses import JSONResponse

def Check(Names : dict = None, Phone : str = None, Email : str = None, UserID : str = None):
    try:
        
        find = {}
        if Names != None:
            for Name in Names:
                find.update({f"Info.{Name}" : Names[Name]})
        if Phone != None:
            find.update({"Info.Phone" : Phone})
        if Email != None:
            find.update({"Info.Email" : Email})
        if UserID != None:
            find.update({"Auth.UID" : UserID})

        find = mongo.account.find(find)

        if len(list(find)) > 0:
            return True

        else:
            return False

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)