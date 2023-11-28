import psutil
import os
import telebot
from dotenv import load_dotenv

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)

if percent <= 98:
    load_dotenv()
    bot_key = os.getenv('BOT_KEY')
    chat_id = os.getenv('CHAT_ID')

    bot = telebot.TeleBot(bot_key)
    bot.send_message(chat_id, f"Battery percent is {percent}%")