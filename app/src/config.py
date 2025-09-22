import os

from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_GOOGLE_FILE_NAME = os.getenv("CREDENTIALS_GOOGLE_FILE_NAME", "")
CREDENTIALS_GOOGLE_LOCAL_PATH = os.getenv("CREDENTIALS_GOOGLE_LOCAL_PATH", "")