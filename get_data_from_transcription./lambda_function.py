import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3')
    response = client.get_object(Bucket='synthesize-test-bucket', 
        Key=event['transcription'])
        
    transcription = json.loads(response['Body'].read())
    print('xxxxx', transcription)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
