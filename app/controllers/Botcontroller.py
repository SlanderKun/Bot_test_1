import os
from app import app
from app.app import bot
from flask import request, render_template, abort
import telebot
from app.services.UserService import UserService


@app.route(f'/{os.getenv("BOT_TOKEN")}/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, добро пожаловать в маркетплейс.
Чтобы зарегистрироваться пропишите команду /set_name\
""")


@bot.message_handler(commands=['set_name'])
def set_name(message):
    id = message.from_user.id
    username = message.from_user.username
    print(message)
    print(username)
    user = UserService.find_or_create(id, username)
    bot.reply_to(message, "Ваше имя добавлено в базу данных")


@bot.message_handler(commands=['set_name_1'])
def set_name(message):
    id = message.from_user.id
    username = message.from_user.first_name
    last_name = message.from_user.last_name

    if last_name != None:
        username = str(username + ' ' + last_name)
    print(username)

    user = UserService.find_or_create(id, username)
    bot.reply_to(message, "Ваше имя добавлено в базу данных")


@bot.message_handler(commands=['set_display_name'])
def set_display_name(message):
    idi = message.from_user.id
    username = message.from_user.first_name
    last_name = message.from_user.last_name

    if last_name != None:
        username = str(username + ' ' + last_name)
    print(username)
    user = UserService.add_display_name(idi, username)

    if user == None:
        bot.reply_to(message, "Вашего пользователя не существует, введите команду /set_name")


@bot.message_handler(commands=['check'])
def get_user(message):
    print(message)
    