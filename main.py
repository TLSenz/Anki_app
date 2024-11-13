import random as r
import functions
from functions import aktualsieren


def main():
    aktualsieren()
    print(f"Hallo")
    print(f"Heute hast du {len(functions.checkcards())} zu lernen")


def ask_questions():
    count = 0
    asking_cards = function.checkcard()
    while count <= len(asking_cards):
        card = functions.get_cardarray(r.choice(0,len(asking_cards)-1))

        



