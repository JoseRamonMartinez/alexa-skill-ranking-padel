from boto3 import client as boto3_client
import json

lambda_client = boto3_client('lambda')

def get_ranking():
    invoke_response = lambda_client.invoke(FunctionName="padel-prod-get_ranking",
                                           InvocationType='RequestResponse',
                                           Payload=json.dumps({}))
    return invoke_response['Payload'].read()