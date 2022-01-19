import requests

def http(url, api_key, payload):
    
    headers = {
    'x-api-key': api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text