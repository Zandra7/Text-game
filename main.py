import random

EnemiesKilled = 0
health = 10
enemyHealth = 0
encounters = ['monster', 'monster', 'monster',
         'chest']  # 1/4 chance to find a chest


def start():
    print("")
    print("You have", health, "health")
    print("The enemy has", enemyHealth, "health")
    print("")
    global attack
    attack = input("Do you want to attack? ")
    print("")


def tryAgain():  # Try again
    global health
    health = random.randint(5, 10)
    start()


def notTryAgain():  # Not trying again
    if EnemiesKilled > 1:
        print("You killed", EnemiesKilled, "enemies")
    else:
        print("You only killed", EnemiesKilled, "enemies")
    global continiue
    continiue = "no"


health = random.randint(5, 10)

continiue = "yes"
while continiue == "yes":
    encounter_type = random.choice(encounters)
    if encounter_type == "monster":  # If you encounter a monster
        enemyHealth = random.randint(1, 10)
        start()
        if attack == "yes":  # If you want to attack
            if health > enemyHealth:  # If you have more health than the enemy
                print("You killed the enemy")
                EnemiesKilled += 1
                health -= enemyHealth
            elif health == enemyHealth:  # If you have the same amount of health as the enemy
                sameHealth = random.randint(1, 2)
                if sameHealth == 1:  # If you beat the enemy
                    print("You killed the enemy")
                    EnemiesKilled += 1
                    health -= enemyHealth
                else:  # If you don't beat the enemy
                    print("You are dead")
                    print("")
                    retry = input("Do you want to try again? ")
                    if retry == "yes":  # If you want to try again
                        tryAgain()
                    else:  # If you don't want to try again
                        notTryAgain()
            else:  # If you have less health than the enemy
                print("You are dead")
                print("")
                retry = input("Do you want to try again? ")
                if retry == "yes":  # If you want to try again
                    tryAgain()
                else:  # If you don't want to try again
                    notTryAgain()
        elif attack == "no":  # If you don't want to attack
            print("You try to run away")
            runAway = random.randint(1, 2)
            if runAway == 1:  # If you get away
                print("You got away")
                print("")
            else:  # If you don't get away
                print("You could not get away")
                print("")
                retry = input("Do you want to try again? ")
                if retry == "ja":  # If you want to try again
                    tryAgain()
                else:  # If you don't want to try again
                    notTryAgain()
        else:  # If you write something else than "ja/nei"
            print("You are dead")
            continiue = "no"
    elif encounter_type == "chest":  # If you find a chest
        print("You found a chest!")
        health += 3
        print("You found 3 lives and now have", health, "health")
        print("")
        continiue = input("Do you want to continiue? ")
