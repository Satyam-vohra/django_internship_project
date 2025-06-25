from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import telebot
import json

API_TOKEN = '7322124559:AAE0huCM-Jyzx3tVNFcf6Ufwj1Ah2FmToSU'
bot = telebot.TeleBot(API_TOKEN)

# ✅ Bot Command Handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to Internship Bot!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"You said: {message.text}")

# ✅ Webhook View
@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json.loads(json_str))
        bot.process_new_updates([update])
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"error": "invalid method"})
