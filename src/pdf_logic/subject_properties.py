from dataclasses import dataclass
from tkinter import messagebox

from gui.gui_notification import show_error_message


@dataclass
class SubjectProperties:
    subject_name: str
    subject_location: str
    subject_start: str
    subject_end: str


def create_raw_subject_list(week_schedule_list: list):
    subject_properties_list = []

    for day in week_schedule_list:
        for i in day:
            if isinstance(i, str):
                subject_name = ''
                subject_location = ''
                subject_start = ''
                subject_end = ''
                if i[2] == ':' and i[5] == '-' and i[8] == ':':  # zabezpieczyć jeśli jest mniej liter w stringu
                    subject_date = i.split("-")
                    if (week_schedule_list.index(day)) == 0:
                        subject_start = f"mondayT{subject_date[0]}:00"
                        subject_end = f"mondayT{subject_date[1]}:00"
                    elif (week_schedule_list.index(day)) == 1:
                        subject_start = f"tuesdayT{subject_date[0]}:00"
                        subject_end = f"tuesdayT{subject_date[1]}:00"
                    elif (week_schedule_list.index(day)) == 2:
                        subject_start = f"wednesdayT{subject_date[0]}:00"
                        subject_end = f"wednesdayT{subject_date[1]}:00"
                    elif (week_schedule_list.index(day)) == 3:
                        subject_start = f"thursdayT{subject_date[0]}:00"
                        subject_end = f"thursdayT{subject_date[1]}:00"
                    elif (week_schedule_list.index(day)) == 4:
                        subject_start = f"fridayT{subject_date[0]}:00"
                        subject_end = f"fridayT{subject_date[1]}:00"
                    next_property = day[day.index(i) + 1]

                    if "Lab" in next_property or "Ćwi" in next_property or "Wyk" in next_property or "Lek" in next_property:
                        subject_name = day[day.index(i) + 1]
                        subject_location = day[day.index(i) + 2]
                    else:
                        subject_name = day[day.index(i) + 1] + ' ' + day[day.index(i) + 2]
                        subject_location = day[day.index(i) + 3]

                if subject_name != '':
                    if subject_location == "harmonogram":
                        subject_location = "Check Hornet"
                    subject_properties_list.append(SubjectProperties(subject_name, subject_location, subject_start, subject_end))
    return subject_properties_list


def get_subject_list(week_schedule_list, semester_start_week):
    subject_properties_list = create_raw_subject_list(week_schedule_list)
    for subject in subject_properties_list:
        subject_start = subject.subject_start
        subject_end = subject.subject_end
        if 'monday' in subject_start:
            subject_start = subject_start.replace("monday", semester_start_week[0])
            subject_end = subject_end.replace("monday", semester_start_week[0])
        if 'tuesday' in subject_start:
            subject_start = subject_start.replace("tuesday", semester_start_week[1])
            subject_end = subject_end.replace("tuesday", semester_start_week[1])
        if 'wednesday' in subject_start:
            subject_start = subject_start.replace("wednesday", semester_start_week[2])
            subject_end = subject_end.replace("wednesday", semester_start_week[2])
        if 'thursday' in subject_start:
            subject_start = subject_start.replace("thursday", semester_start_week[3])
            subject_end = subject_end.replace("thursday", semester_start_week[3])
        if 'friday' in subject_start:
            subject_start = subject_start.replace("friday", semester_start_week[4])
            subject_end = subject_end.replace("friday", semester_start_week[4])
        subject.subject_start = subject_start
        subject.subject_end = subject_end
    return delete_nonstandard_subjects(subject_properties_list)


def delete_nonstandard_subjects(subject_properties_list):
    deleted_subjects_list = [s for s in subject_properties_list if "#" in s.subject_end]
    if len(deleted_subjects_list) > 0:
        show_error_message("Warning", "Obecna wersja programu nie obsługuje dodawania przedmiotów, które nie odbywają się regularnie.")

    unique_deleted_subjects_list = list(set([s.subject_name for s in deleted_subjects_list]))
    for subject in unique_deleted_subjects_list:
        show_error_message("Error", f"Przedmiot {subject} nie został dodany ponieważ zajęcia nie odbywają się regularnie")

    return [s for s in subject_properties_list if "#" not in s.subject_end]
