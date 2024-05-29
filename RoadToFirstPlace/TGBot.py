import io
import os
import telebot
from telebot import types
import matplotlib.pyplot as plt
import numpy as np


TOKEN = '7470422777:AAEAtkQswXCa8ClBPkHJ3ClCWFgLfVlbCQU'
bot = telebot.TeleBot(TOKEN)

ADMIN_ROLE = 'admin'
USER_ROLE = 'user'

# Инициализируем базу данных с пользователями и их ролями
users = {
    "2016656729": ADMIN_ROLE,
    "2016656729": USER_ROLE

#5706665178 - ЛЕха
#2016656729 - Iam
}

data = [10, 242, 34 ,341, 112, 1148, 154, 78, 34]

labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', "HIU", "SASHA"]


@bot.message_handler(commands=['start'])
def start(message):
    #chat_id = message.chat.id
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name
    user_last_name = message.from_user.last_name if hasattr(message.from_user, 'last_name') else ''
    user_full_name = f"{user_name} {user_last_name}".strip()


    print(message.from_user.id)
    if user_id in users:
        usr_role = users[user_id]
        if usr_role == ADMIN_ROLE:
            markup = types.ReplyKeyboardMarkup(row_width=2)
            btn1 = types.KeyboardButton('/show_stats')
            btn2 = types.KeyboardButton('/edit_stats')
            markup.add(btn1, btn2)
            bot.reply_to(message,"Привет администратор! Нажмите /show_stats, чтобы просмотреть диаграмму, или /edit_stats, чтобы изменить данные.", reply_markup=markup)
        elif usr_role == USER_ROLE:
            markup = types.ReplyKeyboardMarkup(row_width=2)
            btn1 = types.KeyboardButton('/show_stats')
            markup.add(btn1)
            bot.reply_to(message,f"Привет {user_full_name}! Нажмите /show_stats, чтобы просмотреть диаграмму.",  reply_markup=markup)
        else:
            bot.reply_to(message,"У вас нет доступа к этому боту")

@bot.message_handler(commands=['show_stats'])
def show_stats(message):
    user_id = str(message.from_user.id)
    if user_id in users:
        plt.figure(figsize=(8, 6))
        plt.bar(labels, data)
        plt.title('Weekly Stat')
        plt.xlabel('Days')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        bot.send_photo(chat_id=message.chat.id, photo=buf)  # Используем chat.id из сообщения, а не отдельную переменную.
        buf.close()
    else:
        bot.reply_to(message, "У вас нет доступа")

@bot.message_handler(commands=['edit_stats'])
def edit_stats(message):
    user_id = str(message.chat.id)
    if user_id in users and users[user_id] == ADMIN_ROLE:
        bot.reply_to(message, "This is the statistics editing feature.")
    else:
        bot.reply_to(message, "You don't have access to this command.")

# Запуск бота
bot.polling()






