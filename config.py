import os
from dotenv import load_dotenv

load_dotenv()

INSTAGRAM_CLIENT_ID = os.getenv("INSTAGRAM_CLIENT_ID")
INSTAGRAM_CLIENT_SECRET = os.getenv("INSTAGRAM_CLIENT_SECRET")
INSTAGRAM_REDIRECT_URI = "http://127.0.0.1:3000/InstagramAuth"  # Matches frontend
