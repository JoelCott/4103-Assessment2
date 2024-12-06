import time
import random
from enum import Enum

gridMap = []
players = []
treasure = []
treasureCount = 0 
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
    
    def movePlayer(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < len(gridMap) - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < len(gridMap) - 1:
            self.x += 1
        else:
            print("Invalid move")
        updateGrid()

def createGrid(mapSize):
    global gridMap
    gridMap = [[" "] * mapSize for _ in range(mapSize)]
    displayGrid()
        
def displayGrid():
    for row in gridMap:
        print("|".join(row))

def playerCreation(amount_of_players, mapSize):
    for i in range(amount_of_players):
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        while gridMap[y][x] != " ":
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        
        players.append(Player(i, playerHealth, x, y))
        gridMap[y][x] = str(i + 1)
        print(f"Player {i + 1} created at ({x}, {y})")
        
def treasureCreation(amount_of_treasure, mapSize):
    for i in range(amount_of_treasure):
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        while gridMap[y][x] != " ":
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        
        players.append(Player(i, playerHealth, x, y))
        gridMap[y][x] = str(i + 1)
        print(f"Player {i + 1} created at ({x}, {y})")


def updateGrid():
    global gridMap
    createGrid(len(gridMap))
    for player in players:
        gridMap[player.getY()][player.getX()] = str(player.id + 1)
    displayGrid()

# Main Code
mapSize = int(input("Please enter a number for how big the grid shall be: "))
createGrid(mapSize)

amount_of_players = int(input("Enter the amount of players you would like: "))
playerCreation(amount_of_players, mapSize)

amount_of_treasure = int(input("Enter "))

while playerHealth > 0:
    for player in players:
        print(f"Player {player.id + 1}'s Turn")
        time.sleep(2)
        displayGrid()
        direction = input("Please enter the direction you would like to go: 'Up', 'Down', 'Left' & 'Right' ").lower()
        player.movePlayer(direction)