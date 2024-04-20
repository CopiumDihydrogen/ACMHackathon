print("Welcome to the Andersons' house...")

print("You stand across the street from a burning building, the building stands only with hope and prayer, never to be slavaged again...")



choice = input("walk forward and investigate (Q) or explore the nearby forest for any survivors (F)? ").upper()



if choice == "Q":

print("stepping among ash and burning coals of wood you find a stuffed bear")

choice2 = input("pick it up and investigate further (W) or leave and investigate further (C)? ").upper()



if choice2 == "W":

print("you pick up the stuffed bear and head towards the house...")



elif choice2 == "C":

print("you leave the bear to pick up later, but it fills you with sorrow, there may be a child.")



else:

print("Your indecision led you astray. Game over.")



elif choice == "F":

print("You enter the forest and hear the screach of a crying child.")

choice3 = input("investigate further (X) or go back to investigating the house (G)? ").upper()


if choice3 == "X":
print("the shreeking gets louder and louder as you peer slowly behind a bush to find your untimely demise")

print("Game Over...")


if choice3 == "G":
print("i havent coded this yet so be patient")

print("Game Over...")

else:

print("Invalid choice. Please restart the game.")
