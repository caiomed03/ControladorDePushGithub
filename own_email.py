import smtplib
import json

class Email():
    gmail_user = 'caiolk960@gmail.com'
    with open('passwords.json') as f:
        gmail_password = json.load(f)['key']
    sent_from = 'caiolk960@gmail.com'
    to = ['caiolk960@gmail.com']
    subject = 'Nuevo push en el repositorio'
    
    @classmethod
    def send_email(self, user:str) -> bool:
        body = 'El usuario '+user+' ha hecho un push'
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (self.sent_from, ", ".join(self.to), self.subject, body) 
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(self.gmail_user, self.gmail_password)
            smtp_server.sendmail(self.sent_from, self.to, email_text)
            smtp_server.close()
            return True
        except Exception as ex:
            return False
        