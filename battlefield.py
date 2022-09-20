import time
from herd import Herd
from fleet import Fleet
import random


def wait ():
    time.sleep(1)

class Battlefield:

    def __init__(self):
        self.round = 1
        self.robotFleet = Fleet()
        self.dinoHerd = Herd()

    def checkIfDead (self, input):                        # Function to check if the active participants in the battle_phase are dead
        if input.health <= 0:                             # and to remove them from their respective herd or fleet
            if input in self.dinoHerd.units_available:
                self.dinoHerd.killDinosaur(input)

            elif input in self.robotFleet.units_available:
                self.robotFleet.killRobot(input)
            
            
    def run_game(self):
        self.display_welcome()
        self.robotFleet.addRobot(self.robotFleet.robotOne) ## Droid is 0
        wait()
        self.robotFleet.addRobot(self.robotFleet.robotTwo) ## Wall-E is 1
        wait()
        self.robotFleet.addRobot(self.robotFleet.robotThree) ## Zenyatta is 2
        wait()
        self.dinoHerd.addDinosaur(self.dinoHerd.velociraptor) ## Velociraptor is 0
        wait()
        self.dinoHerd.addDinosaur(self.dinoHerd.tRex) ## Tyrannosaurus Rex is 1
        wait()
        self.dinoHerd.addDinosaur(self.dinoHerd.stegosaurus) ## Stegosaurus is 2
        print ("")
        time.sleep(3)
        while len(self.dinoHerd.units_available) > 0 and len(self.robotFleet.units_available) > 0:
            self.battle_phase()
        self.display_winner()
        
    
    def display_welcome(self):
        print ("Hello! Welcome to the robot vs dinosaur showdown! Today we have an exciting battle between a herd of dinos and a fleet of robots.")
        print ("")
        timeTilStart = 10
        while timeTilStart > 0:
            print(f"The battle will begin in {timeTilStart} second(s)..",end="\r")
            time.sleep(1)
            timeTilStart -= 1

    def battle_phase(self):
        print(f"Round {self.round}:")
        attackingRobot = random.choice(self.robotFleet.units_available)    # Selects a random robot to participate in this phase of the battle
        randomWeapon = random.choice(attackingRobot.weapons)    # Selects a random weapon for the chosen robot to use
        attackingDino = random.choice(self.dinoHerd.units_available)     # Selects a random dino to participate in this phase of the battle
        attackingRobot.chooseWeapon(randomWeapon)      # Changes the robot's active weapon to the randomly chosen one
        wait()
        print(f"{attackingRobot.name} and {attackingDino.name} are attacking each other!")
        attackingRobot.attack(attackingDino)
        wait()
        print (f"{attackingDino.name} has {attackingDino.health} health left.")
        wait()
        self.checkIfDead(attackingDino)
        if attackingDino.health <= 0:   # This makes the dino being attacked unable to retaliate if it dies after being attacked by the robot
            print(f"{attackingDino.name} was defeated before it had a chance to attack {attackingRobot.name}.")
            print(f"{attackingRobot.name} has {attackingRobot.health} health remaining.")
            pass
        else:
            attackingDino.attack(attackingRobot)
            print (f"{attackingRobot.name} has {attackingRobot.health} health left.")
            self.checkIfDead(attackingRobot)
        self.round += 1
        print ("")
        time.sleep(3)

    def display_winner(self):
        if len(self.robotFleet.units_available) == 0:
            print ("All of the robots have been defeated. The dinosaurs win!")
        elif len(self.dinoHerd.units_available) == 0:
            print ("All of the dinosaurs have been defeated. The robots claim victory!")