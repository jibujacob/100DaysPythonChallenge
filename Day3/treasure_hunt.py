#Treasure hunt challenge
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input('You are at a cross road. Where do you want ot go? Type "left" or "right"\n')
if (direction.lower()=="left"):
    direction=input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swin across\n')
    if (direction.lower() =="swim"):
        direction=input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do your choose?\n')
        if (direction.lower() == "yellow"):
            print("You Win!")
        elif (direction.lower() == "red"):
            print("Burned by fire. Game Over")
        elif (direction.lower() == "blue"):
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fell into a hole. Game Over")
