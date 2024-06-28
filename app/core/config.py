from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv('DATABASE')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
PORT = int(os.getenv('PORT'))
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')