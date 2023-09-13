# guerrero.py

from Character import Character

class Warrior(Character):
    def __init__(self, name, strength, intelligence, defense, health, sword):
        super().__init__(name, strength, intelligence, defense, health)
        self.sword = sword

    def change_weapon(self):
        option = int(input("Choose a weapon: (1) Valyrian Steel, damage 8. (2) Dragon Slayer, damage 10"))
        if option == 1:
            self.sword = 8
        elif option == 2:
            self.sword = 10
        else:
            print("Incorrect weapon number. No changes made.")

    def attributes(self):
        super().attributes()
        print("·Sword:", self.sword)

    def damage(self, enemy):
        return self.strength * self.sword - enemy.defense

