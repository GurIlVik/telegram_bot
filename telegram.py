# d1={'a' : 1}
# d2={'s' : 2}
# d3 = d1 | d2
# print(d3)

# python -m pip install telebot
# Далее создается файл секретный для получения токена - получить токен на bot father
# на нем получается новый бот 
# token="194435528:AAEy1X9NkzpW7Ugc0gbs8DFCax-RVNjsLd4"
from secret import token
import telebot
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start'])
def start(message):
    print ("У меня начался рабочий день!")
    bot.send_message(
        message.chat.id,
        '<b>Я Вас слушаю)</b>',
        parse_mode='html')


bot.polling(none_stop=True)
