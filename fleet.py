from robot import Robot

class Fleet:

    def __init__(self):
        self.type = "Robot"
        self.units_available = []

    def createBot(self):
        robotOne = Robot("Droid")
        robotTwo = Robot("Wall-E")
        robotThree = Robot("Zenyatta")
        
        
    def addRobot(self, botToAdd):
        self.units_available.append (botToAdd)
        print (f"With a shocking {botToAdd.health} health and wielding the {botToAdd.weapons[0].name}, the {botToAdd.weapons [1].name}, and the {botToAdd.weapons[2].name}; {botToAdd.name} has been added to the {self.type} fleet!")
        
    def killRobot(self, botThatDied):
        self.units_available.remove(botThatDied)
        print (f"{botThatDied.name} has died and is no longer part of the {self.type} fleet.")