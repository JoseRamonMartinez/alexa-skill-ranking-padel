import requests
import json
import os
from dotenv import load_dotenv

def http(path):
    load_dotenv()
    payload = {}
    api_key = os.environ['API_KEY']
    aws_domain = os.environ['AWS_DOMAIN']
    aws_region = os.environ["AWS_REGION"]
    
    headers = {
    'x-api-key': api_key
    }

    url = 'https://{}.execute-api.{}.amazonaws.com{}'.format(aws_domain, aws_region, path)

    response = requests.get(url, headers=headers, data=payload)

    return json.dumps(response.text)