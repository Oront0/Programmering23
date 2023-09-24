# Items class
class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # Return name of item
    def getName(self):
        return self.name

    # Return description of item
    def getDescription(self):
        return self.description

    # Return formatted string
    def ToString(self):
        return self.name + "\n" + self.description