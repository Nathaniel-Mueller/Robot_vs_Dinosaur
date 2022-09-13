class Herd:
    
    def __init__(self):
        self.type = "Dinosaur"
        self.units_available = []

    def addDinosaur(self, dinoToAdd):
        self.units_available.append(dinoToAdd)
        print (f"{dinoToAdd.name} added to the {self.type} herd!")

    def killDinosaur(self, dinoThatDied):
        self.units_available.remove(dinoThatDied)
        print (f"{dinoThatDied} has died and is no longer part of the {self.type} herd.")