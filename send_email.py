import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    encoded_message = message.encode('utf-8')

    username = os.getenv("sender_email")
    password = os.getenv("email_password")

    receiver = os.getenv("receiver_email")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, encoded_message)
