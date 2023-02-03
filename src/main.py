from google_logic.calendar_api_service import add_schedule_to_google_calendar
from google_logic.service_creator import create_service
from pdf_logic.pdf_reader import check_pdf_file, read_pdf_file, read_semester, read_week_schedule_list_from_pdf
from pdf_logic.semester_properties import get_current_semester
from pdf_logic.subject_properties import get_subject_list


def import_schedule(file_path):
    pdf_file = read_pdf_file(file_path)
    if check_pdf_file(pdf_file):
        current_semester = get_current_semester(read_semester(pdf_file))
        service = create_service()
        subject_list = get_subject_list(read_week_schedule_list_from_pdf(file_path), current_semester.semester_start_week)
        add_schedule_to_google_calendar(service, subject_list, current_semester)
    else:
        print('File is not UEP schedule')


def main():
    import_schedule('resources/plan.pdf')


if __name__ == "__main__":
    main()
