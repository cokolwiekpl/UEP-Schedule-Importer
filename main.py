import fitz
from tabula import read_pdf
from pandas import *
#################################################################################
import eventAdder
import newCalendarCreator
import subjectsProperties
import currentAcademicSemester

subject_list = subjectsProperties.create_subject_list('plan.pdf', currentAcademicSemester.semester_start_week)
print(subject_list)


calendar_id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar())
eventAdder.add_events(subject_list, calendar_id)
#################################################################################


# subjectsProperties.create_subject_list('plan.pdf', currentAcademicSemester.semester_start_week)
# print(currentAcademicSemester.semester_start_week)
