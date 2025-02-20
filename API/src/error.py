from discord_webhook import DiscordWebhook, DiscordEmbed
from traceback import format_exc
from datetime import datetime
from json import load
from random import choice

from fastapi.responses import JSONResponse

ErrorMassage = load(open("data/error.json", "r"))
Setup_Data = load(open("data/Setup_Data.json", "r"))

webhook = DiscordWebhook(
    url=Setup_Data["DISCORD_INFO"]["WEBHOOK"],
    username=Setup_Data["SERVICE_NAME"]
)

class Error:
    def Push() -> None:
        color = ("".join(choice('0123456789ABCDEF') for j in range(6)))
        embed = DiscordEmbed(title=f'{Setup_Data["SERVICE_NAME"]} Error Logger', color=color)

        embed.set_timestamp()
        embed.add_embed_field(name='Massages', value=str(format_exc()), inline=False)
        embed.add_embed_field(name='RunTime', value=str(datetime.now().__str__()), inline=False)

        webhook.add_embed(embed)
        webhook.execute(remove_embeds=True)
        pass

    def return_error(Status_Code : int = 200, TextType : str = None, return_text : str = None) -> JSONResponse:
        return_date = {"msg" : ErrorMassage[str(Status_Code)]}

        if return_text != None:
            return_date.update({TextType : return_text})

        return JSONResponse(
            status_code = Status_Code,
            content = return_date
        )