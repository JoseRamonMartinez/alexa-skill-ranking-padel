import requests
from dotenv import load_dotenv
import os

def http(path,payload):

    load_dotenv()
    api_key = os.environ['API_KEY']
    aws_domain = os.environ['AWS_DOMAIN']
    aws_region = os.environ['AWS_REGION']
    
    headers = {
    'x-api-key': api_key
    }

    url = 'https://{}.execute-api.{}.amazonaws.com{}'.format(aws_domain, aws_region, path)

    #response = requests.get(url, headers=headers, data=payload)

    return "hola"#response.text