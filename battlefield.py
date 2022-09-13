from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot
import random

robotFleet = Fleet()
dinoHerd = Herd()
velociraptor = Dinosaur("Velociraptor", 75)
tRex = Dinosaur("Tyrannosaurus Rex", 350)
stegosaurus = Dinosaur("Stegosaurus", 200)
robotOne = Robot("Droid")
robotTwo = Robot("Wall-E")
robotThree = Robot("Zenyatta")


class Battlefield:

    def __init__(self):
        pass

    def run_game(self):
        robotFleet.addRobot(robotOne) ## Droid is 0
        robotFleet.addRobot(robotTwo) ## Wall-E is 1
        robotFleet.addRobot(robotThree) ## Zenyatta is 2
        dinoHerd.addDinosaur(velociraptor) ## Velociraptor is 0
        dinoHerd.addDinosaur(tRex) ## Tyrannosaurus Rex is 1
        dinoHerd.addDinosaur(stegosaurus) ## Stegosaurus is 2
    
    def display_welcome(self):
        print ("Hello! Welcome to the robot vs dinosaur showdown! Today we have an exciting battle between a herd of dinos and a fleet of robots.")

    def battle_phase(self):
        a = 0
        while a < len(robotFleet.units_available) or a < len(dinoHerd.units_available):
            attackingRobot = random.choice(robotFleet.units_available)
            randomWeapon = random.choice(attackingRobot.weapons)
            defendingRobot = random.choice(robotFleet.units_available)
            attackingDino = random.choice(dinoHerd.units_available)
            defendingDino = random.choice(dinoHerd.units_available)
            attackingRobot.attack(defendingDino)
            print (f"{defendingDino.name} has {defendingDino.health} health left!")
            attackingRobot.chooseWeapon(randomWeapon.name)
            if defendingDino.health <= 0:
                dinoHerd.killDinosaur(defendingDino)
            

    def display_winner(self):
        pass