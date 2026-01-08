import os

from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_GOOGLE_FILE_NAME = os.getenv("CREDENTIALS_GOOGLE_FILE_NAME", "")
CREDENTIALS_GOOGLE_LOCAL_PATH = os.getenv("CREDENTIALS_GOOGLE_LOCAL_PATH", "")

LLM_KEY = os.getenv("GROQ_API_KEY", "")

FILE_PATH = os.getenv("FILE_PATH", "")

WORKSHEET_NAME = os.getenv("WORKSHEET_NAME", "")
WORKSHEET_FOLDER_ID = os.getenv("WORKSHEET_FOLDER_ID", "")