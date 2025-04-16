import telebot
import subprocess
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # الحصول على التوكن من متغير البيئة
ALLOWED_USERS = [6438249032]  # ID الخاص بك

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in ALLOWED_USERS:
        return bot.reply_to(message, "هذا البوت خاص وغير متاح لك.")
    bot.reply_to(message, "أهلاً بك في JiabLoadBot!\nأرسل أي رابط فيديو وسأقوم بتحميله لك.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    if message.from_user.id not in ALLOWED_USERS:
        return bot.reply_to(message, "هذا البوت خاص وغير متاح لك.")

    url = message.text
    bot.reply_to(message, "جاري التحميل...")

    try:
        subprocess.run(['yt-dlp', '-o', 'video.mp4', url], check=True)
        with open('video.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ أثناء التحميل.\n{e}")

bot.polling()
