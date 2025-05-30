import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

def send_sms(message):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("RECIPIENT_PHONE_NUMBER")
    )

if __name__ == "__main__":
    send_sms("Christ Embassy Reminder: Join us Sunday @10AM – You’re invited!")