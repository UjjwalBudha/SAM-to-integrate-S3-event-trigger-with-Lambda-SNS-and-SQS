import json
import boto3
import os

def lambda_handler(event, context):
    notification = "Hello, something has been added into the bucket."
    print(notification)
    
    client = boto3.client('sns')
    
    response = client.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=notification
    )
    print("Message published")
    return response
