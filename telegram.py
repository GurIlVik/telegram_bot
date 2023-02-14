# print({'a' : 1} | {'s' : 2})

# python -m pip install telebot

from secret import token
import telebot
bot = telebot.TeleBot(token)

# @bot.message_handler(commands= ['start'])
# def start(message):
#     print ("У меня начался рабочий день!")
#     bot.send_message(
#         message.chat.id,
#         '<b>Я Вас слушаю)</b>',
#         parse_mode='html') - это уже сам код работы бота


bot.polling(none_stop=True)
