import boto3
import json

lambda_client = boto3.client('lambda')

def get_ranking():
    invoke_response = lambda_client.invoke(FunctionName="padel-prod-get_ranking",
                                           InvocationType='RequestResponse')
                                           
    return invoke_response['Payload'].read()