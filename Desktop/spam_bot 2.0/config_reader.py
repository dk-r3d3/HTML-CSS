from pydantic import BaseSettings, SecretStr
from pyrogram import Client

api_id = 10999029
api_hash = '28f51abca348b18c88aa5453ea6b3ab6'
app = Client('my_account', api_id, api_hash)

class Settings(BaseSettings):
    bot_token: SecretStr
    class Config:
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


config = Settings()
