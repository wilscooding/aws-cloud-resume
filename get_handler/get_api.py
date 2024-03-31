import boto3
from botocore.exceptions import ClientError
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('aws-cloud-resume')


def get_count():
    try:
        response = table.query(KeyConditionExpression=Key('ID').eq('visitors'))
        # Get the list of items or an empty list if no items
        items = response.get('Items', [])
        if items:  # Check if items list is not empty
            # Retrieve the count from the first item
            count = items[0]['visitors']
            return int(count)
        else:
            return 0  # Return 0 if no items were found
    except (ClientError, IndexError) as e:
        return "Error occurred while retrieving count: {}".format(str(e))


def lambda_handler(event, context):
    try:
        count = get_count()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': True,
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'count': count})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
