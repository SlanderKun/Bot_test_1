import os
from app import app
from app.app import bot
from flask import request, render_template, abort
import telebot
from app.services.UserService import UserService
from app.services.ShopServise import ShopService


@app.route(f'/{os.getenv("BOT_TOKEN")}/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    id = message.from_user.id
    username = message.from_user.first_name
    user = UserService.find_or_create(id, username)
    chat_id = message.chat.id
    bot.send_message(chat_id, """\
Привет, добро пожаловать в маркетплейс.
Чтобы изменить ваши данные пропишите команду /--\
""")


# @bot.message_handler(commands=['set_name'])
# def set_name(message):
#     id = message.from_user.id
#     username = message.from_user.username
#     print(message)
#     print(username)
#     user = UserService.find_or_create(id, username)
#     bot.reply_to(message, "Ваше имя добавлено в базу данных")
#

@bot.message_handler(commands=['set_name'])
def set_name(message):
    chat_id = message.chat.id
    id = message.from_user.id
    username = message.from_user.first_name
    print(message)
    print(username)
    user = UserService.find_or_create(id, username)
    bot.send_message(chat_id, "Ваше имя добавлено в базу данных")


@bot.message_handler(commands=['set_display_name'])
def set_display_name(message):
    id = message.from_user.id
    username = message.from_user.first_name
    last_name = message.from_user.last_name

    if last_name != None:
        username = str(username + ' ' + last_name)
    print(username)
    user = UserService.add_display_name(id, username)

    if user == None:
        bot.reply_to(message, "Вашего пользователя не существует, введите команду /set_name")


@bot.message_handler(commands=['create_shop'])
def create_shop(message):
    id = message.from_user.id
    chat_id = message.chat.id
    entities = message.entities
    if len(entities) > 1:
        bot.send_message(chat_id, "Нельзя обработать больше 2 команд.")
        return
    print(entities[0].length)
    shop_name = message.text[entities[0].length+1:]
    print(shop_name)
    if not shop_name == '':
        user = ShopService.find_or_create_shop(id, shop_name)
    else:
        bot.send_message(chat_id, "Введите название магазина")

    if user != None:
        bot.send_message(chat_id, "У вас уже есть магазин с таким же именем")
    else:
        bot.send_message(chat_id, "Ваш магазин успешно создан")


@bot.message_handler(commands=['get_shop_by_user'])
def get_shop_by_user(message):
    id = message.from_user.id


@bot.message_handler(commands=['check'])
def get_user(message):
    print(message)