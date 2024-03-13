import os

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am a bot')
    bot.send_message(message.chat.id, 'What is your name?')
    bot.register_next_step_handler(message, process_name)


def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f'Nice to meet you, {name}!')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    print('Bot started')
    bot.polling(non_stop=True)