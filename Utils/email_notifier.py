import os
from smtplib import SMTP
from ConfigParser import ConfigParser
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.text import MIMEText


class EmailNotifier:
    def __init__(self, config_file):
        config = ConfigParser()
        config.read(config_file)
        self.server = config.get('smtp', 'server')
        self.port = config.get('smtp', 'port')
        self.username = config.get('smtp', 'username')
        self.password = os.environ.get('EMAIL_PASSWORD', '')
        self.sender = config.get('smtp', 'sender')

    def send_email(self, receiver, subject, text):
        message = MIMEMultipart('related')
        message['From'] = self.sender
        message['To'] = receiver
        message['Date'] = formatdate(localtime=True)
        message['Subject'] = subject

        message.attach(MIMEText(text))

        smtp = SMTP(self.server, int(self.port))
        smtp.starttls()
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, receiver, message.as_string())
        smtp.close()
