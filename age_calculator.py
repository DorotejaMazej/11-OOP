import time
from datetime import date

today = date.today()

my_birthday = date(today.year, 1, 24)

if my_birthday < today:
    my_birthday = my_birthday.replace(year=1979)
    print my_birthday
    time_to_birthday = abs(my_birthday - today)
    tt= abs(today.year-my_birthday.year)
    print tt
