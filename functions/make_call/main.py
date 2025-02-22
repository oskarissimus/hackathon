import requests
import json
import functions_framework
from pydantic import BaseModel, ValidationError

class CallRequest(BaseModel):
    first_message: str
    number: str

@functions_framework.http
def make_call(request):
    """Funkcja wywoływana przez harmonogram, dzwoniąca pod zadany numer."""
    try:
        request_json = request.get_json()
        call_request = CallRequest(**request_json)
    except (ValidationError, json.JSONDecodeError) as e:
        return 'Błąd walidacji danych: {}'.format(e), 400

    url = "https://6165-213-216-69-163.ngrok-free.app/outbound-call"  # Twój endpoint
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "prompt": "jesteś kochanym wnuczkiem babci który przypomina o wzięciu leków",
        "first_message": call_request.first_message,
        "number": call_request.number
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Sprawdzenie, czy nie ma błędów HTTP
        return 'Połączenie zainicjowane: {}'.format(response.status_code)
    except requests.exceptions.RequestException as e:
        return 'Błąd połączenia: {}'.format(e)