import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "noreply@christembassy.org"
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.sendgrid.net', 465) as smtp:
        smtp.login('apikey', os.getenv("SENDGRID_API_KEY"))
        smtp.send_message(msg)