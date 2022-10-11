import fitz


def return_subject_list(schedule):
    words_dict_list = read_pdf(schedule)

    monday_coordinates = read_day_coordinates(words_dict_list, 'monday')
    tuesday_coordinates = read_day_coordinates(words_dict_list, 'tuesday')
    wednesday_coordinates = read_day_coordinates(words_dict_list, 'wednesday')
    thursday_coordinates = read_day_coordinates(words_dict_list, 'thursday')
    friday_coordinates = read_day_coordinates(words_dict_list, 'friday')
    subject_coordinates_list = clear_words_dict_list(words_dict_list)

    week_schedule_list = create_week_schedule_list(monday_coordinates,
                                                   tuesday_coordinates,
                                                   wednesday_coordinates,
                                                   thursday_coordinates,
                                                   friday_coordinates,
                                                   subject_coordinates_list)
    # print(week_schedule_list)
    clear_week_schedule_list(week_schedule_list)


def clear_week_schedule_list(week_schedule_list): # to można użyć w create_week_schedule_list
    for day in week_schedule_list:
        print(day)
        for i in day:
            print(i)
            # łączyć pomiędzy godziną, a salą, a nazwie budynku usuwać do godziny


def create_week_schedule_list(monday_coordinates,
                              tuesday_coordinates,
                              wednesday_coordinates,
                              thursday_coordinates,
                              friday_coordinates,
                              subject_coordinates_list):
    monday_schedule_list = ['monday']
    tuesday_schedule_list = ['tuesday']
    wednesday_schedule_list = ['wednesday']
    thursday_schedule_list = ['thursday']
    friday_schedule_list = ['friday']
    for x in subject_coordinates_list:
        if monday_coordinates + 50 > x[0] > monday_coordinates - 50:
            monday_schedule_list.append(x[1])
        if tuesday_coordinates + 50 > x[0] > tuesday_coordinates - 50:
            tuesday_schedule_list.append(x[1])
        if wednesday_coordinates + 50 > x[0] > wednesday_coordinates - 50:
            wednesday_schedule_list.append(x[1])
        if thursday_coordinates + 50 > x[0] > thursday_coordinates - 50:
            thursday_schedule_list.append(x[1])
        if friday_coordinates + 50 > x[0] > friday_coordinates - 50:
            friday_schedule_list.append(x[1])
    week_schedule_list = [monday_schedule_list,
                          tuesday_schedule_list,
                          wednesday_schedule_list,
                          thursday_schedule_list,
                          friday_schedule_list]
    return week_schedule_list


def clear_top_words_dict_list(words_dict_list):
    for x in words_dict_list:
        if x[4] == 'Poniedziałek':
            for i in range(0, words_dict_list.index(x)):
                del words_dict_list[0]
    return words_dict_list


def clear_words_dict_list(words_dict_list):
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

    words_dict_list = clear_top_words_dict_list(words_dict.get(0))  # words_dict.get(0)
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
