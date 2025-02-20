from pydantic import BaseModel

# Account Setup
class SNSInfo(BaseModel):
    SNS_Service : str
    UID : str

class Bank_Account(BaseModel):
    Bank : str
    Number : str

class UserInfo(BaseModel):
    FirstName : str = None
    LastName : str = None
    Nickname : str = None
    Phone : str = None


class Account_AddSet(BaseModel):
    Password : str
    Info : UserInfo

class Account_PasswordFind(BaseModel):
    Password : str = None

class Account_Info_UpdateSet(BaseModel):
    Info : UserInfo = None

class Account_Auth_UpdateSet(BaseModel):
    Password : str = None
    Sns : SNSInfo = None

class Account_FindSet(BaseModel):
    Password : str
    Sns : SNSInfo = None


# Admin Setup
from enum import Enum

class Auth_Account_Update_Set(str, Enum):
    All_No = "None"
    Read = "Read"
    Write = "Read/Write"
    All = "All"

class Auth_CDN_Update_Set(str, Enum):
    All_No = "None"
    Read = "Read"
    Write = "Read/Write"
    All = "All"

class Auth_SQL_Update_Set(str, Enum):
    All_No = "None"
    Read = "Read"
    Write = "Read/Write"
    All = "All"

class Auth_Execpro_Update_Set(str, Enum):
    All_No = "None"
    Read = "Read"
    Write = "Read/Write"
    All = "All"

class Auth_Hosting_Update_Set(str, Enum):
    All_No = "None"
    Read = "Read"
    Write = "Read/Write"
    All = "All"

class Auth_Apparel_Recommendation_Update_Set(str, Enum):
    Off = "Off"
    On = "On"


class Auth_Profanity_Recognition_Update_Set(str, Enum):
    Off = "Off"
    On = "On"

class Auth_Psychoanalysis_Update_Set(str, Enum):
    Off = "Off"
    On = "On"

class Auth_Garbage_Aware_Update_Set(str, Enum):
    Off = "Off"
    On = "On"

class Auth_Scientific_Treatise_Webhook_Update_Set(str, Enum):
    Off = "Off"
    On = "On"