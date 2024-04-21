import time


print("Welcome to the Andersons' house...")
print("A short choose-your-own-adventure style story by Anthony, Matthew and Eris")
#Prompt 1
print("You stand across the street from a burning building, the building stands only with hope and prayer, never to be slavaged again...")
choice = input("walk forward and investigate (Q) or explore the nearby forest for any survivors (F)? ").upper()
#Branch 1
if choice == "Q":#Choice 1
    print("stepping among ash and burning coals of wood you find a stuffed bear")
    choice2 = input("pick it up and investigate further (W) or leave and investigate further (C)? ").upper()
    #Sub-branch 1
    if choice2 == "W":#Sub-choice 1
        print("you pick up the stuffed bear and head towards the house...")
    elif choice2 == "C":#Sub-choice 2
        print("you leave the bear to pick up later, but it fills you with sorrow, there may be a child.")
    else:#Sub-choice 3
        print("Your indecision led you astray. Game over.")
        time.sleep(8)
        exit()
elif choice == "F":#Choice 2
    print("You enter the forest and hear the screach of a crying child.")
    choice3 = input("investigate further (X) or go back to investigating the house (G)? ").upper()
    #Sub-branch 1
    if choice3 == "X":#Sub-choice 1
        print("the shreeking gets louder and louder as you peer slowly behind a bush to find your untimely demise")
        print("Game Over...")
        time.sleep(8)
        exit()
    if choice3 == "G":#Sub-choice 2
        print("Your search yielded no results.")
        print("Game Over...")
        time.sleep(8)
        exit()
else:
    print("Invalid choice. Please restart the game.")
    time.sleep(8)
    exit()