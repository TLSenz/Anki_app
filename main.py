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
        functions.return_card(functions.cal_score(ask(card)))

        

def ask(card):
    s = input(f"Frage: {card[1]}")
    print(f"Antwort: {card[2]}")
    answer = input(f"Frage: {card[1]}, Antwort: E(easy) G(gut) S(schwer) N(nochmal)")
    if answer == "E":
        return "easy",card[5]
    
    elif answer == "G":
        return "good",card[5]
    
    elif answer == "S":
        return "difficult",card[5]
    
    elif answer == "N":
        return "didnt_know",card[5]

