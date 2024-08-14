print("Welcome to Treasure Island.")
print("Your mission is to find the trasure.")
current_location = input("You're at a cross road. Where dou you want to go? Left or Right? ")

if current_location == "Left":
    swim_or_wait = input("You found a lake. Do you want to swim across it or wait a few moments? Swim or Wait: ")
    if swim_or_wait == "Wait":
        select_doors = input("3 doors magically appear in front of you, which one do  you choose? Red, Blue or Yellow? ")
        if select_doors == "Red":
            print("You were burned by fire. Game over.")
            exit()
        elif select_doors == "Blue":
            print("You were eaten by beasts. Game over.")
            exit()
        elif select_doors == "Yellow":
            print("You found the Treasure, congratulations! You Won!")
            exit()
        else:
            print("Game over.")
    elif swim_or_wait == "Swim":
        input("You were attacked by a shark. Game over.") 
        exit()
    else:
        input("You were attacked by a shark. Game over.") 
        exit()       
    exit()
elif current_location == "Right":
    print("You fell into a hole. Game over.")
    exit()
else:
    print("You fell into a hole. Game over.")
    exit()
