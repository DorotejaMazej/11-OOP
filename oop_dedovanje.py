class Dad(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        print "%s %s" %(self.first_name, self.last_name)

class Child(Dad):
    def __init__(self, first_name, last_name, toy):
        self.first_name = first_name
        self.last_name = last_name
        self.toy = toy

johnny = Child(first_name="Johnny", last_name="Brown", toy="Travtor")
johnny.full_name()

