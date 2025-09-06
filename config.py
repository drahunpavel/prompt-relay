"""app config"""
import os
from dotenv import load_dotenv
load_dotenv()


FASTAPI_HOST = os.getenv('FASTAPI_HOST')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT'))

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

API_TRANSCRIBE_URL = os.getenv('API_TRANSCRIBE_URL')
