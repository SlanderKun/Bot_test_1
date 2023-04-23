from app.app import bot
from telebot import types
from app.services.ItemService import ItemService
from app.services.ShopServise import ShopService
from app.dto.CreateItemDto import CreateItemDto


@bot.message_handler(commands=['create_item'])
def create_item(message):
    id = message.from_user.id
    chat_id = message.chat.id
    entities = message.entities
    if len(entities) > 1:
        bot.send_message(chat_id, "Нельзя обработать больше 2 команд.")
        return
    item_dto = CreateItemDto.load_from_string(message.text[entities[0].length + 1:])
    item_name = item_dto.name
    if not item_name == '':
        item = ItemService.find_or_create(id, item_dto)
    else:
        bot.send_message(chat_id, "Введите название предмета")
