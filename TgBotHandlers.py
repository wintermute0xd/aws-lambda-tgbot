from abc import update_abstractmethods
from ast import Pass
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

    def send_message(self):
        method = 'sendMessage'
        params = {'chat_id': self.chat_id, 'text': 'Hello'}
        resp = requests.post(TG_URL + method, params)
        return resp
