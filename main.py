from pprint import pprint

import currentAcademicSemester
import newCalendarCreator

from google_apis import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_Id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar())

name = 'Techn.i systemy multimedialne'
location = '1.17 CEUE'

event = {
    'summary': name,
    'location': location,
    'start': {
        'dateTime': '2022-10-08T12:00:00',
        'timeZone': 'Europe/Warsaw',
    },
    'end': {
        'dateTime': '2022-10-08T13:00:00',
        'timeZone': 'Europe/Warsaw',
    },
    'recurrence': [
        'RRULE:FREQ=WEEKLY;UNTIL=20221030T170000Z'  # yyyymmdd
    ],
}

event_response = service.events().insert(
    calendarId=calendar_Id,
    body=event).execute()
