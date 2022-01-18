from boto3 import client as boto3_client
from datetime import datetime
import json

lambda_client = boto3_client('lambda')

def get_player_by_name(data):
    msg = {"name":data["name"]}
    invoke_response = lambda_client.invoke(FunctionName="get_player_by_name",
                                           InvocationType='Event',
                                           Payload=json.dumps(msg))
    return invoke_response