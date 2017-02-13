
class Vehicle:
    def __init__(self, badge, model, num_km, service_date):
        self.badge = badge
        self.model = model
        self.num_km = num_km
        self.service_date = service_date

    def get_full_name(self):
        return self.badge + " " + self.model

def list_all_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print "ID" + " " + str(index)
        print car.get_full_name()
        print car.num_km
        print car.service_date
        print ""

def edit_km(vehicles):
    print "Select the vehicle you would like to edit"
    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_name()

    selection_id = raw_input("Please enter the ID of the vehicle you would like to edit")
    selection_vehicle = vehicles[int(selection_id)]

    new_num_km = raw_input("Enter new number of kilometers")
    vehicles.num_km = new_num_km

    print ""
    print "Number of kilometers have been successfully updated"

def edit_servis_date(vehicles):
    print "Select the vehicle you would like to edit"
    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_name()

    selection_id = raw_input("Please enter the ID of the vehicle you would like to edit")
    selection_vehicle = vehicles[int(selection_id)]

    new_service_date = raw_input("Enter new date of service")
    vehicles.service_date = new_service_date

    print ""
    print "Date of service have been successfully updated"

def add_new_vehicle(vehicles):
    badge = raw_input("Enter car's badge")
    model = raw_input("Enter car's model")
    num_km = raw_input("Enter number of car's kilometers")
    service_date = raw_input("Enter date of car's service")

    new = Vehicle(badge=badge, model=model, num_km=num_km, service_date=service_date)
    Vehicle.append(new)

    print ""
    print "Vehicle was successfully added to your list"

def delete_vehicle(vehicles):
    print "Select the vehicle you would like to delete"
    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_name()
        print ""

    selection_id = raw_input("Please enter the car's ID to delete the car")
    selection_vehicle = Vehicle[int(selection_id)]
    Vehicle.remove(selection_vehicle)

    print ""
    print "Vehicle was successfully removed from you list"

def main():
    chevrolet = Vehicle(badge="Chevrolet", model="Corvette", num_km="72 105", service_date="1.5.2014")
    toyota = Vehicle(badge="Toyota", model="Tundra", num_km="12 081", service_date="15.1.2017")
    bmw = Vehicle(badge="BMW", model="3-series", num_km="160 899", service_date="8.10.2016")
    audi = Vehicle(badge="Audi", model="A4", num_km="190 892", service_date="5.6.2017")
    jaguar = Vehicle(badge="Jaguar", model="XE", num_km="40 656", service_date="26.5.2015")

    vehicles = [chevrolet, toyota, bmw, audi, jaguar]


    while True:
        print ""
        print "Select the option: "
        print "a) Show all vehicles in a list"
        print "b) Edit number of driven kilometers"
        print "c) Edit date of service"
        print "d) Add new vehicle to the list"
        print "e) Delete a vehicle from the list"
        print "f) Quit the program"

        selection = raw_input("Please enter your selection (a,b,c,d,e,f)")
        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            edit_km(vehicles)
        elif selection.lower() == "c":
            edit_servis_date(vehicles)
        elif selection.lower() == "d":
            add_new_vehicle(vehicles)
        elif selection.lower() == "e":
            delete_vehicle(vehicles)
        elif selection.lower() == "f":
            print "Thank you for using our program. Goodbye"
            break
        else:
            print "We didn't understand your choice. Try again"
            continue

if __name__ == "__main__":
    main()



