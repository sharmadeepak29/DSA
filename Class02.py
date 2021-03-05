class Character():
    def __init__(self, name):
        self.health = 100
        self.name = name

    def printName(self):
        print(self.name)

class Forge:
    def __init__(self, forgeName):
        self.name = forgeName

class Blacksmith(Character):
    def __init__(self, name, forgeName):
        super(Blacksmith, self).__init__(name)
        self.forge = Forge(forgeName)


bs = Blacksmith("Deepak", "Sharma")
bs.printName()
print(bs.forge.name)
