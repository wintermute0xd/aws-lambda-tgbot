import requests
import datetime
import logging
import json
import os

BOT_TOKEN = os.environ['BOT_TOKEN']

TG_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'
'''
Class for telegram bot.
Can get updates from Telegram API and make response in depends of chat text message.
'''

class TgBotHandler:
    def __init__(self, update):
        self.chat_id = update['message']['chat']['id']
        self.get_botinfo()


    def star_handler(self):
        text = 'Hello from AWS Lambda'
        self.send_message(text)

    def send_message(self, text):
        print('send-start')
        method = 'sendMessage'
        params = {'chat_id': self.chat_id, 'text': text}
        print(self.chat_id)
        resp = requests.post(TG_URL + method, params)
        return resp

    def get_botinfo(self):
        method = 'getMe'
        botinfo = requests.post(TG_URL + method)
        print(botinfo)