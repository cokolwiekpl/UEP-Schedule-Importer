from google_logic.calendar_api_service import add_schedule_to_google_calendar
from google_logic.service_creator import create_service
from gui.gui_notification import show_error_message
from pdf_logic.pdf_reader import check_pdf_file, read_pdf_file, read_semester, read_week_schedule_list_from_pdf
from pdf_logic.semester_properties import get_current_semester
from pdf_logic.subject_properties import get_subject_list
from tkinter import messagebox, filedialog
import tkinter as tk


def import_schedule(file_path):
    pdf_file = read_pdf_file(file_path)
    if check_pdf_file(pdf_file):
        current_semester = get_current_semester(read_semester(pdf_file))
        subject_list = get_subject_list(read_week_schedule_list_from_pdf(file_path), current_semester.semester_start_week)

        for i in subject_list:
            print(i)

        # service = create_service()
        # add_schedule_to_google_calendar(service, subject_list, current_semester)
    else:
        show_error_message("Błąd", "To nie jest plan zajęć UEP")
        print('File is not UEP schedule')




def main():
    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            path_variable.set(file_path)

    def update_button_state():
        if path_variable.get():
            import_button.config(state="normal")
        else:
            import_button.config(state="disabled")

    root = tk.Tk()
    root.title("UEP Schedule Importer")
    root.geometry("500x100")

    path_variable = tk.StringVar()
    path_entry = tk.Entry(root, textvariable=path_variable)
    path_entry.pack(fill="x")

    open_button = tk.Button(root, text="Otwórz plik", command=open_file)
    open_button.pack()

    import_button = tk.Button(root, text="Dodaj plan zajęć do kalendarza", command=lambda: import_schedule(path_variable.get()))
    import_button.pack()

    path_variable.trace("w", lambda *args: update_button_state())
    update_button_state()

    root.mainloop()


if __name__ == "__main__":
    main()
