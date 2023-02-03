from dataclasses import dataclass


@dataclass
class SubjectProperties:
    subject_name: str
    subject_location: str
    subject_start: str
    subject_end: str


def create_raw_subject_list(week_schedule_list: list) -> list:
    subject_properties_list = []
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    for day_index, day in enumerate(week_schedule_list):
        for i in day:
            if isinstance(i, str) and len(i) == 11 and i[2] == ':' and i[5] == '-' and i[8] == ':':
                subject_date = i.split("-")
                subject_start = f"{days[day_index]}T{subject_date[0]}:00"
                subject_end = f"{days[day_index]}T{subject_date[1]}:00"
                next_property = day[day.index(i) + 1]
                if "Lab" in next_property or "Ćwi" in next_property or "Wyk" in next_property or "Lek" in next_property:
                    subject_name = next_property
                    subject_location = day[day.index(i) + 2]
                else:
                    subject_name = next_property + ' ' + day[day.index(i) + 2]
                    subject_location = day[day.index(i) + 3]

                if subject_location == "harmonogram":
                    subject_location = "Check Hornet"
                subject_properties_list.append(SubjectProperties(subject_name, subject_location, subject_start, subject_end))
    return subject_properties_list


def get_subject_list(week_schedule_list: list, semester_start_week: list) -> list[SubjectProperties]:
    subject_properties_list = create_raw_subject_list(week_schedule_list)
    day_map = {
        'monday': semester_start_week[0],
        'tuesday': semester_start_week[1],
        'wednesday': semester_start_week[2],
        'thursday': semester_start_week[3],
        'friday': semester_start_week[4]
    }

    for subject in subject_properties_list:
        subject_start = subject.subject_start
        subject_end = subject.subject_end
        for day, date in day_map.items():
            if day in subject_start:
                subject_start = subject_start.replace(day, date)
                subject_end = subject_end.replace(day, date)
        subject.subject_start = subject_start
        subject.subject_end = subject_end
    return subject_properties_list
