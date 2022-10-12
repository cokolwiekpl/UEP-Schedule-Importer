from tabula import read_pdf
from pandas import *


def read_pdf_table(file):
    df_temp = read_pdf(file, stream=True, output_format='DataFrame')
    schedule = df_temp[0]
    schedule.head()
    schedule.to_csv('output.csv')
    print(schedule)
    data = read_csv("output.csv")

    monday_schedule_list = data['Poniedziałek'].tolist()
    tuesday_schedule_list = data['Wtorek'].tolist()
    wednesday_schedule_list = data['Środa'].tolist()
    thursday_schedule_list = data['Czwartek'].tolist()
    friday_schedule_list = data['Piątek'].tolist()


    print('wtorek:', tuesday_schedule_list)
