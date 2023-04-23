from app.app import bot
from telebot import types
from app.services.UserService import UserService
from app.services.ShopServise import ShopService
from app.dto.CreateShopDto import CreateShopDto


@bot.message_handler(commands=['create_shop'])
def create_shop(message):
    id = message.from_user.id
    chat_id = message.chat.id
    entities = message.entities
    if len(entities) > 1:
        bot.send_message(chat_id, "Нельзя обработать больше 2 команд.")
        return
    shop_dto = CreateShopDto.load_from_string(message.text[entities[0].length+1:])
    shop_name = shop_dto #для условия ниже
    if not shop_name == '':
        user = ShopService.create(id, shop_dto)
    else:
        bot.send_message(chat_id, "Введите название магазина")

    if user == False:
        bot.send_message(chat_id, "У вас уже есть магазин с таким же именем")
    else:
        bot.send_message(chat_id, "Ваш магазин успешно создан")


@bot.message_handler(commands=['show_shops'])
def show_shops(message):
    chat_id = message.chat.id
    shops = ShopService.find_all_shops()
    bot.send_message(chat_id, text=f"Все магазины:{shops}")
    print(shops)

