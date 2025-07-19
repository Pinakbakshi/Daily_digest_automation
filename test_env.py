# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()

print("EMAIL:", os.getenv("EMAIL_ADDRESS"))
print("PASS:", os.getenv("EMAIL_PASSWORD"))
print("TO:", os.getenv("TO_EMAIL"))

