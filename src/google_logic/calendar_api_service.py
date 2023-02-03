def create_new_calendar(service, current_semester_name):
    request_body_of_new_calendar = {
        'summary': current_semester_name
    }
    service.calendars().insert(body=request_body_of_new_calendar).execute()


def return_calendar_id(service, current_semester_name):
    create_new_calendar(service, current_semester_name)
    response = service.calendarList().list().execute()
    calendar_list = response.get('items')
    calendar_summary_and_id_list = []
    for calendar in calendar_list:
        calendar_dict = {
            'summary': calendar['summary'],
            'id': calendar['id']
        }
        calendar_summary_and_id_list.append(calendar_dict)
    for calendar in calendar_summary_and_id_list:
        if calendar['summary'] == current_semester_name:
            return calendar['id']


def add_schedule_to_google_calendar(service, subject_list, current_semester):
    calendar_id = return_calendar_id(service, current_semester.current_semester_name)
    semester_end = current_semester.semester_end

    for subject in subject_list:
        event = {
            'summary': subject.subject_name,
            'location': subject.subject_location,
            'start': {
                'dateTime': subject.subject_start,
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': subject.subject_end,
                'timeZone': 'Europe/Warsaw',
            },
            'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL=' + semester_end + 'T170000Z'  # yyyymmdd
            ],
        }
    service.events().insert(calendarId=calendar_id, body=event).execute()
