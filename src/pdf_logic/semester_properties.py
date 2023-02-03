from dataclasses import dataclass
import datetime


@dataclass
class CurrentSemester:
    current_semester_name: str
    semester_start_week: list
    semester_end: str


def get_current_semester(semester: str) -> CurrentSemester:
    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)

    current_time = datetime.datetime.now()

    if semester == "zimowy":
        current_semester_name = "UEP " + str(current_time.year) + "/" + str(current_time.year + 1) + " Winter term"
        semester_end = str(current_time.year + 1) + '0228'
        d = datetime.date(current_time.year, 10, 1)
        semester_start_week = [str(next_weekday(d, 0)), str(next_weekday(d, 1)), str(next_weekday(d, 2)),
                               str(next_weekday(d, 3)), str(next_weekday(d, 4))]

    if semester == "letni":
        current_semester_name = "UEP " + str(current_time.year - 1) + "/" + str(current_time.year) + " Summer term"
        semester_end = str(current_time.year) + '0731'
        d = datetime.date(current_time.year, 2, 1)
        semester_start_week = [str(next_weekday(d, 0)), str(next_weekday(d, 1)), str(next_weekday(d, 2)),
                               str(next_weekday(d, 3)), str(next_weekday(d, 4))]

    return CurrentSemester(current_semester_name, semester_start_week, semester_end)
