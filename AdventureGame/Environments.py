class Room:

    # Class constructor
    def __init__(self, name):
        self.name = name
        self.items = []
        self.doors = []
        self.description = ""
        self.inspect = ""

    # Used to add a description to a room
    def setDescription(self, description):
        self.description = description

    # Used to add items
    def addItem(self, item):
        self.items.append(item)

    # Used to add available doors to a room
    def addDoor(self, door):
        self.doors.append(door)

    # Used to check which door have been made available in a room
    def checkDoor(self, direction):
        return direction in self.doors

    # Used to set descriptions of items found if current room is inspected
    def setInspect(self, inspect):
        self.inspect = inspect

    # Used to format and deliver the description of the room
    def toString(self):
        # Description of the current room
        response = ""
        response = self.description + "\n"
        response = response

        # Print available doors in current room
        response = response + "There are doors to your:\n"
        # Formats the printed doors
        directions = ""
        for direction in self.doors:
            directions = directions + " \n" + direction
        directions = directions[2:]
        response = response + directions + "\n"

        return response

    # Prints out detailed information about room
    def lookCloser(self):
        print(self.inspect)
