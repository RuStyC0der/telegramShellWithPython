# -*- coding: utf-8 -*-
import time


import telebot
from lesson_01 import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('a', 'v')
    markup.row('c', 'd', 'e')
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
    bot.send_message(message.chat.id, "hello")





@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)