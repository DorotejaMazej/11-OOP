import time
from datetime import date

today = date.today()

le = 1979
my_birthday = date(1979, 2, 6)
time_to_brth = today.year - my_birthday.year
l = str(time_to_brth) + " " + "years" + " " + "old"
print l