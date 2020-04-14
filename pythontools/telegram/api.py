import requests

TELEGRAM_TOKEN = None

def setToken(TOKEN):
    global TELEGRAM_TOKEN
    TELEGRAM_TOKEN = TOKEN

def sendMessage(chat_id, message):
    global TELEGRAM_TOKEN
    requests.post('https://api.telegram.org/bot' + TELEGRAM_TOKEN + '/sendMessage', data={'chat_id': chat_id, 'text': message, 'parse_mode': "Markdown"})