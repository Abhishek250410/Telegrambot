import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Fetching token from environment variables
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I am your Render-hosted bot.")

bot.polling()
