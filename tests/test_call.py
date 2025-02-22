import requests


url = "https://us-central1-papiez-polak-2137.cloudfunctions.net/make_call"

payload = {
    "number": "PLACEHOLDER",
    "first_message": "Cześć babciu, weź enarenal na nadciśnienie",
}

response = requests.post(url, json=payload)
print(f"Status code: {response.status_code}")
print(f"Response: {response.text}")
