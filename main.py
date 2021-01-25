import telebot
bot = telebot.TeleBot('1482586619:AAH11_5FnmgBjrkMf6zbJLp24ro33dXvnRM')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, f'Привет 😊 \nC чего начнём? \n{text_response} ')

text_response = "/courses - бесплатные онлайн-курсы\n/books - книги для изучения языка\n/articles - полезные статьи"

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет 😊 \nСкорее напиши 'Хочу учиться'!")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, f"Здесь можно найти учебные материалы для изучения языка программирования "
                                               "Python. Выберите пункт меню, который вас интересует:\n"
                                               f"{text_response}")
    elif message.text.lower() == "хочу учиться":
        bot.send_message(message.from_user.id, f'Лови! \n{text_response}')

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")


bot.polling(none_stop=True, interval=0)
