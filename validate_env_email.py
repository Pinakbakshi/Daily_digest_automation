import os
import smtplib
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def validate_env():
    required_keys = ["SENDER_EMAIL", "SENDER_PASSWORD", "TO_EMAIL"]
    missing = [key for key in required_keys if os.getenv(key) is None]

    if missing:
        print(f"❌ Missing keys in .env: {', '.join(missing)}")
        return False
    else:
        print("✅ All required environment variables are present.")
        return True

def test_gmail_login():
    email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, password)
        print("✅ Gmail login successful using App Password.")
    except smtplib.SMTPAuthenticationError as e:
        print("❌ Gmail login failed. Authentication error.")
        print("👉 Reason:", e.smtp_error.decode() if hasattr(e, 'smtp_error') else e)
    except Exception as e:
        print("❌ Gmail login failed with unexpected error.")
        print("👉 Error:", e)

if __name__ == "__main__":
    if validate_env():
        test_gmail_login()

