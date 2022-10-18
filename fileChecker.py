from PyPDF2 import PdfReader


def check_file(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    if (text.find("zimowy")) >= 0:
        return True

    if (text.find("letni")) >= 0:
        return True

    if (text.find("letni")) == -1 and (text.find("zimowy")) == -1:
        return False
