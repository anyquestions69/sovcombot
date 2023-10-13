import telebot
import os

bot = telebot.TeleBot(os.environ['TOKEN'], parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте! Пожалуйста, авторизуйтесь")
	
@bot.message_handler(commands=['login', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите номер телефона: ")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.infinity_polling()