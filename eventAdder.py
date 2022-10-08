import currentAcademicSemester
from google_apis import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def add_events(event_list, calendar_id):
    semester_end = currentAcademicSemester.semester_end
    for x in event_list:
        name = event_list[event_list.index(x)][0]
        location = event_list[event_list.index(x)][1]
        event_start = event_list[event_list.index(x)][2]
        event_end = event_list[event_list.index(x)][3]

        # print(name)
        # print(location)
        # print(event_start)
        # print(event_end)

        event = {
            'summary': name,
            'location': location,
            'start': {
                'dateTime': event_start,
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': event_end,
                'timeZone': 'Europe/Warsaw',
            },
            'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL=' + semester_end + 'T170000Z'  # yyyymmdd
            ],
        }
        event_response = service.events().insert(
            calendarId=calendar_id,
            body=event).execute()
