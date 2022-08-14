import json

import TgBotHandlers

def is_command(update):
    if 'entities' in update and update['entities'][0]['type'] == 'bot_command':
        return True
    else:
        return False

def lambda_handler(event, context):
    update = json.loads(event['body'])

    bot = TgBotHandlers.TgBotHandler(update)
    print(update)
    if is_command(update['message']):
        command = update['message']['text']
        if command == '/start':
            bot.start_handler()


    return {'statusCode': 200}

