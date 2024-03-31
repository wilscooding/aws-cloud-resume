import boto3
from botocore.exceptions import ClientError
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('aws-cloud-resume')


def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'ID': 'visitors'},
            UpdateExpression='ADD visitors :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': True,
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'Visitor count updated successfully'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
