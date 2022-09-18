import time
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

def checkIfDead (input):                        # Function to check if the active participants in the battle_phase are dead
    if input.health <= 0:                       # and to remove them from their respective herd or fleet
        if input in dinoHerd.units_available:
            dinoHerd.killDinosaur(input)

        elif input in robotFleet.units_available:
            robotFleet.killRobot(input)

def wait ():
    time.sleep(1)

class Battlefield:

    def __init__(self):
        self.round = 1

    def run_game(self):
        self.display_welcome()
        robotFleet.addRobot(robotOne) ## Droid is 0
        wait()
        robotFleet.addRobot(robotTwo) ## Wall-E is 1
        wait()
        robotFleet.addRobot(robotThree) ## Zenyatta is 2
        wait()
        dinoHerd.addDinosaur(velociraptor) ## Velociraptor is 0
        wait()
        dinoHerd.addDinosaur(tRex) ## Tyrannosaurus Rex is 1
        wait()
        dinoHerd.addDinosaur(stegosaurus) ## Stegosaurus is 2
        print ("")
        time.sleep(3)
        while len(dinoHerd.units_available) > 0 and len(robotFleet.units_available) > 0:
            self.battle_phase()
        self.display_winner()
        
    
    def display_welcome(self):
        print ("Hello! Welcome to the robot vs dinosaur showdown! Today we have an exciting battle between a herd of dinos and a fleet of robots.")
        print ("")
        #timeTilStart = 10
        #while timeTilStart > 0:
        #    print(f"The battle will begin in {timeTilStart} second(s)..",end="\r")
        #    time.sleep(1)
         #   timeTilStart -= 1

    def battle_phase(self):
        print(f"Round {self.round}:")
        attackingRobot = random.choice(robotFleet.units_available)    # Selects a random robot to participate in this phase of the battle
        randomWeapon = random.choice(attackingRobot.weapons)    # Selects a random weapon for the chosen robot to use
        attackingDino = random.choice(dinoHerd.units_available)     # Selects a random dino to participate in this phase of the battle
        attackingRobot.chooseWeapon(randomWeapon)      # Changes the robot's active weapon to the randomly chosen one
        wait()
        print(f"{attackingRobot.name} and {attackingDino.name} are attacking each other!")
        attackingRobot.attack(attackingDino)
        wait()
        print (f"{attackingDino.name} has {attackingDino.health} health left.")
        wait()
        checkIfDead(attackingDino)
        if attackingDino.health <= 0:   # This makes the dino being attacked unable to retaliate if it dies after being attacked by the robot
            print(f"{attackingDino.name} was defeated before it had a chance to attack {attackingRobot.name}.")
            print(f"{attackingRobot.name} has {attackingRobot.health} health remaining.")
            pass
        else:
            attackingDino.attack(attackingRobot)
            print (f"{attackingRobot.name} has {attackingRobot.health} health left.")
            checkIfDead(attackingRobot)
        self.round += 1
        print ("")
        time.sleep(3)

    def display_winner(self):
        if len(robotFleet.units_available) == 0:
            print ("All of the robots have been defeated. The dinosaurs win!")
        elif len(dinoHerd.units_available) == 0:
            print ("All of the dinosaurs have been defeated. The robots claim victory!")