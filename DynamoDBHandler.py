import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TgBotText')

response = table.get_item(
    Key={
        'id': 'start'
    }
)
print(response)
item = response['Item']
print(item)