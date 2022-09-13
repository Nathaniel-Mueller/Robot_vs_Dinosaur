from weapon import Weapon

sword = Weapon("Sword", 75)
rocketLauncher = Weapon("Rocket Launcher", 250)
laser = Weapon("Laser", 150)

class Robot:

    def __init__(self, robotName):
        self.name = robotName
        self.health = 750
        self.weapons = [sword, rocketLauncher, laser]
        self.active_weapon = sword

    def chooseWeapon (self, newWeapon):
        if newWeapon == "Sword":
            self.active_weapon = self.weapons[0]
            print (f"{self.active_weapon.name} selected!")
        elif newWeapon == "Rocket Launcher":
            self.active_weapon = self.weapons[1]
            print (f"{self.active_weapon.name} selected!")
        elif newWeapon == "Laser":
            self.active_weapon = self.weapons[2]
            print(f"{self.active_weapon.name} selected!")

    def attack (self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power