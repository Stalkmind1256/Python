import io
import telebot
from telebot import types
import matplotlib.pyplot as plt
from db_bot import SessionLocal, User, init_db
from conf import TOKEN


init_db()

bot = telebot.TeleBot(TOKEN)

ADMIN_ROLE = 'admin'
USER_ROLE = 'user'

data = [10, 242, 34, 341, 112, 1148, 154, 78, 34]
labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', "HIU", "SASHA"]

def get_or_create_session(session, telegram_id, username):
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id, username=username, user_role=USER_ROLE)
        session.add(user)
        session.commit()
    return user

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    with SessionLocal() as session:
        user = get_or_create_session(session, user_id, username)
        user_full_name = f"{message.from_user.first_name} {getattr(message.from_user, 'last_name', '')}".strip()

        if user.user_role == ADMIN_ROLE:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1 = types.KeyboardButton('/show_stats')
            btn2 = types.KeyboardButton('/edit_stats')
            markup.add(btn1, btn2)
            bot.reply_to(message, f"Здравствуйте, администратор {user_full_name}! Нажмите /show_stats, чтобы просмотреть статистику, или /edit_stats для редактирования данных.", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn1 = types.KeyboardButton('/show_stats')
            markup.add(btn1)
            bot.reply_to(message, f"Здравствуйте, {user_full_name}! Нажмите /show_stats, чтобы просмотреть статистику.", reply_markup=markup)

@bot.message_handler(commands=['show_stats'])
def show_stats(message):
    with SessionLocal() as session:
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()

        if not user or user.user_role not in [ADMIN_ROLE, USER_ROLE]:
            bot.reply_to(message, "У вас нет доступа к этой функции.")
            return

        plt.figure(figsize=(8, 6))
        plt.bar(labels, data)
        plt.title('Статистика за неделю')
        plt.xlabel('Дни')
        plt.ylabel('Значения')
        plt.xticks(rotation=45)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        bot.send_photo(chat_id=message.chat.id, photo=buf)
        buf.close()

@bot.message_handler(commands=['edit_stats'])
def edit_stats(message):
    with SessionLocal() as session:
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()

        if user and user.user_role == ADMIN_ROLE:
            bot.reply_to(message, "Функция редактирования статистики.")
        else:
            bot.reply_to(message, "У вас нет доступа к этой команде.")

bot.polling(none_stop=True)