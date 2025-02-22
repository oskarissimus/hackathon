from typing import Optional
import json
import functions_framework
from pydantic import BaseModel

class CallRequest(BaseModel):
    first_message: str
    number: str

class ScheduleRequest(BaseModel):
    call_schedule: str
    first_message: str
    number: Optional[str] = "PLACEHOLDER"

from google.cloud import scheduler_v1

@functions_framework.http
def add_schedule(request):
    """Tworzy jednorazowy harmonogram na podstawie danych z request."""

    request_data = request.get_json()
    schedule_request = ScheduleRequest(**request_data)
    first_message = schedule_request.first_message
    number = schedule_request.number
    call_schedule = schedule_request.call_schedule

    client = scheduler_v1.CloudSchedulerClient()
    project_id = 'papiez-polak-2137'  # Zastąp ID twojego projektu
    location = 'us-central1'
    location_path = client.common_location_path(project_id, location)

    job = scheduler_v1.Job(
        http_target=scheduler_v1.HttpTarget(
            uri=f'https://{location}-{project_id}.cloudfunctions.net/make_call',
            http_method=scheduler_v1.HttpMethod.POST,
            headers={
                'Content-Type': 'application/json'
            },
            body=json.dumps({
                'first_message': first_message,
                'number': number
            }).encode()
        ),
        schedule=call_schedule,
        time_zone="CET"
    )

    # Utworzenie harmonogramu
    response = client.create_job(
        scheduler_v1.CreateJobRequest(
            parent=location_path,
            job=job,
        )
    )

    return 'Harmonogram utworzony: {}'.format(response.name), 201