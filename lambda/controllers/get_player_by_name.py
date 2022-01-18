import boto3
import json

lambda_client = boto3.client('lambda')

def get_player_by_name(data):
    msg = {"name":data["name"]}
    invoke_response = lambda_client.invoke(FunctionName="padel-prod-get_player_by_name",
                                           InvocationType='Event',
                                           Payload=json.dumps(msg))
    return invoke_response