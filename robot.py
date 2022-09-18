import random
from weapon import Weapon
import time as t

knife = Weapon("Knife", 50)
sword = Weapon("Sword", 75)
gun = Weapon("Gun", 100)
laser = Weapon("Laser", 150)
rocketLauncher = Weapon("Rocket Launcher", 250)

weaponsList = [knife, sword, gun, laser, rocketLauncher]

class Robot:

    def __init__(self, robotName):
        self.name = robotName
        self.health = 750
        self.weapons = random.sample(weaponsList, 3)
        self.active_weapon = self.weapons[0]

    def chooseWeapon (self, newWeapon):
        print (f"{self.name} is selecting a weapon!")
        t.sleep(1)
        self.active_weapon = newWeapon
        print (f"{self.active_weapon.name} selected!")


    def attack (self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power