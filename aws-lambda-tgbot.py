import json

import TgBotHandlers

def lambda_handler(event, context):
    update = json.loads(event['body'])

    bot = TgBotHandlers.TgBotHandler

    print(bot.send_message())

    

