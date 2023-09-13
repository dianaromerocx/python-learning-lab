# main.py

from Warrior import Warrior
from Wizard import Wizard

def combat(player_1, player_2):
    turn = 0
    while player_1.is_alive() and player_2.is_alive():
        print("\nTurn", turn)
        print(">>> Action by", player_1.name, ":", sep="")
        player_1.attack(player_2)
        print(">>> Action by", player_2.name, ":", sep="")
        player_2.attack(player_1)
        turn = turn + 1
    if player_1.is_alive():
        print("\n", player_1.name, "has won")
    elif player_2.is_alive():
        print("\n", player_2.name, "has won")
    else:
        print("\nIt's a tie")

character_1 = Warrior("Guts", 20, 10, 4, 100, 4)
character_2 = Wizard("Vanessa", 5, 15, 4, 100, 3)

character_1.attributes()
character_2.attributes()

combat(character_1, character_2)

