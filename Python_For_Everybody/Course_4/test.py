'''
class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print("So far", self.x)

an = PartyAnimal()

#an.party()
#print("Type", type(an))
#print("Dir", dir(an))
'''
'''
class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x += 1
        print("So far", self.x)

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print("an contains", an)
'''

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

#    def __del__(self):
#        print("I am destructed", self.x)
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
