import random

# Function determaining if the player finds item when looking around
def item():
    newRandom = random.randint(0, 1)
    if newRandom == 0:
        return print("You look around the current room, but don't find anything interesting.")
    else:
        return print("You found something real cool.")


# Define an environment
# House
entranceHouse = "in the hallway to a big mansion. It's dingy and smells of mold."
stairsUpHouse = "at the foot of stairs going upward. There are pictures along the wall and only darkness at the top"
stairsDownHouse = "at the precipice of stairs descending downward. The bottom of them are shrouded in darkness."
livingRoomHouse = "in a quiet living room. The faint flicker of dying embers try their best at illuminating the space, to no avail."
libraryRoomHouse = "in an old library. The walls around covered in bookshelves and the bookshelves contain heavy tomes of leather or smelly parchment."
kitchenRoomHouse = "in an awful kitchen. You're assaulted by a smell not of this world. The sink is full of dirty dishes and old food. Is there something cooking in the oven?"
basementRoomHouse = "at the foot of the stairs in a basement with no light. You can't see anything."

# List of rooms and directions
rooms = [stairsUpHouse, stairsDownHouse, livingRoomHouse, libraryRoomHouse, kitchenRoomHouse, basementRoomHouse]
doors = ["North", "South", "East", "West"]


# Welcome message and opening
print("Hello, and welcome to AdventureGame")
print("***********************************")
print()

print("You're standing " + entranceHouse)
input("Press any key to continue...")
print("----------------------------")
print()

# Main loop
run = True
while run:

    # Print environments and picks a random predefined room for the player to spawn in
    print()
    print("You're standing", random.choice([stairsUpHouse, stairsDownHouse, livingRoomHouse, libraryRoomHouse, kitchenRoomHouse, basementRoomHouse]))
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
    