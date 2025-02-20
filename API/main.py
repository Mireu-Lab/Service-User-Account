from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Depends

from src.Account.read.auth import Auth as Account_Auth_Info

api = FastAPI()
authapi = HTTPBearer()

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
async def main():
    return RedirectResponse("https://www.mireu.xyz")


from src.Account.write import add as Account_add, delete as Account_Delete
from src.Account.write.update import (
    auth as Account_Auth_Update,
    info as Account_Info_Update,
    authoruty as Account_Authoruty_Update,
)
from src.Account.read import info as Account_info, signin as Account_signin

from src.Account.find import PasswordFind
from src.Account.auth import token, smtp

from jsonset import (
    Account_AddSet,
    Account_Info_UpdateSet,
    Account_Auth_UpdateSet,
    Account_FindSet,
    Account_PasswordFind,
)


@api.post("/v1/account/auth", tags=["Account"])
async def User_Auth(Email: str):
    return smtp.Auth_Email().Push(Email)


@api.post("/v1/account/add", tags=["Account"])
async def User_Add(Token: str, Account_AddSet: Account_AddSet):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return Account_add.Add(Account_AddSet, Check[1])

    else:
        return Check


@api.put("/v1/account/info/update", tags=["Account"])
async def User_Info_Update(
    Account_UpdateSet: Account_Info_UpdateSet,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    return Account_Info_Update.Update(UserID.credentials, Account_UpdateSet)


# @api.put("/v1/account/auth/update", tags=["Account"])
# async def User_Auth_Update( #
#     Token : str,
#     Account_UpdateSet : Account_Auth_UpdateSet,
#     UserID : HTTPAuthorizationCredentials = Depends(authapi)):

#     Check = token.Auth_Check(Token)
#     if type(Check) == list:
#         return Account_Auth_Update.Update(UserID.credentials, Account_UpdateSet)

#     else:
#         return Check


@api.put("/v1/account/auth/update", tags=["Account"])
async def User_Auth_Update(
    Token: str,
    Account_UpdateSet: Account_Auth_UpdateSet,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return Account_Auth_Update.Update(UserID.credentials, Account_UpdateSet)

    else:
        return Check


from jsonset import (
    Auth_Account_Update_Set,
    Auth_CDN_Update_Set,
    Auth_SQL_Update_Set,
    Auth_Execpro_Update_Set,
    Auth_Hosting_Update_Set,
    Auth_Apparel_Recommendation_Update_Set,
    Auth_Garbage_Aware_Update_Set,
    Auth_Profanity_Recognition_Update_Set,
    Auth_Psychoanalysis_Update_Set,
    Auth_Scientific_Treatise_Webhook_Update_Set,
)


@api.put("/v1/account/authoruty/update", tags=["Account"])
async def User_Authoruty_Update(
    Token: str,
    CDN_Update_Set: Auth_CDN_Update_Set = None,
    SQL_Update_Set: Auth_SQL_Update_Set = None,
    Execpro_Update_Set: Auth_Execpro_Update_Set = None,
    Hosting_Update_Set: Auth_Hosting_Update_Set = None,
    Apparel_Recommendation_Update_Set: Auth_Apparel_Recommendation_Update_Set = None,
    Profanity_Recognition_Update_Set: Auth_Profanity_Recognition_Update_Set = None,
    Psychoanalysis_Update_Set: Auth_Psychoanalysis_Update_Set = None,
    Garbage_Aware_Update_Set: Auth_Garbage_Aware_Update_Set = None,
    Scientific_Treatise_Webhook_Update_Set: Auth_Scientific_Treatise_Webhook_Update_Set = None,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return Account_Authoruty_Update.Update(
            UserID.credentials,
            CDN_Update_Set,
            SQL_Update_Set,
            Execpro_Update_Set,
            Hosting_Update_Set,
            Apparel_Recommendation_Update_Set,
            Profanity_Recognition_Update_Set,
            Psychoanalysis_Update_Set,
            Garbage_Aware_Update_Set,
            Scientific_Treatise_Webhook_Update_Set,
        )

    else:
        return Check


@api.delete("/v1/account/delete", tags=["Account"])
async def User_Delete(
    Token: str, UserID: HTTPAuthorizationCredentials = Depends(authapi)
):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return Account_Delete.Delete(UserID.credentials)

    else:
        return Check


@api.post("/v1/account/find", tags=["Account"])
async def User_Singin(Token: str, Account_FindSet: Account_FindSet):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return Account_signin.Signin(Account_FindSet, Check[1])

    else:
        return Check


@api.post("/v1/account/find/password", tags=["Account"])
async def User_Passwordfind(Token: str, Account_PasswordFind: Account_PasswordFind):
    Check = token.Auth_Check(Token)
    if type(Check) == list:
        return PasswordFind(Check[1], Account_PasswordFind)

    else:
        return Check


@api.get("/v1/account/info", tags=["Account"])
async def User_Info(UserID: HTTPAuthorizationCredentials = Depends(authapi)):
    return Account_info.Info(UserID.credentials)


from src.Admin.read import search as Admin_Account_Search
from src.Admin.write import (
    auth as Admin_Account_Auth_Update,
    update as Admin_Account_Info_Update,
)

from jsonset import (
    Auth_Account_Update_Set,
    Auth_CDN_Update_Set,
    Auth_SQL_Update_Set,
    Auth_Execpro_Update_Set,
    Auth_Hosting_Update_Set,
)


@api.get("/v1/admin/account/find", tags=["Admin"])
async def Root_account_search(
    Account_Info_Search: str = None,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    auth = Account_Auth_Info(UserID.credentials, "Account", "Read")
    print(auth)
    if auth == True:
        return Admin_Account_Search.Search(Account_Info_Search)

    else:
        return auth


@api.put("/v1/admin/account/auth/update", tags=["Admin"])
async def Root_account_auth_update(
    Appointment_User: str,
    Account_Update_Set: Auth_Account_Update_Set = None,
    CDN_Update_Set: Auth_CDN_Update_Set = None,
    SQL_Update_Set: Auth_SQL_Update_Set = None,
    Execpro_Update_Set: Auth_Execpro_Update_Set = None,
    Hosting_Update_Set: Auth_Hosting_Update_Set = None,
    Apparel_Recommendation_Update_Set: Auth_Apparel_Recommendation_Update_Set = None,
    Profanity_Recognition_Update_Set: Auth_Profanity_Recognition_Update_Set = None,
    Psychoanalysis_Update_Set: Auth_Psychoanalysis_Update_Set = None,
    Garbage_Aware_Update_Set: Auth_Garbage_Aware_Update_Set = None,
    Scientific_Treatise_Webhook_Update_Set: Auth_Scientific_Treatise_Webhook_Update_Set = None,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    auth = Account_Auth_Info(UserID.credentials, "Account", "Write")
    if auth == True:
        return Admin_Account_Auth_Update.Update(
            Appointment_User,
            Account_Update_Set,
            CDN_Update_Set,
            SQL_Update_Set,
            Execpro_Update_Set,
            Hosting_Update_Set,
            Apparel_Recommendation_Update_Set,
            Profanity_Recognition_Update_Set,
            Psychoanalysis_Update_Set,
            Garbage_Aware_Update_Set,
            Scientific_Treatise_Webhook_Update_Set,
        )

    else:
        return auth


@api.put("/v1/admin/account/info/update", tags=["Admin"])
async def Root_account_Info_update(
    Appointment_User: str,
    Account_UpdateSet: Account_Info_UpdateSet,
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    auth = Account_Auth_Info(UserID.credentials, "Account", "Write")
    if auth == True:
        return Admin_Account_Info_Update.Update(Appointment_User, Account_UpdateSet)

    else:
        return auth


from src.Service.auth import View as Account_Auth


@api.get("/v1/app/account/auth/view", tags=["App"])
async def App_Account_Auth_View(
    UserID: HTTPAuthorizationCredentials = Depends(authapi),
):
    return Account_Auth(UserID.credentials)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(api, host="0.0.0.0", port=80)
