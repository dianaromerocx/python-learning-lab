# character.py

class Character:
    def __init__(self, name, strength, intelligence, defense, health):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.health = health

    def attributes(self):
        print(self.name, ":", sep="")
        print("·Strength:", self.strength)
        print("·Intelligence:", self.intelligence)
        print("·Defense:", self.defense)
        print("·Health:", self.health)

    def level_up(self, strength, intelligence, defense):
        self.strength = self.strength + strength
        self.intelligence = self.intelligence + intelligence
        self.defense = self.defense + defense

    def is_alive(self):
        return self.health > 0

    def die(self):
        self.health = 0
        print(self.name, "has died")

    def damage(self, enemy):
        return self.strength - enemy.defense

    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.health = enemy.health - damage
        print(self.name, "has dealt", damage, "points of damage to", enemy.name)
        if enemy.is_alive():
            print(enemy.name, "'s health is", enemy.health)
        else:
            enemy.die()

