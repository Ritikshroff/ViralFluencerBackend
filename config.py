import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class Config:
    INSTAGRAM_CLIENT_ID = os.getenv("INSTAGRAM_APP_ID")
    INSTAGRAM_CLIENT_SECRET = os.getenv("INSTAGRAM_APP_SECRET")
    INSTAGRAM_REDIRECT_URI = os.getenv("REDIRECT_URI")
