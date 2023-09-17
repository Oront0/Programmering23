import random
import goblin
import environments

# TODO Initial idea is to plan out a house that the player may move around in.
# TODO Each door (upstairs?) will lead to a different kind of game that the player has to beat.
# TODO Perhaps the player acquires a key for each mini game they beat which they need to escape the house?
# TODO Would prefer each game to be contained within its own file.

goblin.goblin()


# Function determining if the player finds item when looking around
def item():
    newRandom = random.randint(0, 1)
    if newRandom == 0:
        return print("You look around the current room, but don't find anything interesting.")
    else:
        return print("You found something real cool.")


# List of rooms and directions
doors = ["North", "South", "East", "West"]


# Welcome message and opening
print("Hello, and welcome to AdventureGame")
print("***********************************")
print()

print("You're standing " + environments.entranceHouse)
input("Press any key to continue...")
print("----------------------------")
print()

# Main loop
run = True
while run:

    # Print environments.py and picks a random predefined room for the player to spawn in
    print()
    print("You're standing", random.choice(environments.rooms))
    print()
    input("Press any key to continue...")
    print("----------------------------")
    print()
    print("Where would you like to move?")

    # Format and print out all the available directions
    directions = ""
    for direction in doors:
        direction = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    print()

    # Print menu
    print("What would you like to do?")
    print("1. Go North")
    print("2. Go South.")
    print("3. Go East.")
    print("4. Go West.")
    print("5. Look around.")
    print("0. Quit")

    # Ask user for input
    choice = input("Please enter your choice: ")
    print("----------------------------")

    # Clear user input
    if not choice.isnumeric():
        print()
        print("Sorry, that's not possible.")
        print("Press any key to return to the main menu and enter a number.")
        input()
        continue

    # Do something based on user input
    # If user enters unknown variable, tell them
    choice = int(choice)
    if choice == 1:
        print()
        print("You go North.")
    elif choice == 2:
        print()
        print("You go South")
    elif choice == 3:
        print()
        print("You go East")
    elif choice == 4:
        print()
        print("You go West")
    elif choice == 5:
        print()
        item()
    else:
        print()
        print("Sorry, you can't do that.")

    print("Press any key to continue...")
    print("----------------------------")
    input()
    