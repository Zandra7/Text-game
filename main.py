import random

fienderDrept = 0
liv = random.randint(1, 10)
fiendeLiv = 0

def start():
    print("")
    print("Du har", liv, "liv")
    print("Fienden har", fiendeLiv, "liv")
    print("")
    global angrip
    angrip = input("Vil du angripe? ")
    print("")

fortsett = "ja"
while fortsett == "ja":
    liv = random.randint(1,10)
    fiendeLiv = random.randint(1, 10)

    start()

    if angrip == "ja":
        if liv > fiendeLiv:
            print("Du drepte fienden")
            fienderDrept += 1
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
                print("Du beseiret", fienderDrept, "fiende(r)")
                fortsett = "nei"
            
    else:
        print("Du er død")



