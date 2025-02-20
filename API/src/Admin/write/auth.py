from ...set import mongo
from ...error import Error

from fastapi.responses import JSONResponse

def Service_Set_Auth(Update_Set : str) -> list:
    ReturnSet = []
    if Update_Set == "All_No" or Update_Set == "Off":
        return ReturnSet
    elif Update_Set == "Read":
        ReturnSet.append("Read")
    elif Update_Set == "Write":
        ReturnSet.append("Read")
        ReturnSet.append("Write")
    elif Update_Set == "All":
        ReturnSet.append("Read")
        ReturnSet.append("Write")
        ReturnSet.append("Delete")
    elif Update_Set == "On":
        ReturnSet.append("On")
    
    return ReturnSet

def Update(
    UserID : str,
    CDN_Update_Set : str, 
    SQL_Update_Set : str, 
    Execpro_Update_Set : str,
    Hosting_Update_Set : str,
    Apparel_Recommendation_Update_Set : str,
    Profanity_Recognition_Update_Set : str,
    Psychoanalysis_Update_Set : str,
    Garbage_Aware_Update_Set : str,
    Scientific_Treatise_Webhook_Update_Set : str) -> JSONResponse:

    try:
        Account_Auth_Update = {}

        # Services
        if Apparel_Recommendation_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Apparel_Recommendation" : Service_Set_Auth(Apparel_Recommendation_Update_Set)})
        if Profanity_Recognition_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Profanity_Recognition" : Service_Set_Auth(Profanity_Recognition_Update_Set)})
        if Psychoanalysis_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Psychoanalysis_Update" : Service_Set_Auth(Psychoanalysis_Update_Set)})
        if Garbage_Aware_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Garbage_Aware" : Service_Set_Auth(Garbage_Aware_Update_Set)})
        if Scientific_Treatise_Webhook_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Scientific_Treatise" : Service_Set_Auth(Scientific_Treatise_Webhook_Update_Set)})

        # Hosting
        if CDN_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.CDN" : Service_Set_Auth(CDN_Update_Set)})
        if SQL_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.SQL" : Service_Set_Auth(SQL_Update_Set)})
        if Execpro_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Execpro" : Service_Set_Auth(Execpro_Update_Set)})
        if Hosting_Update_Set != None:
            Account_Auth_Update.update({"Auth.Authority.Hosting" : Service_Set_Auth(Hosting_Update_Set)})

        mongo.account.update_one(
            {"Auth.UID" : UserID}, 
            {"$set" : Account_Auth_Update})

        Status_Code = 200
    
    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code)