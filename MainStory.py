import time


print("Welcome to the Andersons' house... a short series game by the best newbs in the world!")
print("You stand across the street from a burning building, the building stands only with hope and prayer, never to be salvaged again...")

choice = input("walk forward and investigate (Q) or explore the nearby forest for any survivors (F)? ").upper()

if choice == "Q":
    print("stepping among ash and burning coals of wood you find a stuffed bear")
    choice2 = input("pick it up and investigate further (W) or leave and investigate further (C)? ").upper()
    if choice2 == "W":
        print("you pick up the stuffed bear and head towards the house...")
        print("The stuffed bear was partially charred from one side with parts of the exposed, burnt stuffing crubling to dust as soon as you touch it.")
        print("The sight of the bear's dark, beady eyes fills your heart with sorrow")
        print("You try to imagine the previous owner of this stuffed toy")
        print("Visions of a helpless child blissfully oblivious to what was happening fill your head")
    elif choice2 == "C":
        print("you leave the bear to pick up later, but it fills you with sorrow, there may be a child.")
        print("As you leave the site, you hear something akin to a person off in the distance")
        print("You decide to go investigate to see if it's a survivor of the fire")
    else:
        print("Your indecision led you astray. Game over.")
if choice == "F":
    print("You enter the forest and hear the screach of a crying child.")
    choice3 = input("investigate further (X) or go back to investigating the house (G)? ").upper()
    if choice3 == "X":
        print("the shreeking gets louder and louder as you peer slowly behind a bush to find your untimely demise")
#the ones and zeros are for a tech related plot twist later ;)
        for _ in range(20): print("011010[ ~ D O N T ~ C O M E ~ H E R E ~ A G A I N ~ ]110101")
    elif choice3 == "G":
        print("you head back to the house and while youre walking through soot and ash you stumble apon a stuffed bear")

else:
    print("Invalid choice. Please restart the game.")
#feel free to put while loops instead of this else statement
