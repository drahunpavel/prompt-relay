"""tg-bot config"""
import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
API_TRANSCRIBE_URL = os.getenv('API_TRANSCRIBE_URL')
