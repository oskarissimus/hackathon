import requests
import json

url = 'https://us-central1-papiez-polak-2137.cloudfunctions.net/add_schedule'
headers = {'Content-Type': 'application/json'}
# call on 18:40 today
data = {
    'call_schedule': '36 19 * * *',
    'first_message': 'Hello, this is a test message.',
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
