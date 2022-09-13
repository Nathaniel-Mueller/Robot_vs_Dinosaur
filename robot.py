from weapon import Weapon
import random

sword = Weapon("Sword", 75)
rocketLauncher = Weapon("Rocket Launcher", 250)
laser = Weapon("Laser", 150)
class Robot:

    def __init__(self, robotName):
        self.name = robotName
        self.health = 750
        self.weapons = [sword, rocketLauncher, laser]
        self.active_weapon = sword

    def chooseWeapon (self):
        pass

    def attack (self, dinosaur):
        pass