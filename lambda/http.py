import requests
from dotenv import load_dotenv

def http(path,payload):

    load_dotenv()

    api_key = os.environ['API_KEY']
    aws_domain = os.environ['AWS_URL']

    headers = {
    'x-api-key': api_key
    }

    url = f'{}{}'.format(aws_domain, path)

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text