import os

from flask import Flask
from app.lib.db import Factory
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')
WEBHOOK_URL = os.environ.get('NGROK_TOKEN')

bot = telebot.TeleBot(TOKEN)

bot.set_webhook(url=WEBHOOK_URL + f'/{TOKEN}/')

app = Flask(__name__)

db = Factory(
    DATABASE_URI=os.environ.get('DATABASE_URI'),
    app=app
).make()



