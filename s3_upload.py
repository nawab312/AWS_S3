import json
import boto3

def lambda_handler(event, context):
    #Get the s3 Bucket and object from the event
    s3_event = event['Records'][0]['s3']
    bucket_name = s3_event['bucket']['name']
    object_key = s3_event['object']['key']

    #Log information
    print(f"File uploaded {object_key} in bucket: {bucket_name}")

    #Reading the file content from s3
    s3 = boto3.client('s3')
    file_content = s3.get_object(Bucket=bucket_name, Key=object_key)['Body'].read().decode('utf-8')

    print(f"File content: {file_content}")

    return {
            'statusCode': 200,
            'body': json.dumps(f'Processed file {object_key} from {bucket_name}')}

