import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

msg = EmailMessage()
msg["Subject"] = "✅ Test Email from Daily Digest Bot"
msg["From"] = SENDER_EMAIL
msg["To"] = TO_EMAIL
msg.set_content("This is a test email to check SMTP setup via .env file!")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)


