class Herd:
    
    def __init__(self):
        self.type = "Dinosaur"
        self.units_available = []

    def addDinosaur(self, dinoToAdd):
        self.units_available.append(dinoToAdd)
        print (f"{dinoToAdd.name} added to the {self.type} herd!")