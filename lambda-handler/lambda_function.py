import boto3
import os

client = boto3.client('sns')

def lambda_handler(event, context):
   response = client.publish(TopicArn=os.environ['SNS_TOPIC_ARN'], Message="Object uploaded in bucket!")
   print("Message published")
   return(response)