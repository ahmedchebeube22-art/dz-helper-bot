import os
import telebot

# يجلب التوكن تلقائياً من متغيرات البيئة (Environment Variables) في Render
TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# الرد على أمر /start أو /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت متصل ويعمل بنجاح على Render 🚀")

# الرد على أي رسالة نصية أخرى
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أرسلت لي: {message.text}")

# تشغيل البوت باستمرار
bot.infinity_polling()
