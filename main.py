import fitz

#################################################################################
import eventAdder
import newCalendarCreator
import subjectsProperties

subjects_list = [['nazwa przedmiotu 1', 'CEUE 1', '2022-10-08T12:00:00', '2022-10-08T13:00:00'],
                 ['nazwa przedmiotu 2', 'CEUE 2', '2022-10-09T12:00:00', '2022-10-09T13:00:00']]

# calendar_id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar())
# eventAdder.add_events(subjects_list, calendar_id)
#################################################################################

subjectsProperties.return_subject_list('plan.pdf')


