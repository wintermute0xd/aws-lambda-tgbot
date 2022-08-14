import boto3

def read_db(lang):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TgBotText')

    response = table.get_item(
        Key={
            'id': 'start'
        }
    )
    item = response['Item'][lang]
    return (item)