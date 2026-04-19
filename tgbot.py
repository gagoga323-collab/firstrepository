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

@bot.message_handler(commands = ['weather'])
def get_weather(message):
    city = message.text.replace('/weather','').strip()

    if not city:
        bot.reply_to(
            message,
            'Пожалуйста, укажите название города\n'
            'Пример: /weather Moscow'
        )
        return
    
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',
            'lang': 'ru'
        }

        response = requests.get(base_url, params = params)
        data = response.json()

        if response.status_code != 200:
            if data.get('cod') == '404':
                bot.reply_to(message, f'Город "{city}" не найден. Проверьте написание.')
            else:
                bot.reply_to(message, 'Ошибка при получении данных о погоде.')
            return




































































# api_key = "cc2ba876736132e270670f8d7ebb0aef"
# city = "Moscow,RU"
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

# response = requests.get(url)
# data = response.json()

# print(data)  