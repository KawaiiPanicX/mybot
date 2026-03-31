import telebot
import os
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")   # Better to use environment variable

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def get_chat_id(message):
    try:
        bot.send_message(message.chat.id, f"Chat ID: {message.chat.id}")
        print(f"Sent to: {message.chat.id}")
    except Exception as e:
        print(f"Error: {e}")

print("Bot started...")
while True:
    try:
        bot.infinity_polling(none_stop=True, timeout=20)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
