class Fleet:

    def __init__(self):
        self.type = "Robot"
        self.units_available = []

    def addRobot(self, botToAdd):
        self.units_available.append (botToAdd)
        print (f"{botToAdd.name} has been added to the {self.type} fleet!")
        
    def killRobot(self, botThatDied):
        self.units_available.remove(botThatDied)
        print (f"{botThatDied.name} has died and is no longer part of the {self.type} fleet.")