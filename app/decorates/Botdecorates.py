from app import app
from app.app import bot
from flask import request, render_template
import telebot
import logging
import time


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
