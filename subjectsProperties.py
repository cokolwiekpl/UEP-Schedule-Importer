from tabula import read_pdf
from pandas import *


def read_pdf_table(file):
    df_temp = read_pdf(file, stream=True, output_format='DataFrame')
    schedule = df_temp[0]
    schedule.head()
    schedule.to_csv('output.csv')
    data = read_csv("output.csv")

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


subject_list_tat = [['nazwa przedmiotu 1', 'CEUE 1', '2022-10-08T12:00:00', '2022-10-08T13:00:00'],
                    ['nazwa przedmiotu 2', 'CEUE 2', '2022-10-09T12:00:00', '2022-10-09T13:00:00']]


def create_raw_subject_list(schedule_pdf):
    week_schedule_list = read_pdf_table(schedule_pdf)
    subject_list = []

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

                    if "Lab" in next_property or "Ćwi" in next_property or "Wyk" in next_property:
                        subject_name = day[day.index(i) + 1]
                        subject_location = day[day.index(i) + 2]
                    else:
                        subject_name = day[day.index(i) + 1] + ' ' + day[day.index(i) + 2]
                        subject_location = day[day.index(i) + 3]

                if subject_name != '':
                    subject_properties = [subject_name, subject_location, subject_start, subject_end]
                    # print(subject_properties)

                    subject_list.append(subject_properties)
                    # print(subject_list)
    for i in subject_list:
        print(i)