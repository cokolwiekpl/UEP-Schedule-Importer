from tabula import read_pdf
from pandas import *


def read_pdf_table(file):
    df_temp = read_pdf(file, stream=True, output_format='DataFrame')
    schedule = df_temp[0]
    schedule.head()
    schedule.to_csv('output.csv')
    data = read_csv("./output.csv")

    raw_monday_schedule_list = data['Poniedziałek'].tolist()
    raw_tuesday_schedule_list = data['Wtorek'].tolist()
    raw_wednesday_schedule_list = data['Środa'].tolist()
    raw_thursday_schedule_list = data['Czwartek'].tolist()
    raw_friday_schedule_list = data['Piątek'].tolist()

    week_schedule_list = [raw_monday_schedule_list,
                          raw_tuesday_schedule_list,
                          raw_wednesday_schedule_list,
                          raw_thursday_schedule_list,
                          raw_friday_schedule_list,
                          ]

    return week_schedule_list


def create_raw_subject_list(schedule_pdf):
    week_schedule_list = read_pdf_table(schedule_pdf)
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
                        subject_start = 'mondayT' + subject_date[0] + ':00'
                        subject_end = 'mondayT' + subject_date[1] + ':00'
                    elif (week_schedule_list.index(day)) == 1:
                        subject_start = 'tuesdayT' + subject_date[0] + ':00'
                        subject_end = 'tuesdayT' + subject_date[1] + ':00'
                    elif (week_schedule_list.index(day)) == 2:
                        subject_start = 'wednesdayT' + subject_date[0] + ':00'
                        subject_end = 'wednesdayT' + subject_date[1] + ':00'
                    elif (week_schedule_list.index(day)) == 3:
                        subject_start = 'thursdayT' + subject_date[0] + ':00'
                        subject_end = 'thursdayT' + subject_date[1] + ':00'
                    elif (week_schedule_list.index(day)) == 4:
                        subject_start = 'fridayT' + subject_date[0] + ':00'
                        subject_end = 'fridayT' + subject_date[1] + ':00'
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
                    subject_properties = [subject_name, subject_location, subject_start, subject_end]

                    subject_properties_list.append(subject_properties)
    return subject_properties_list


def create_subject_list(schedule_pdf, semester_start_week):
    subject_properties_list = create_raw_subject_list(schedule_pdf)
    for i in subject_properties_list:
        if 'monday' in i[2]:
            i[2] = i[2].replace("monday", semester_start_week[0])
            i[3] = i[3].replace("monday", semester_start_week[0])
        if 'tuesday' in i[2]:
            i[2] = i[2].replace("tuesday", semester_start_week[1])
            i[3] = i[3].replace("tuesday", semester_start_week[1])
        if 'wednesday' in i[2]:
            i[2] = i[2].replace("wednesday", semester_start_week[2])
            i[3] = i[3].replace("wednesday", semester_start_week[2])
        if 'thursday' in i[2]:
            i[2] = i[2].replace("thursday", semester_start_week[3])
            i[3] = i[3].replace("thursday", semester_start_week[3])
        if 'friday' in i[2]:
            i[2] = i[2].replace("friday", semester_start_week[4])
            i[3] = i[3].replace("friday", semester_start_week[4])
    return subject_properties_list
