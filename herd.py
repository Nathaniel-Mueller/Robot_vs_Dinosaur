from dinosaur import Dinosaur
import time

class Herd:
    
    def __init__(self):
        self.type = "Dinosaur"
        self.units_available = []
        self.createDino()
        
    def createDino (self):
        velociraptor = Dinosaur("Velociraptor", 200)
        tRex = Dinosaur("Tyrannosaurus Rex", 400)
        stegosaurus = Dinosaur("Stegosaurus", 300)
        self.addDinosaur(velociraptor)
        self.addDinosaur(tRex)
        self.addDinosaur(stegosaurus)

    def addDinosaur(self, dinoToAdd):
        self.units_available.append(dinoToAdd)
        print (f"With a whopping {dinoToAdd.health} health, and dealing {dinoToAdd.attack_power} damage, {dinoToAdd.name} has been added to the {self.type} herd!")
        time.sleep(1)

    def killDinosaur(self, dinoThatDied):
        self.units_available.remove(dinoThatDied)
        print (f"{dinoThatDied.name} has died and is no longer part of the {self.type} herd.")