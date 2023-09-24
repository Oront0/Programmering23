import random
from Environments import Room
from Items import Items

# TODO Initial idea is to plan out a house that the player may move around in.
# TODO Each door (downstairs) will lead to a different kind of game that the player has to beat.
# TODO Perhaps the player acquires a key for each minigame they beat which they need to escape the house?
# TODO Would prefer each game to be contained within its own file.


# Welcome message and opening
def welcomeMessage():
    print("Hello, and welcome to AdventureGame")
    print("***********************************")
    print()

    print("You arrive at the haunted old mansion at the top of the lonely hill.")
    print("After hearing stories of the treasures hidden away here you decided to find them.")
    print("With some minor hesitations you open the door and step inside.")
    print("The door slams shut behind you and you see X amount of symbols light up as you hear the door locking itself") # TODO change X to number of minigames once determined
    print("In turn the light of the symbols wanes and disappears. The door is impossible to open. Perhaps you should explore the house for another way out.")
    print("You slowly turn around and inspect the room you're in.")
    print()
    input("Press Enter to continue...")
    print("----------------------------")
    print()


# Printing main menu
def displayMenu():
    print("What would you like to do?")
    print("1. Go North")
    print("2. Go South.")
    print("3. Go East.")
    print("4. Go West.")
    print("5. Look around.")
    print("6. Check inventory.")
    print("0. Quit")


# Handle user input
def fetchInput():
    ans = input("Please enter your choice: ")
    if ans.isdigit():
        if 0 <= int(ans) <= 6:  # This rewrite was suggested by PyCharm
            return int(ans)
    return -1


# Function allowing player to search a room and choose to pick up and item, if they find one.
def itemSearch():
    if currentRoom.items:
        print(currentRoom.inspect + "\n")
        ans = input("Would you like to pick it up? y/n\n")
        if ans.lower() == "y":
            found = currentRoom.items[0]
            inventory.append(found)
            return print("You pick up: " + found.getName())
        elif ans.lower() == "n":
            print("You leave it behind.")
        else:
            print("Bad input, please try again.")

    else:
        return print("You poke around the room but find nothing of interest.")


# Gives the player a list of the items they've found so far
# TODO Implement item inspection
def checkInventory():
    if not inventory:
        print("Your inventory is empty!")
    else:
        print("You have:", [item.getName() for item in inventory])  # I am still considering if I like the items displaying the way they are or if I want to clean up the output


# Define player
inventory = []

######################
# Define Environment #

#########
# Items # # TODO Add more items once all the game rooms have been decided
coin = Items("Coin", "A shiny coin.")
paper = Items("Scrap of paper", "There are drawings of hand gestures on the scrap of paper with arrows going from one to the other in a circle.")
earrings = Items("Earrings", "Two earrings. One is adorned with an X, the other an O.")
noose = Items("Noose", "An old piece of rope tied into a noose... (yikes)")


############
# Entrance #
entrance = Room("Entrance")
entrance.setDescription("You're in the entrance hallway of the big mansion. It's dingy and smells of mold.")
entrance.addDoor("North")
entrance.addDoor("South")
entrance.addDoor("East")
entrance.addItem(coin)
entrance.setInspect("There's a coin on the floor...")

###############
# Living room #
livingRoom = Room("Living room")
livingRoom.setDescription("You're standing in a quiet living room. The faint flicker of dying embers try their best at illuminating the space, to no avail.")
livingRoom.addDoor("South - to entrance.")
livingRoom.addDoor("South - to kitchen.")
livingRoom.addItem(earrings)
livingRoom.setInspect("You see some odd-looking earrings on a small table in the corner of the room.")


###########
# Kitchen #
kitchen = Room("Kitchen")
kitchen.setDescription("You're standing in an awful kitchen. You're assaulted by a smell not of this world. The sink is full of dirty dishes and old food.")
kitchen.addDoor("North - to living room.")
kitchen.addDoor("South - to library.")
kitchen.addDoor("West - to hallway with stairs.")
kitchen.addItem(noose)
kitchen.setInspect("On the counter there's a noose... ominous.")

###########
# Library #
library = Room("Library")
library.setDescription("You're standing in an old library. The walls around covered in bookshelves and the bookshelves contain heavy tomes of leather or smelly parchment.")
library.addDoor("North - to entrance.")
library.addDoor("North - to kitchen.")
library.addItem(paper)
library.setInspect("A piece of paper sticks out from between two books.")

###########
# Hallway #
hallway = Room("Hallway")
hallway.setDescription("You're standing in a small hallway with stairs leading to the second floor and a door leading to a basement. The stairs going up are rotted and ruined. Unless.")
hallway.addDoor("North - to basement.")
hallway.addDoor("West - to entrance.")
hallway.addDoor("East - to kitchen.")

############
# Basement #
basement = Room("Basement")
basement.setDescription("You're standing in the basement. It's wet and cold. There is nothing of interest down here except a trap door in the middle of the room.")
basement.addDoor("South - to hallway.")

#################
# Game room hub #
hub = Room("Mysterious space...")
hub.setDescription("You're standing in an oddly large room. You feel as if the ceiling is too high with how short those stairs were. The room is empty except for four doors.")
hub.addDoor("South - to safety.")


################
# Main Program #
# TODO Attempt to implement a matrix to handle movement through rooms
# TODO I would like to keep the descriptive text of each door (ex: "to kitchen") but haven't figured out how yet


# Matrix to handle rooms
roomNumber = [
    [livingRoom],
    [entrance, hallway, kitchen],  # the hub room isn't implemented yet, not sure where to put it.
    [library]]

# Variables to handle player position
currentRoom = entrance
currentRow = 2
currentCol = 1

# Prints welcome message
welcomeMessage()

# Main loop
run = True
while run:

    # Display the room the player is in
    print(currentRoom.toString())

    # Display main menu
    displayMenu()

    # Ask user for input
    choice = fetchInput()
    print("----------------------------")

    # Clear user input
    if choice == -1:
        print()
        print("Sorry, that's not possible.")
        print("Press Enter to return to the main menu and enter a number.")
        input()
        continue

    # Do something based on user input
    # If user enters unknown variable, tell them
    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        if currentRow > 0 and currentRoom.checkDoor("North"): # TODO The way I've made the matrix something like this should work but you end up in the wrong room
            currentRow -= 1
            currentRoom = roomNumber[currentRow][currentCol]
            print(currentRow, currentCol) # Only used for debugging while I figure out matrices
            print()
            print("You go North")
        else:
            print(currentRow, currentCol)
            print("You can't move that way.")
    elif choice == 2:
        if currentRow <= 3 and currentRoom.checkDoor("South"):
            currentRow += 1
            currentRoom = roomNumber[currentRow][currentCol]
            print()
            print("You go South")
        else:
            print(currentRow, currentCol)
            print("You can't move that way.")
    elif choice == 3:
        if currentCol <= 3 and currentRoom.checkDoor("East"):
            currentCol += 1
            currentRoom = roomNumber[currentRow][currentCol]
            print()
            print("You go East")
        else:
            print(currentRow, currentCol)
            print("You can't move that way.")
    elif choice == 4:
        if currentCol < 0 and currentRoom.checkDoor("West"):
            currentCol -= 1
            currentRoom = roomNumber[currentRow][currentCol]
            print()
            print("You go West")
        else:
            print(currentRow, currentCol)
            print("You can't move that way.")
    elif choice == 5:
        print()
        itemSearch()
    elif choice == 6:
        print()
        checkInventory()
    else:
        print()
        print("Sorry, you can't do that.")

    print("Press Enter to continue...")
    print("----------------------------")
    input()
    