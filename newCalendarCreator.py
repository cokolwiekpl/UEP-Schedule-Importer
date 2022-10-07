from google_apis import create_service
import currentAcademicSemester

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def create_new_calendar():
    request_body_of_new_calendar = {
        'summary': currentAcademicSemester.current_semester
    }
    calendar_response = service.calendars().insert(body=request_body_of_new_calendar).execute()
    return currentAcademicSemester.current_semester


def return_calendar_id(calendar_summary):
    response = service.calendarList().list().execute()
    calendar_list = response.get('items')
    calendar_summary_and_id_list = []
    for x in calendar_list:
        calendar = x
        calendar_summary_and_id_list.append(calendar['summary'])
        calendar_summary_and_id_list.append(calendar['id'])
    for x in calendar_summary_and_id_list:
        if x == calendar_summary:
            return calendar_summary_and_id_list[calendar_summary_and_id_list.index(x) + 1]
