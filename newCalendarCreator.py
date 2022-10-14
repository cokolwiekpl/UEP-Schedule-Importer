import currentAcademicSemester


def create_new_calendar(service):
    request_body_of_new_calendar = {
        'summary': currentAcademicSemester.current_semester
    }
    calendar_response = service.calendars().insert(body=request_body_of_new_calendar).execute()
    return currentAcademicSemester.current_semester


def return_calendar_id(calendar_summary, service):
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
