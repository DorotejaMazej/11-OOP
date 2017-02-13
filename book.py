class Contact:
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

def list_all_contacts(contacts):
    for index, person in enumerate(contacts,1):
        print "ID" + str(index)
        print person.get_full_name()
        print person.birth_year
        print person.email
        print ""

def add_contact(contacts):
    first_name = raw_input("Please enter a contact's first name.")
    last_name = raw_input("Please enter a contact's last name.")
    phone =raw_input("Please enter a contact's phone number.")
    birth_year = raw_input("Please enter a contact's birth year.")
    email = raw_input("Please enter a contact's email.")

    new = Contact(first_name=first_name, last_name=last_name, phone_number=phone, birth_year=birth_year, email=email)
    contacts.append(new)

    print ""
    print new.get_full_name() + "was successfully added to your contacts"

def edit_contact(contacts):
    print "Select the contact you would like to edit."
    for index, person in enumerate(contacts,1):
        print str(index) + ") " + person.get_full_name()

    selection_id = raw_input("Please select the ID of the contact you would like to edit.")
    selection_contact = contacts[int(selection_id)]

    new_first_name = raw_input("Plese enter contact's new first name")
    selection_contact.first_name = new_first_name

    print ""
    print "First name updated"

    new_last_name = raw_input("Please enter contact's last name")
    selection_contact.new_last_name = new_last_name

    print ""
    print "Last name updated"

    new_phone_number = raw_input("Please enter contact's nes phone number")
    selection_contact.new_phone_number = new_phone_number

    print ""
    print "Phone number updated"

    new_email = raw_input("Please enter a contact new email")
    selection_contact.email = new_email

    print ""
    print "Email updated"


def delete(contacts):
    print "Select the contact you would like to delete"

    for index, person in enumerate(contacts,1):
        print str(index) + ") " + person.get_full_name()

    selection_id = raw_input("Please select the ID of the contact you would like to edit.")
    selection_contact = contacts[int(selection_id)]
    contacts.remove(selection_contact)

    print ""
    print "Contact was successfully removed from contact list."

def main():
    print "Welcome to your contact book"
    print ""

    john = Contact(first_name="John", last_name="Clark", phone_number="89348239429", birth_year="1979", email="john@clarck.com")
    marissa = Contact(first_name="Marissa", last_name="Mayer", phone_number="83483204032", birth_year="1978", email="marissa@yahoo.com")
    bruce = Contact(first_name="Bruce", last_name="Wayne", phone_number="902432309443", birth_year="1939", email="bruce@batman.com")

    contacts = [john, marissa, bruce]

    while True:
        print ""
        print "Select the options:"
        print "a) show contacts in a list"
        print "b) Add a new contact"
        print "c) Edit a contact"
        print "d) Delete a contact"
        print "e) Quit program"
        print ""

        selection = raw_input("Please enter your selection (a,b,c,d,e)")
        print ""

        if selection.lower() == "a":
            list_all_contacts(contacts)
        elif selection.lower() == "b":
            add_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delete(contacts)
        elif selection.lower() == "e":
            print "Thank you for using our program. Goodbye"
            break
        else:
            print "We didn't understand your selection. Try again"
            continue

if __name__ == "__main__":
    main()









