from ...set import Setup_Data
from ...error import Error, JSONResponse
from .token import Auth_Token

from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime

class Auth_Email:
    def __init__(self) -> None:
        if Setup_Data["SMTP_INFO"]["Server"]["SSL"] == True:
            self.SMTPServer = SMTP_SSL(
                Setup_Data["SMTP_INFO"]["Server"]["HOST"],
                Setup_Data["SMTP_INFO"]["Server"]["PORT"]
            )

        else:
            self.SMTPServer = SMTP(
                Setup_Data["SMTP_INFO"]["Server"]["HOST"],
                Setup_Data["SMTP_INFO"]["Server"]["PORT"]
            )

        self.SMTPServer.login(
            Setup_Data["SMTP_INFO"]["Account"]["EMAIL"],
            Setup_Data["SMTP_INFO"]["Account"]["TOKEN"]
        )

    def Push(self, Email : str) -> JSONResponse:
        try:
            Errormsg = None
            if len(Email) != 0:
                Token = Auth_Token(Email)

                if type(Token) != int and type(Token) != float:
                    msg = MIMEMultipart()
                    msg['To'] = Email

                    msg['Subject'] = f'[{Setup_Data["SERVICE_NAME"]}] 이메일 인증'
                    msg.attach(MIMEText(f"이메일 인증을 위한 인증번호는 아래와 같습니다.\n\n {str(Token)}", "plain"))

                    self.SMTPServer.sendmail(
                        Setup_Data["SMTP_INFO"]["Account"]["EMAIL"], 
                        Email, 
                        msg.as_string()
                    )
                    self.SMTPServer.close()

                    Status_Code = 200
                        
                else:
                    if type(Token) == int:    
                        Status_Code = 200

                    elif type(Token) == float:
                        Status_Code = 202
                        Errormsg = datetime.strftime(datetime.fromtimestamp(Token), "%M:%S")
            else:
                Status_Code = 403
                
        except:
            Error.Push()
            Status_Code = 500

        return Error.return_error(Status_Code, "Retry_Time", Errormsg)