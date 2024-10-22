import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

# Directories
PATH_ROOT = Path('/')

# Database SQL
DATABASE_CONNECTION_STRING = f"sqlite:///{os.getenv('SQLITE_DB_PATH')}"

# AI API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Telegram Keys
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
TELEGRAM_BOT_NAME = os.getenv('TELEGRAM_BOT_NAME')