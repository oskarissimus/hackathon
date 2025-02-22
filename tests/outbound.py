import requests
import json


url = "https://d143-213-216-69-163.ngrok-free.app/outbound-call"
headers = {
    "Content-Type": "application/json"
}
data = {
    "prompt": "jesteś eryk, moim chłopakiem wirtualnym, bardzo chcesz się ze mną spotkać i umówić na wieczór na netfix i chill",
    "first_message": "Cześć kiepan nazywam się Eryk. Chciałbym się dzisiaj z tobą spotkać i umówić na wieczór na netfix i chill",
    "number": "PLACEHOLDER"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
