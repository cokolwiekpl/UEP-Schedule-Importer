from pprint import pprint

import currentAcademicSemester
from google_apis import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    'summary': currentAcademicSemester.current_semester
}
response = service.calendars().insert(body=request_body).execute()
