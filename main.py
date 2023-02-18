import random

fienderDrept = 0
liv = 10
fiendeLiv = 0
møter = ['monster', 'monster', 'monster', 'kiste'] # 1/4 sjanse for å finne en kiste

def start():
    print("")
    print("Du har", liv, "liv")
    print("Fienden har", fiendeLiv, "liv")
    print("")
    global angrip
    angrip = input("Vil du angripe? ")
    print("")

def tryAgain():
    start()

def notTryAgain():
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
    if møte_type == "monster": # Hvis man møter et monster
        fiendeLiv = random.randint(1, 10)
        start()
        if angrip == "ja": # Hvis du vil angripe
            if liv > fiendeLiv: # Hvis du har mer liv enn fienden
                print("Du drepte fienden")
                fienderDrept += 1
                liv -= fiendeLiv
            elif liv == fiendeLiv: # Hvis du har like mye liv som fienden
                liktLiv = random.randint(1, 2)
                if liktLiv == 1: # Hvis du slår fienden
                    print("Du drepte fienden")
                    fienderDrept += 1
                    liv -= fiendeLiv
                else: # Hvis du ikke slår fienden
                    print("Du er død")
                    print("")
                    prøvIgjen = input("Vil du prøve igjen? ")
                    if prøvIgjen == "ja": # Hvis du vil prøve igjen                
                        tryAgain()
                    else: # Hvis du ikke vil prøve igjen
                        notTryAgain()
            else: # Hvis du har mindre liv enn fienden
                print("Du er død")
                print("")
                prøvIgjen = input("Vil du prøve igjen? ")
                if prøvIgjen == "ja": # Hvis du vil prøve igjen                
                    tryAgain()
                else: # Hvis du ikke vil prøve igjen
                    notTryAgain()
        elif angrip == "nei": # Hvis du ikke vil angripe
            print("Du prøver å stikke av")
            stikkAv = random.randint(1, 2)
            if stikkAv == 1: # Hvis du kommer deg vekk
                print("Du kom deg vekk")
                print("")
            else: # Hvis du ikke kommer deg vekk
                print("Du kom deg ikke vekk")
                print("")
                prøvIgjen = input("Vil du prøve igjen? ")
                if prøvIgjen == "ja": # Hvis du vil prøve igjen
                    tryAgain()
                else: # Hvis du ikke vil prøve igjen
                    notTryAgain()
        else: # Hvis du skriver noe annet enn ja/nei
            print("Du er død")
            fortsett = "nei"
    elif møte_type == "kiste": # Hvis man finner en kiste
        print("Du fant en kiste!")
        liv += 3
        print("Du fant 3 liv og du har nå", liv, "liv")
        print("")
        fortsett = input("Vil du fortsette? ")
