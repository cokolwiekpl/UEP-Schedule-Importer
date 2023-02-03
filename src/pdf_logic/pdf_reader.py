from PyPDF2 import PdfReader
from pandas import read_csv
from tabula import read_pdf


def check_pdf_file(file_text: str) -> bool:
    if (file_text.find("zimowy")) >= 0:
        return True

    if (file_text.find("letni")) >= 0:
        return True

    if (file_text.find("letni")) == -1 and (file_text.find("zimowy")) == -1:
        return False


def read_semester(file_text: str) -> str:
    if (file_text.find("zimowy")) >= 0:
        return "zimowy"

    if (file_text.find("letni")) >= 0:
        return "letni"


def read_pdf_file(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def read_week_schedule_list_from_pdf(file_path: str) -> list:
    df_temp = read_pdf(file_path, stream=True, output_format='DataFrame')
    schedule = df_temp[0]
    schedule.head()

    schedule.to_csv('resources/output.csv')
    data = read_csv("resources/output.csv")
    type(data)

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
