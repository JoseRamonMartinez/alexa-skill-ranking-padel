import boto3
import json

lambda_client = boto3.client('lambda', region_name='eu-west-1')

def get_ranking():
    invoke_response = lambda_client.invoke(FunctionName="padel-prod-get_ranking",
                                           InvocationType='RequestResponse')
                                           
    return "hola"