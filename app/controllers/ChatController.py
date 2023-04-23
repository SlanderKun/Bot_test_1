from app.app import bot


@bot.message_handler(content_types=['text'])
def text_from_user(message):
    chat_id = message.chat.id
    user_text = message.text
    print(message.from_user.first_name, '|', message.from_user.username, ':', user_text)

    if (user_text == "❓ Как создать магазин"):
        bot.send_message(chat_id, text="Чтобы создать магазин пропишите команду /create_shop name='ИМЯ МАГАЗИНА'.")

    elif (user_text == "❓ Как получить токен"):
        bot.send_message(chat_id, text="Чтобы получить токен пропишите /get_token.")

    elif (user_text == "❓ Как изменить никнейм"):
        bot.send_message(chat_id, text="Чтобы изменить никнейм пропишите команду /change_name 'НОВОЕ ИМЯ'.")

    elif (user_text == "Мой профиль"):
        bot.send_message(chat_id, text="Чтобы посмотреть свой профиль напишите /profile.")

    elif (user_text == "❓ Как добавить предмет в магазин"):
        bot.send_message(chat_id, text="""
        Чтобы добавить предмет пропишите команду 
        /create_item shop='ИМЯ ИМЕЮЩЕГО МАГАЗИНА' name='ИМЯ ПРЕДМЕТА' category='ИМЯ КАТЕГОРИИ' amount='КОЛИЧЕСТВО'""")
