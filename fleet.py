class Fleet:

    def __init__(self):
        self.type = "Robot"
        self.units_available = []

    def addRobot(self, botToAdd):
        self.units_available.append (botToAdd)
        print (f"{botToAdd} added to the {self.type} fleet!")