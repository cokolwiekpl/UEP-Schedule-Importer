import fitz


def return_subject_list(schedule):
    words_dict_list = read_pdf(schedule)

    monday_coordinates = read_day_coordinates(words_dict_list, 'monday')
    tuesday_coordinates = read_day_coordinates(words_dict_list, 'tuesday')
    wednesday_coordinates = read_day_coordinates(words_dict_list, 'wednesday')
    thursday_coordinates = read_day_coordinates(words_dict_list, 'thursday')
    friday_coordinates = read_day_coordinates(words_dict_list, 'friday')
    subject_coordinates_list = clear_list(words_dict_list)
    print(words_dict_list)
    print(monday_coordinates)
    print(tuesday_coordinates)
    print(wednesday_coordinates)
    print(thursday_coordinates)
    print(friday_coordinates)
    print('----')
    for x in subject_coordinates_list:
        print(x)
    print('----')

    create_tuesday_schedule_list(tuesday_coordinates, subject_coordinates_list)


def create_monday_schedule_list(monday_coordinates, subject_coordinates_list):
    print('monday')


def create_tuesday_schedule_list(tuesday_coordinates, subject_coordinates_list):
    for x in subject_coordinates_list:
        if tuesday_coordinates + 50 > x[0] > tuesday_coordinates - 50:
            # 192 < 249 or 192 > 149
            print(x)

    # print(x)
    print('tuesday')


def create_wednesday_schedule_list(wednesday_coordinates, subject_coordinates_list):
    print('wednesday')


def create_thursday_schedule_list(thursday_coordinates, subject_coordinates_list):
    print('thursday')


def create_friday_schedule_list(friday_coordinates, subject_coordinates_list):
    print('friday')


def clear_top_list(list_to_clear):
    for x in list_to_clear:
        if x[4] == 'Poniedziałek':
            for i in range(0, list_to_clear.index(x)):
                del list_to_clear[0]
    return list_to_clear


def clear_list(words_dict_list):
    subject_list_with_coordinates = []
    for x in words_dict_list:
        subject_coordinates = x[0], x[4]
        subject_list_with_coordinates.append(subject_coordinates)
    for i in range(0, 5):
        del subject_list_with_coordinates[0]
    return subject_list_with_coordinates


def read_pdf(schedule):
    with fitz.open(
            'plan.pdf') as document:  # z tego sprawdzić które zajęcia do którego dnia (na podstawie pierwszej zmiennej
        words_dict = {}
        for page_number, page in enumerate(document):
            words = page.get_text("words")
            words_dict[page_number] = words

    words_dict_list = clear_top_list(words_dict.get(0))  # words_dict.get(0)
    return words_dict_list


def read_day_coordinates(words_dict_list, day_name):
    for x in words_dict_list:
        if x[4] == 'Poniedziałek' and day_name == 'monday':
            return x[0]
        if x[4] == 'Wtorek' and day_name == 'tuesday':
            return x[0]
        if x[4] == 'Środa' and day_name == 'wednesday':
            return x[0]
        if x[4] == 'Czwartek' and day_name == 'thursday':
            return x[0]
        if x[4] == 'Piątek' and day_name == 'friday':
            return x[0]

# https://www.w3schools.com/python/python_tuples.asp
