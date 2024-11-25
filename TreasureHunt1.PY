import time
import random
from enum import Enum

gridMap = []
players = []
playerHealth = 5

class Player:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = health
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def movePlayer(direction, playerID):
        if direction == "up":
            #for each direction 
            #if can go up, if y != 0  
            #remove old position from grid - set x and y = ' ' 
            #then -1 update player self y
            #update grid with new position displaygrid()
            print("up")
        elif direction == "down":
            print("down")
        elif direction == "left":
            print("left")
        elif direction == "right":
            print("right")
        #update grid

# --// Procedures, Functions & Parameters \\--
def createGrid(mapSize):
    global gridMap  # Ensure gridMap is recognized as global
    gridMap = []  # Reset gridMap for new grid
    for i in range(mapSize):  # Creating the rows in the list
        row = [" "] * mapSize  # Filling the row with spaces
        gridMap.append(row)  # Appending the row to the gridMap
    displayGrid()
        
def displayGrid():
    for row in gridMap:  # Printing the grid
        print("|".join(row))  # Print the grid in a formatted way

def playerCreation(amount_of_players, mapSize):
    for i in range(amount_of_players):
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        # Ensure the position is empty
        while gridMap[x][y] != " ":
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        
        count = i + 1
        players.append(Player(i, playerHealth, x, y, ))
        gridMap[x][y] = str(count) # Place player on the grid
        print(f"Player {i} created at ({x}, {y})")  # Print player position


# --// Main Code \\--
mapSize = int(input("Please enter a number for how big the grid shall be: "))
createGrid(mapSize)

amount_of_players = int(input("Enter the amount of players you would like: "))
playerCreation(amount_of_players, mapSize)

displayGrid()

#turn order(rounds) while loop until win or death etc
#for player in players etc
#user input the direction/movement player[index].moveplayer(inpue("sadhkasjhdkajh"))
