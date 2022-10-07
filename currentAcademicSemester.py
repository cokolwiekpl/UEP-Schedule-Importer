import datetime

current_time = datetime.datetime.now()
month = current_time.month

if month >= 8 or month ==1:
    current_semester = "UEP Schedule " + str(current_time.year) + "/" + str(current_time.year + 1) + " Winter term"
else:
    current_semester = "UEP Schedule " + str(current_time.year - 1) + "/" + str(current_time.year) + " Summer term"
