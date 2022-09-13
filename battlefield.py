from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot

robotFleet = Fleet()
dinoHerd = Herd()
velociraptor = Dinosaur("Velociraptor", 75)
tRex = Dinosaur("Tyrannosaurus Rex", 350)
stegosaurus = Dinosaur("Stegosaurus", 200)
robotOne = Robot("Droid")
robotTwo = Robot("Wall-E")
robotThree = Robot("Zenyatta")
robotFleet.addRobot(robotOne)
robotFleet.addRobot(robotTwo)
robotFleet.addRobot(robotThree)
dinoHerd.addDinosaur(velociraptor)
dinoHerd.addDinosaur(tRex)
dinoHerd.addDinosaur(stegosaurus)

class Battlefield:

    def __init__(self):
        pass

    def run_game(self):
        pass
    
    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass