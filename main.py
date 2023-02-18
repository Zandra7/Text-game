import random

fienderDrept = 0
liv = 10
fiendeLiv = 0
møter = ['monster', 'monster', 'monster',
         'kiste']  # 1/4 chance to find a chest


def start():
    print("")
    print("Du har", liv, "liv")
    print("Fienden har", fiendeLiv, "liv")
    print("")
    global angrip
    angrip = input("Vil du angripe? ")
    print("")


def tryAgain():  # Try again
    start()


def notTryAgain():  # Not trying again
    if fienderDrept > 1:
        print("Du beseiret", fienderDrept, "fiender")
    else:
        print("Du beseiret bare", fienderDrept, "fiende")
    global fortsett
    fortsett = "nei"


liv = random.randint(5, 10)

fortsett = "ja"
while fortsett == "ja":
    møte_type = random.choice(møter)
    if møte_type == "monster":  # If you encounter a monster
        fiendeLiv = random.randint(1, 10)
        start()
        if angrip == "ja":  # If you want to attack
            if liv > fiendeLiv:  # If you have more health than the enemy
                print("Du drepte fienden")
                fienderDrept += 1
                liv -= fiendeLiv
            elif liv == fiendeLiv:  # If you have the same amount of health as the enemy
                liktLiv = random.randint(1, 2)
                if liktLiv == 1:  # If you beat the enemy
                    print("Du drepte fienden")
                    fienderDrept += 1
                    liv -= fiendeLiv
                else:  # If you don't beat the enemy
                    print("Du er død")
                    print("")
                    prøvIgjen = input("Vil du prøve igjen? ")
                    if prøvIgjen == "ja":  # If you want to try again
                        tryAgain()
                    else:  # If you don't want to try again
                        notTryAgain()
            else:  # If you have less health than the enemy
                print("Du er død")
                print("")
                prøvIgjen = input("Vil du prøve igjen? ")
                if prøvIgjen == "ja":  # If you want to try again
                    tryAgain()
                else:  # If you don't want to try again
                    notTryAgain()
        elif angrip == "nei":  # If you don't want to attack
            print("Du prøver å stikke av")
            stikkAv = random.randint(1, 2)
            if stikkAv == 1:  # If you get away
                print("Du kom deg vekk")
                print("")
            else:  # If you don't get away
                print("Du kom deg ikke vekk")
                print("")
                prøvIgjen = input("Vil du prøve igjen? ")
                if prøvIgjen == "ja":  # If you want to try again
                    tryAgain()
                else:  # If you don't want to try again
                    notTryAgain()
        else:  # If you write something else than "ja/nei"
            print("Du er død")
            fortsett = "nei"
    elif møte_type == "kiste":  # If you find a chest
        print("Du fant en kiste!")
        liv += 3
        print("Du fant 3 liv og du har nå", liv, "liv")
        print("")
        fortsett = input("Vil du fortsette? ")
