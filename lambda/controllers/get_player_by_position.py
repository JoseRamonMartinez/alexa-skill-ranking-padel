from boto3 import client as boto3_client
from datetime import datetime
import json

lambda_client = boto3_client('lambda')

def get_player_by_position(data):
    msg = {"position":data["position"]}
    invoke_response = lambda_client.invoke(FunctionName="padel-prod-get_player_by_position",
                                           InvocationType='Event',
                                           Payload=json.dumps(msg))
    return invoke_response