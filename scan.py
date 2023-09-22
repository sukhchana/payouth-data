import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def _scan(table_name):
    try:
      dynamodb = boto3.resource('dynamodb')
      table = dynamodb.Table(table_name)
      response = table.scan()
      data = response['Items']

      while 'LastEvaluatedKey' in response:
          response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
          data.extend(response['Items'])

      print (len(data))
    except Exception as e:
      logger.info(e)
      raise e

print (_scan("usertable"))