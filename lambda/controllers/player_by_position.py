from boto3 import client as boto3_client
from datetime import datetime
import json

lambda_client = boto3_client('lambda')

def lambda_handler(event, context):
    msg = {"position":"1"}
    invoke_response = lambda_client.invoke(FunctionName="get_player_by_position",
                                           InvocationType='Event',
                                           Payload=json.dumps(msg))
    print(invoke_response)