import eventAdder
import newCalendarCreator
import subjectsProperties
import currentAcademicSemester
from google_apis import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

subject_list = subjectsProperties.create_subject_list('plan.pdf', currentAcademicSemester.semester_start_week)
calendar_id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar(service), service)
eventAdder.add_events(subject_list, calendar_id, service)
