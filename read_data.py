from decimal import Decimal
import json
import logging
import requests
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_data(table_name,email):
    try:
      dynamodb = boto3.resource('dynamodb')
      table = dynamodb.Table(table_name)
      response = table.get_item(
        Key={
          'name': email
        }
      )
      print(response['Item'])
    except Exception as e:
        logger.info(e)
        raise e

print(get_data("usertable","DJ"))
