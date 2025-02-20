from ...set import mongo, Set
from ...error import Error

from ..read.check import Check

from fastapi.responses import JSONResponse
from datetime import datetime

def Add(Input_Data : dict, Email : str) -> JSONResponse:
    UserID = None
    try:
        UserID = Set.Hash_Build(f"{Email}-{datetime.now().timestamp()}")

        User_Setup_Date = {
            "Info" : {
                "FirstName" : Input_Data.Info.FirstName,
                "LastName" : Input_Data.Info.LastName,
                "Nickname" : Input_Data.Info.Nickname,
                "Phone" : Input_Data.Info.Phone,
                "Email" : Email,
                "Join Time" : datetime.now().timestamp()
            },

            "Auth" : {
                "UID" : UserID,
                "Password" : Set.Hash_Build(Input_Data.Password),
                "SNS" : {
                    "google" : None,
                    "github" : None,
                    "naver" : None,
                    "kakao" : None
                },
                "Authority" : {
                    "Account" : [None],
                    "Services" : [None],
                    "CDN" : [None],
                    "SQL" : [None],
                    "Execpro" : [None],
                    "Hosting" : [None]
                }
            }
        }
        
        NameInfo = {
            "FirstName" : Input_Data.Info.FirstName,
            "LastName" : Input_Data.Info.LastName,
            "Nickname" : Input_Data.Info.Nickname,
        }
        
        if Check(Names=NameInfo, Phone=Input_Data.Info.Phone, Email=Email) == False:
            mongo.account.insert_one(User_Setup_Date)
            Status_Code = 200

        else:
            UserID = None
            Status_Code = 202

    except:
        Error.Push()
        Status_Code = 500

    return Error.return_error(Status_Code, "UserID", UserID)