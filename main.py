import currentAcademicSemester
from google_apis import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body_of_new_calendar = {
    'summary': currentAcademicSemester.current_semester
}
calendar_response = service.calendars().insert(body=request_body_of_new_calendar).execute()

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
        'RRULE:FREQ=WEEKLY;UNTIL=20221030T170000Z' #yyyymmdd
    ],

    # 'reminders': {
    #    'useDefault': False,
    #    'overrides': [
    #        {'method': 'email', 'minutes': 24 * 60},
    #        {'method': 'popup', 'minutes': 10},
    #    ],
    # },
}

event_response = service.events().insert(
    calendarId='29943d99a2ca5d1ac47860a24f277e4c94cc9cf097cb3672e33df078280214eb@group.calendar.google.com',
    body=event).execute()
