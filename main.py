import random

fienderDrept = 0
liv = 10
fiendeLiv = 0

def start():
    print("")
    print("Du har", liv, "liv")
    print("Fienden har", fiendeLiv, "liv")
    print("")
    global angrip
    angrip = input("Vil du angripe? ")
    print("")

liv = random.randint(5,10)
fortsett = "ja"
while fortsett == "ja":
    fiendeLiv = random.randint(1, 10)

    start()

    if angrip == "ja":
        if liv > fiendeLiv:
            print("Du drepte fienden")
            fienderDrept += 1
            liv -= fiendeLiv
        else:
            print("Du er død")
            print("")
            prøvIgjen = input("Vil du prøve igjen? ")
            if prøvIgjen == "ja":
                start()
            else:
                print("Du beseiret", fienderDrept, "fiende(r)")
                fortsett = "nei"
    elif angrip == "nei":
        print("Du prøver å stikke av")
        stikkAv = random.randint(1, 2)
        if stikkAv == 1:
            print("Du kom deg vekk")
        else:
            print("Du kom deg ikke vekk")
            prøvIgjen = input("Vil du prøve igjen? ")
            if prøvIgjen == "ja":
                start()
            else:
                if fienderDrept > 1:
                    print("Du beseiret", fienderDrept, "fiender")
                else:
                    print("Du beseiret bare", fienderDrept, "fiende")
                fortsett = "nei"
    else:
        print("Du er død")



