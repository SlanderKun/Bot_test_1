import os
from app import app
from app.app import bot
from flask import request, abort
import telebot


@app.route(f'/{os.getenv("BOT_TOKEN")}/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)
