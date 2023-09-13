# Define a room
description = "big room with chandeler hanging from the ceiling, and painting along all the walls."
doors = ["north", "south", "east", "west"]


# Welcome message
print("Hello, and welcome to Jimmy's Berlin")
print("************************************")
print()

# Main loop/Game loop
run = True
while run:
    
    # Print room
    print("You are standing in a " + description)
    print("There are doors to the: ")
    
    # Format and print out all the directions that are available in the room
    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    print()
    
    # Print menu
    print("What would you like to do?")
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    print("5. Look around")
    print("0. Quit")
    
    # Ask user for input
    choice = input("Please enter your choice: ")
    
    # Clear user input
    if not choice.isnumeric():
        print()
        print("Sorry! Did not understand what your meant.")
        print("Press any key to return to the main menu and enter a number...")
        input()
        continue
    
    # Do something based on user input
    # If user enters unknown variable, tell them
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print()
        print("You go North")
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
        print("You look around the current room, but don't find anything interesting")
    else:
        print()
        print("Sorry, you can't do that.")
        
    print("Press any key to continue...")
    input()