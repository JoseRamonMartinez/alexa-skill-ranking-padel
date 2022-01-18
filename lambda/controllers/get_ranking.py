from boto3 import client as boto3_client
from datetime import datetime
import json

lambda_client = boto3_client('lambda')

def get_ranking():
    invoke_response = lambda_client.invoke(FunctionName="get_ranking",
                                           InvocationType='Event',
                                           Payload=json.dumps({}))
    return invoke_response