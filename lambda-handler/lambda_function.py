import json
import boto3
import os

def lambda_handler(event, context):
    s3_event = event['Records'][0]
    
    s3_bucket = s3_event['s3']['bucket']['name']
    s3_object_key = s3_event['s3']['object']['key']
    
    print("S3 Bucket:", s3_bucket)
    print("S3 Object Key:", s3_object_key)
    
    notification = f"Hello, something has been added into the {s3_bucket} bucket. Object key: {s3_object_key}."
    print(notification)
    
    client = boto3.client('sns')
    
    response = client.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=json.dumps({'default': notification}),
        MessageStructure='json'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
