import os
import telebot
from telebot import types

# جلب توكين البوت من متغيرات البيئة
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# 1. عند إرسال /start تظهر القائمة الرئيسية الكاملة
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # الصف الأول (أزرار الصورة)
    btn1 = types.KeyboardButton('التعليم والطلاب 🎓')
    btn2 = types.KeyboardButton('الخدمات والبريد 🏢')
    
    # الصف الثاني (أزرار الصورة)
    btn3 = types.KeyboardButton('الصرف والحاسبة 💵')
    btn4 = types.KeyboardButton('الاتصالات والإنترنت 📱')
    
    # الصف الثالث (أزرار الصورة)
    btn5 = types.KeyboardButton('حول البوت ℹ️')
    btn6 = types.KeyboardButton('أرقام الطوارئ 📞')
    
    # الصف الرابع (الأزرار الإضافية)
    btn7 = types.KeyboardButton('الخيار الأول 🚀')
    btn8 = types.KeyboardButton('الخيار الثاني 🛠️')
    
    # الصف الخامس (زر المساعدة)
    btn9 = types.KeyboardButton('المساعدة ❓')
    
    # ترتيب الأزرار داخل اللوحة
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7, btn8)
    markup.add(btn9)

    welcome_text = (
        "🇩🇿 DZ Helper - القائمة الرئيسية\n\n"
        "اختر القسم الذي تريد:"
    )

    bot.reply_to(message, welcome_text, reply_markup=markup)

# 2. الاستجابة عند الضغط على أي زر
@bot.message_handler(func=lambda message: True)
def handle_all_buttons(message):
    text = message.text
    
    # أزرار الصورة الرئيسية
    if text == 'التعليم والطلاب 🎓':
        bot.reply_to(message, "مرحباً بك في قسم التعليم والطلاب! 🎓\nقريباً سيتم إضافة المراجع والمواد التعليمية.")
        
    elif text == 'الخدمات والبريد 🏢':
        bot.reply_to(message, "قسم الخدمات والبريد 🏢\nهنا يمكنك الاستعلام عن خدمات بريد الجزائر وغيرها.")
        
    elif text == 'الصرف والحاسبة 💵':
        bot.reply_to(message, "قسم الصرف والحاسبة 💵\nمتابعة أسعار العملات والحسابات البريدية.")
        
    elif text == 'الاتصالات والإنترنت 📱':
        bot.reply_to(message, "قسم الاتصالات والإنترنت 📱\nعروض وتعبئة أرصدة المتعاملين (موبيليس، جيزي، أوريدو).")
        
    elif text == 'أرقام الطوارئ 📞':
        emergency_text = (
            "📞 أرقام الطوارئ في الجزائر:\n\n"
            "• الحماية المدنية: 14\n"
            "• الشرطة: 17 / 1548\n"
            "• الدرك الوطني: 1055\n"
            "• الرقم الأخضر للأطفال: 1111"
        )
        bot.reply_to(message, emergency_text)
        
    elif text == 'حول البوت ℹ️':
        bot.reply_to(message, "🇩🇿 بوت DZ Helper\nبوت خدمي شامل لتقديم مختلف الخدمات والمعلومات البرمجية والتعليمية.")

    # الأزرار الإضافية المضافة
    elif text == 'الخيار الأول 🚀':
        bot.reply_to(message, "لقد اخترت الخيار الأول بنجاح!")
        
    elif text == 'الخيار الثاني 🛠️':
        bot.reply_to(message, "هذا هو الخيار الثاني.")
        
    elif text == 'المساعدة ❓':
        bot.reply_to(message, "مرحباً بك في قسم المساعدة، كيف يمكنني مساعدتك؟")
        
    else:
        bot.reply_to(message, "يرجى اختيار أحد الخيارات من الأزرار الظاهرة في الأسفل 👇")

# تشغيل البوت باستمرار
bot.infinity_polling()
    
