# mago.py
from Character import Character

class Wizard(Character):
    def __init__(self, name, strength, intelligence, defense, health, book):
        super().__init__(name, strength, intelligence, defense, health)
        self.book = book

    def attributes(self):
        super().attributes()
        print("·Book:", self.book)

    def damage(self, enemy):
        return self.intelligence * self.book - enemy.defense

