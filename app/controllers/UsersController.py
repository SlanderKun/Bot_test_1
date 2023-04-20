from app.app import bot
from telebot import types
from app.services.UserService import UserService
from app.services.ShopServise import ShopService
from app.dto.CreateShopDto import CreateShopDto
from app.dto.BaseDto import BaseDto


@bot.message_handler(commands=['start'])
def send_welcome(message):
    id = message.from_user.id
    username = message.from_user.first_name
    user = UserService.find_or_create(id, username)
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Вывод всех магазинов")
    btn2 = types.KeyboardButton("Вывод новых вещей")
    btn3 = types.KeyboardButton("Мой профиль")
    btn4 = types.KeyboardButton("❓ Как изменить никнейм")
    btn5 = types.KeyboardButton("❓ Как создать магазин")
    btn6 = types.KeyboardButton("❓ Как получить токен")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, text="""\
Привет, добро пожаловать в маркетплейс.
Чтобы изменить ваши данные пропишите команду /--\
""", reply_markup=markup)


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


@bot.message_handler(commands=['change_name']) # в данный момент не нужен
def set_display_name(message):
    id = message.from_user.id
    chat_id = message.chat.id
    entities = message.entities
    if len(entities) > 1:
        bot.send_message(chat_id, "Нельзя обработать больше 2 команд.")
        return
    print(entities[0].length)
    name = message.text[entities[0].length + 1:]
    print(name)
    if not name == '':
        user = UserService.change_display_name(id, name)
    else:
        bot.send_message(chat_id, "Пустое поле, введите никнейм")

    if user == None:
        bot.send_message(chat_id, "Вашего пользователя не существует, введите команду /set_name.")
    else:
        bot.send_message(chat_id, "Имя успешно изменено.")


@bot.message_handler(commands=['get_token'])
def get_token(message):
    chat_id = message.chat.id
    id = message.from_user.id
    token = UserService.update_token(id)
    bot.send_message(chat_id, "Ваш токен: " + token)


@bot.message_handler(commands=['profile'])
def get_profile(message):
    chat_id = message.chat.id
    id = message.chat.id
    user = UserService.find_or_create(id)

    bot.send_message(chat_id, text=f"""\
Ваш профиль:
ID: {user.id}
Username: {user.username}
Display_name: {user.display_name}
Email: {user.email}
Is_active: {user.is_active}
    """)


@bot.message_handler(commands=['get_shop_by_user'])
def get_shop_by_user(message):
    id = message.from_user.id


@bot.message_handler(commands=['check'])
def get_user(message):
    print(message)
