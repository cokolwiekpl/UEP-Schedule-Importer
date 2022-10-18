import eventAdder
import newCalendarCreator
import subjectsProperties
import currentAcademicSemester
import fileChecker
from google_apis import create_service

CLIENT_SECRET_FILE = '../client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']


def import_schedule(file):
    if fileChecker.check_file(file):
        service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        subject_list = subjectsProperties.create_subject_list(file, currentAcademicSemester.semester_start_week)
        calendar_id = newCalendarCreator.return_calendar_id(newCalendarCreator.create_new_calendar(service), service)
        eventAdder.add_events(subject_list, calendar_id, service)
    else:
        print('File is not UEP schedule')

import_schedule('../plan.pdf')
# def browseFiles():
#     filename = filedialog.askopenfilename(initialdir="/",
#                                           title="Select a File",
#                                           filetypes=[('pdf file', '*.pdf')])
#
#     if filename:
#         ctypes.windll.user32.MessageBoxW(0, "Work in progress, it can take a while.", "Uep Schedule Importer", 1)
#         import_schedule(filename)
#         label_file_explorer.configure(text="Schedule imported")
#         print(filename)
#
#
# window = Tk()
# window.title('Uep Schedule Importer')
# window.geometry("500x500")
# window.config(background="white")
#
# label_file_explorer = Label(window,
#                             text="Add schedule file",
#                             width=100, height=4,
#                             fg="blue")
#
# button_explore = Button(window,
#                         text="Browse Files",
#                         command=browseFiles)
#
# # button_exit = Button(window,
# #                    text="Exit",
# #                    command=exit)
#
#
# label_file_explorer.grid(column=1, row=1)
# button_explore.grid(column=1, row=2)
# # button_exit.grid(column=1, row=3)
# window.mainloop()
#