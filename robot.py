class Robot:

    from weapon import Weapon

    sword = Weapon("Sword", 75)
    rocketLauncher = Weapon("Rocket Launcher", 250)
    laser = Weapon("Laser", 150)

    def __init__(self, robotName):
        self.name = robotName
        self.health = 750
        self.active_weapon = ""