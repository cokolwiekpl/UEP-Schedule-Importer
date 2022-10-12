import fitz
from tabula import read_pdf
from pandas import *
#################################################################################
import eventAdder
import newCalendarCreator
import subjectsProperties

subject_list = [['nazwa przedmiotu 1', 'CEUE 1', '2022-10-08T12:00:00', '2022-10-08T13:00:00'],
                 ['nazwa przedmiotu 2', 'CEUE 2', '2022-10-09T12:00:00', '2022-10-09T13:00:00']]

# calendar_id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar())
# eventAdder.add_events(subjects_list, calendar_id)
#################################################################################

# subjectsProperties.return_subject_list('plan.pdf')
subjectsProperties.create_raw_subject_list('plan.pdf')

# file = 'plan.pdf'
# stream = True
# output_format = 'DataFrame'
# df_temp = read_pdf(file, stream=stream, output_format=output_format)
# schedule = df_temp[0]
# schedule.head()
# schedule.to_csv('output.csv')

# def read_pdf_table(file, stream, output_format):
#     df_temp = read_pdf(file, stream=stream, output_format=output_format)
#     schedule = df_temp[0]
#     schedule.head()
#     schedule.to_csv('output.csv')
#
#
# read_pdf_table('plan.pdf', True, 'DataFrame')


