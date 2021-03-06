# Телеграм-бот v.002 - бот создаёт меню, присылает собачку, и анекдот

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types
import requests
import bs4

bot = telebot.TeleBot('5105972662:AAG24fr382U1_hosO4Zrb-tv_BTakAV1MPk')  # Создаем экземпляр бота

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("WEB-камера")
        btn3 = types.KeyboardButton("Управление")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Картиночки с котиками")
        btn2 = types.KeyboardButton("Анекдоты")
        btn3 = types.KeyboardButton("Картиночки с собачками")
        btn4 = types.KeyboardButton("Играть в камень-ножницы-бумага")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)
# ..............................................................................
    elif ms_text == "/cat" or ms_text == "Картиночки с котиками":
        contents = requests.get('https://random.cat/meow.json').json()
        urlCAT = contents['url']
        bot.send_photo(chat_id, photo=urlCAT, caption="Держи котика!")
# ..............................................................................
    elif ms_text == "Анекдоты":
        bot.send_message(chat_id, text="еще не готово...")
# .............................................................................
    elif ms_text == "/dog" or ms_text == "Картиночки с собачками":
        contents = requests.get('https://random.dog/woof.json').json()
        urlDOG = contents['url']
        bot.send_photo(chat_id, photo=urlDOG, caption="Держи собатьку!")
#..............................................................................
    elif ms_text == "Играть в камень-ножницы-бумага":
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "WEB-камера":   # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Панасенко Софья, 1-МД-5")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/ave_satanas_bitch")
        key1.add(btn1)
        img = open('author.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)

    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()
