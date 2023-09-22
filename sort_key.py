import boto3
from boto3.dynamodb.conditions import Key, Attr

def get_user(first_name, last_name):
  dynamodb = boto3.resource('dynamodb')

  table = dynamodb.Table('user')

  response = table.query(
    KeyConditionExpression=Key('first_name').eq(first_name) & Key('last_name').eq(last_name)
  )

  print(response['Items'])


get_user("Dhananjay", "More Patil")
