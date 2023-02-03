import webbrowser

from google_logic.calendar_api_service import add_schedule_to_google_calendar
from google_logic.service_creator import create_service
from pdf_logic.pdf_reader import check_pdf_file, read_pdf_file, read_semester, read_week_schedule_list_from_pdf
from pdf_logic.semester_properties import get_current_semester
from pdf_logic.subject_properties import get_subject_list
from tkinter import messagebox, filedialog
import tkinter as tk

APP_VERSION = "1.0.0"


def import_schedule(file_path):
    pdf_file = read_pdf_file(file_path)
    if check_pdf_file(pdf_file):
        messagebox.showwarning("Uwaga",
                               "Obecna wersja programu nie obsługuje dodawania przedmiotów, które odbywają się nieregularnie (np. przedmioty odbywające się co dwa tygodnie)."
                               "Takie przedmioty należy dodać ręcznie.")
        current_semester = get_current_semester(read_semester(pdf_file))
        subject_list = get_subject_list(read_week_schedule_list_from_pdf(file_path), current_semester.semester_start_week)

        for i in subject_list:
            print(i)

        print('--')
        service = create_service()
        messagebox.showinfo("Sukces autoryzacji", "Gdy dodawanie się zakończy zostaniesz powiadomiony. Może to chwilę potrwać. Nie wyłączaj programu!")
        if add_schedule_to_google_calendar(service, subject_list, current_semester):
            messagebox.showinfo("Sukces", "Plan zajęć został dodany do kalendarza")
    else:
        messagebox.showerror("Błąd", "To nie jest plan zajęć UEP")
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
    root.title(f"UEP Schedule Importer ver. {APP_VERSION}")
    root.geometry("500x100")

    menu = tk.Menu(root)
    root.config(menu=menu)

    # file_menu = tk.Menu(menu)
    # menu.add_cascade(label="Plik", menu=file_menu)

    main_menu = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Menu", menu=main_menu)
    main_menu.add_command(label="Repozytorium GitHub", command=lambda: webbrowser.open("https://github.com/cokolwiekpl/UEP-Schedule-Importer"))
    main_menu.add_command(label="Kontakt", command=lambda: messagebox.showinfo("Kontakt", "stanislav.kumor+UepScheduleImporter@gmail.com"))

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
