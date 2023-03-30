# --- IMPORTS --- # 

import random

# --- VARIABLES --- #

enemiesKilled = 0
health = 10
enemyHealth = 0
encounters = ['monster', 'monster', 'monster',
         'chest']  # 1/4 chance to find a chest

# --- FUNCTIONS --- #

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
    if enemiesKilled > 1:
        print("You killed", enemiesKilled, "enemies")
    else:
        print("You only killed", enemiesKilled, "enemies")
    global continiue
    continiue = "no"
    
def killEnemy(): # If you kill the enemy
    print("You killed the enemy")
    global enemiesKilled
    enemiesKilled += 1
    global health
    health -= enemyHealth

def death():
    print("You are dead")
    print("")
    global retry
    retry = input("Do you want to try again? ")
    if retry == "yes":  # If you want to try again
        tryAgain()
    else:  # If you don't want to try again
        notTryAgain()

def deathRun():
    print("You could not get away")
    print("")
    global retry
    retry = input("Do you want to try again? ")
    if retry == "yes":  # If you want to try again
        tryAgain()
    else:  # If you don't want to try again
        notTryAgain()

def findChest():
    print("You found a chest!")
    global health
    health += random.randint(3, 5)
    print("You found 3 lives and now have", health, "health")
    print("")
    global continiue
    continiue = input("Do you want to continiue? ")

# ------- CODE ------- #

health = random.randint(5, 10)

continiue = "yes"
while continiue == "yes":
    encounter_type = random.choice(encounters)
    if encounter_type == "monster":  # If you encounter a monster
        enemyHealth = random.randint(1, 10)
        start()
        if attack == "yes":  # If you want to attack
            if health > enemyHealth:  # If you have more health than the enemy
                killEnemy()
            elif health == enemyHealth:  # If you have the same amount of health as the enemy
                sameHealth = random.randint(1, 2)
                if sameHealth == 1:  # If you beat the enemy
                    killEnemy()
                else:  # If you don't beat the enemy
                    death()
            else:  # If you have less health than the enemy
                death()
        elif attack == "no":  # If you don't want to attack
            print("You try to run away")
            runAway = random.randint(1, 2)
            if runAway == 1:  # If you get away
                print("You got away")
                print("")
            else:  # If you don't get away
                deathRun()
        else:  # If you write something else than "yes/no"
            death()
    elif encounter_type == "chest":  # If you find a chest
        findChest()
