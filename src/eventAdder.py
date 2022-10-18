import currentAcademicSemester


def add_events(event_list, calendar_id, service):
    semester_end = currentAcademicSemester.semester_end
    for x in event_list:
        name = event_list[event_list.index(x)][0]
        location = event_list[event_list.index(x)][1]
        event_start = event_list[event_list.index(x)][2]
        event_end = event_list[event_list.index(x)][3]

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
