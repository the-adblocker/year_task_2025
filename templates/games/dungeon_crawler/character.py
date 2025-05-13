class Character:
    def __init__(self, name, health, weapon, cash):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.cash = cash


    def attack(self, target):
        target.health -= self.weapon.dmg
        print(f"{self.name} attacked {target.name} with {self.weapon.name}, {target.name} has {target.health} hp left")

        
    def counter(self, target):
        target.health -= (target.weapon.dmg)*0.5
        self.health += (target.weapon.dmg)*0.6
        print(f"{self.name} countered the incoming attack. {target.name} has {target.health} hp left")

