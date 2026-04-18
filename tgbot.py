import telebot
import requests
import json

bot = telebot.TeleBot('8275951668:AAGkWrr1Q44zimR46M3TExQMhT1OEwqcKPk')

api_key = 'cc2ba876736132e270670f8d7ebb0aef' # токен (1-е сообщение)

base_url = 'https://api.openweathermap.org/data/2.5/weather' # ссылка (2-е сообщение)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    welcome_text = (
        'Привет! Я погода-бот.\n\n'
        'Используйте команду /weather для получения прогноза.\n\n'
        'Пример:\n'
        '/weather Moscow\n'
        '/weather London\n'
        '/weather Tokyo\n\n'
        'Введите название города на английском языке.'
    )
    bot.reply_to(message, welcome_text)
