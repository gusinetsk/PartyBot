import telebot
from telebot import types
from random import choice
from text import *
from zadania import *
from conf import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Играть", callback_data="Играть")
    but_2 = types.InlineKeyboardButton(text="Правила", callback_data="Правила")
    key.add(but_1, but_2)
    bot.send_message(message.chat.id, text1)
    bot.send_message(message.chat.id, text2)
    bot.send_message(message.chat.id, text3)
    bot.send_message(message.chat.id,'Для начала игры нажми на кнопку "играть",если ты играешь впервые нажми на кнопку "Правила"', reply_markup=key)



@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'Правила':
    key = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text="Начать игру", callback_data="Начать игру")
    key.add(but1)
    bot.send_message(c.message.chat.id, pravila1, reply_markup=key)
  elif c.data == 'Играть':
      markup = types.ReplyKeyboardMarkup(row_width=1)
      btn1 = types.KeyboardButton("Правда")
      btn2 = types.KeyboardButton("Действие")
      markup.add(btn1, btn2)
      bot.send_message(c.message.chat.id, 'Используйте кнопки Правда или Действие, чтобы начать игру', reply_markup=markup)
  if c.data == 'Начать игру':
      markup = types.ReplyKeyboardMarkup(row_width=1)
      btn1 = types.KeyboardButton("Правда")
      btn2 = types.KeyboardButton("Действие")
      markup.add(btn1, btn2)
      bot.send_message(c.message.chat.id, text='Используйте кнопки Правда или Действие, чтобы начать игру', reply_markup=markup)


@bot.message_handler()
def game(message):
    if message.text == 'Правда' or message.text == 'правда':
        photo = open(choice(pravda), 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text == 'Действие' or message.text == 'действие':
        photo = open(choice(active), 'rb')
        bot.send_photo(message.chat.id, photo)




bot.polling(none_stop=True)