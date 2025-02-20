from ...set import Set, mongo
from ...error import Error, JSONResponse

from datetime import datetime, timedelta
import random


def Auth_Token(Email : str) -> (int | str):
    StartTime = datetime.now().timestamp()
    EndTime = (datetime.now() + timedelta(minutes=10)).timestamp()
    RANDOM_NUM = random.randint(0, 64)
    TokenSearch = mongo.temporary_token.find_one({"Email" : Email}, {"Time.End" : 1})

    try:
        if TokenSearch != None:
            if TokenSearch["Time"]["End"]  < StartTime:
                mongo.temporary_token.delete_one({"Email" : Email})
    
            else:
                return TokenSearch["Time"]["End"] - StartTime

        Token_ONE = Set.Hash_Build(f"{Email}-{datetime.now()}")
        Token_FINAL = Set.Hash_Build(Token_ONE)[RANDOM_NUM : RANDOM_NUM+6]

        mongo.temporary_token.insert_one({
            "Email" : Email,
            "Token" : Token_FINAL, 
            "Time" : {
                "Start" : StartTime, 
                "End" : EndTime
            }
        })

        return Token_FINAL

    except:
        Error.Push()
        return 500


def Auth_Check(Token : str) -> (JSONResponse | list):
    TokenSearch = mongo.temporary_token.find_one({"Token" : Token}, {"Time.End" : 1, "Email" : 1})

    if TokenSearch != None:
        if TokenSearch["Time"]["End"] > datetime.now().timestamp():
            mongo.temporary_token.delete_one({"Token" : Token})
            Status = True
            Email = TokenSearch["Email"]
            return [Status, Email]

    else:
        return Error.return_error(
            404, 
            "Auth", 
            "Incorrect authentication information and timed out information"
        )