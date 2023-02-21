from flask import Flask
from app.lib.db import Factory
from dotenv import load_dotenv
import telebot
from app.services import configService

load_dotenv()

TOKEN = configService.get('BOT_TOKEN')
WEBHOOK_URL = configService.get('NGROK_TOKEN')

app = Flask(__name__)

bot = telebot.TeleBot(TOKEN)

bot.set_webhook(url=WEBHOOK_URL + f'/{TOKEN}/')


db = Factory(
    DATABASE_URI=configService.get('DATABASE_URI'),
    app=app
).make()



