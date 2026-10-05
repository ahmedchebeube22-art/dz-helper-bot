import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# 1. الاستجابة لأمر /start وإرسال الأزرار
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('الخيار الأول 🚀')
    btn2 = types.KeyboardButton('الخيار الثاني 🛠️')
    btn3 = types.KeyboardButton('المساعدة ❓')
    
    markup.add(btn1, btn2)
    markup.add(btn3)

    bot.reply_to(message, "أهلاً بك! اختر من الخيارات التالية:", reply_markup=markup)

# 2. الاستجابة عند الضغط على أي زر
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    
    if text == 'الخيار الأول 🚀':
        bot.reply_to(message, "لقد اخترت الخيار الأول بنجاح!")
    elif text == 'الخيار الثاني 🛠️':
        bot.reply_to(message, "هذا هو الخيار الثاني.")
    elif text == 'المساعدة ❓':
        bot.reply_to(message, "كيف يمكنني مساعدتك؟")
    else:
        bot.reply_to(message, f"أرسلت لي: {text}")

bot.infinity_polling()
