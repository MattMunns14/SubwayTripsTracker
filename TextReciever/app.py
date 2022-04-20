from decimal import Decimal
from time import time

import boto3

from utils import dict_to_dynamo_json


def lambda_handler(event, context):

    try:
        body = event['body'].split('&')
        for param in body:
            if 'Body' in param:
                message = param.split('=')[1]
        message_parts = message.split('+')

        train = message_parts[0]
        wait_time = message_parts[1]
        timestamp = time()

        post_trip_to_dynamo(train, wait_time, timestamp)

        return {
            "headers": {"content-type": "text/xml"},
            "statusCode": 200,
            "body": "<Response> <Message>Trip Recorded!</Message> </Response>",
        }
    except:
        return {
            "headers": {"content-type": "text/xml"},
            "statusCode": 200,
            "body": "<Response> <Message>Error processing trip</Message> </Response>",
        }


def post_trip_to_dynamo(train, wait_time, timestamp):
    if not isinstance(timestamp, Decimal):
        timestamp = Decimal(str(timestamp))
    dict_to_post = {
        'train': train,
        'wait_time': wait_time,
        'timestamp': timestamp
    }
    table = boto3.client('dynamodb')
    table.put_item(
        TableName="TextReciever-TripsTable-1J4MQSZD4BG19",
        Item=dict_to_dynamo_json(dict_to_post)
    )