# Ethan Lawrence
# nov 13 2024
# W3 schools classes/objects

class Character:
    def __init__(self, max_health, power):
        self.power = power
        self.max_health = max_health
        self.health = max_health
    
    def attacked(self, damage):
        self.health -= damage
        if self.health > self.max_health:
            self.health = self.max_health
        print(self.health)

bat = Character(100, 10)
print(bat.health)
bat.attacked(14)