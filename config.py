import os
from dotenv import load_dotenv

load_dotenv('config.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')
