import datetime


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


current_time = datetime.datetime.now()
month = current_time.month

if month >= 8 or month == 1:
    current_semester = "UEP " + str(current_time.year) + "/" + str(current_time.year + 1) + " Winter term"
    semester_start_month = 'october'
    semester_end = str(current_time.year + 1) + '0228'
else:
    current_semester = "UEP " + str(current_time.year - 1) + "/" + str(current_time.year) + " Summer term"
    semester_start_month = 'february'
    semester_end = str(current_time.year) + '0731'

if semester_start_month == 'october':
    d = datetime.date(current_time.year, 10, 1)
    semester_start_week = [str(next_weekday(d, 0)), str(next_weekday(d, 1)), str(next_weekday(d, 2)),
                           str(next_weekday(d, 3)), str(next_weekday(d, 4))]
elif semester_start_month == 'february':
    d = datetime.date(current_time.year, 2, 1)
    semester_start_week = [str(next_weekday(d, 0)), str(next_weekday(d, 1)), str(next_weekday(d, 2)),
                           str(next_weekday(d, 3)), str(next_weekday(d, 4))]
