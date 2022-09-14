from tabnanny import check
from herd import Herd
from fleet import Fleet
from dinosaur import Dinosaur
from robot import Robot
import random

robotFleet = Fleet()
dinoHerd = Herd()
velociraptor = Dinosaur("Velociraptor", 200)
tRex = Dinosaur("Tyrannosaurus Rex", 400)
stegosaurus = Dinosaur("Stegosaurus", 300)
robotOne = Robot("Droid")
robotTwo = Robot("Wall-E")
robotThree = Robot("Zenyatta")

def checkIfDead (input):
    if input.health <= 0:
        if input in dinoHerd.units_available:
            dinoHerd.killDinosaur(input)

        elif input in robotFleet.units_available:
            robotFleet.killRobot(input)
        
class Battlefield:

    def __init__(self):
        self.fleet = robotFleet
        self.herd = dinoHerd

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
        attackingRobot = random.choice(robotFleet.units_available)
        randomWeapon = random.choice(attackingRobot.weapons)
        attackingDino = random.choice(dinoHerd.units_available)
        attackingRobot.chooseWeapon(randomWeapon.name)
        print(f"{attackingRobot.name} and {attackingDino.name} are attacking each other!")
        attackingRobot.attack(attackingDino)
        print (f"{attackingDino.name} has {attackingDino.health} health left.")
        checkIfDead(attackingDino)
        if attackingDino.health <= 0:
            print(f"{attackingDino.name} was defeated before it had a chance to attack {attackingRobot.name}.")
            print(f"{attackingRobot.name} has {attackingRobot.health} health remaining.")
            pass
        else:
            attackingDino.attack(attackingRobot)
            print (f"{attackingRobot.name} has {attackingRobot.health} health left.")
            checkIfDead(attackingRobot)

    def display_winner(self):
        if len(robotFleet.units_available) == 0:
            print ("All of the robots have been defeated. The dinosaurs win!")
        elif len(dinoHerd.units_available) == 0:
            print ("All of the dinosaurs have been defeated. The robots claim victory!")