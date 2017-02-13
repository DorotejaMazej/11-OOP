import time
from datetime import date



class Contact:
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        today = date.today()
        birthday = abs(today.year - self.birth_year)
        age = "age: " +str(birthday)
        return age

john = Contact(first_name="John", last_name="Clarck", phone_number=893482309443, birth_year=1979, email="john@clark.com")
marissa = Contact(first_name="Marissa", last_name="Mayer", phone_number=834832429, birth_year=1978, email="marissa@yahoo.com")
bruce = Contact(first_name="Bruce", last_name="Wayne", phone_number=902432309443, birth_year=1939, email="bruce@batman.com")

contact = [john, marissa, bruce]

for person in contact:
    print person.get_full_name()
    print person.get_age()
    print person.phone_number
    print person.email
    print ""



