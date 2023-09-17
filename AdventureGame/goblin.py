import random

# TODO Figure out how to implement the idea in the main file
# TODO Read up on classes and functions in Python
# TODO Player can find items to enhance abilities?

# Goblin enemy for player to fight with stats
def goblin():
    name = "Goblin"
    health = 10
    defence = 2
    attack = random.randint(0, 5)

# Player character
def player():
    name = "You"
    health = 15
    defence = 0
    attack = random.randint(1, 7)

