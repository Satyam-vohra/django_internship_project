# bot_polling.py
import telebot

API_TOKEN = '7322124559:AAE0huCM-Jyzx3tVNFcf6Ufwj1Ah2FmToSU'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Welcome to your Internship Bot.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is polling now...")
bot.infinity_polling()
