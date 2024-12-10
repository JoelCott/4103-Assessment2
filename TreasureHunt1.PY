import time
import random

gridMap = []
players = []
treasure = []
traps = []
powerup = []
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
    
    def getHealth(self):
        return self.health
    
    def movePlayer(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < len(gridMap) - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < len(gridMap[0]) - 1:
            self.x += 1
        else:
            print("Invalid move")
        updateGrid()
        
class Treasure:
    def __init__(self, id, treasure_x, treasure_y):
        self.id = id
        self.treasure_x = treasure_x
        self.treasure_y = treasure_y
    
    def getTX(self):
        return self.treasure_x
    
    def getTY(self):
        return self.treasure_y

class Traps:
    def __init__(self, id, traps_x, traps_y):
        self.id = id
        self.traps_x = traps_x
        self.traps_y = traps_y
    
    def getTrX(self):
        return self.traps_x
    
    def getTrY(self):
        return self.traps_y

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
        
        treasure.append(Treasure(i, x, y))
        gridMap[y][x] = "T"
        print(f"Treasure {i + 1} created at ({x}, {y})")
        
def trapCreation(amount_of_traps, mapSize):
    for i in range(amount_of_traps):
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        while gridMap[y][x] != " ":
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize)
        
        traps.append(Traps(i, x, y))
        gridMap[y][x] = "X"
        print(f"Traps {i + 1} created at ({x}, {y})")

def checkTreasures(x, y, player):
    global treasure
    for t in treasure:
        if x == t.getTX() and y == t.getTY():
            print("You have found the treasure!")
            userChoice = input("Please choose from 'health', 'powerup', 'clues': ").lower()
            if userChoice == "health":
                print("You have gained 1 more life")
                player.health += 1
                print("Your new health score is: ", player.health)
            elif userChoice == "powerup":
                print("You have gained a powerup. You have immunity to one trap.")
                powerup.append(1)
                print(f"Your current immunities: {powerup}")
            elif userChoice == "clues":
                userChoice2 = input("You now have a clue. Please choose between Binary Search, Depth first search or Breadth first search (BS, DFS, BFS)").lower()
                if userChoice2 == "bs":
                    print("Loading Binary Search")
                elif userChoice2 == "dfs":
                    print("Loading Depth-First Search")
                elif userChoice2 == "bfs":
                    print("Loading Breadth-First Search")
                else:
                    print("ERROR - Please enter the correct input.")
                
            treasure.remove(t)
            break
    if len(treasure) != 0:
        print(f"You have {len(treasure)} treasures left!")
    else:
        print("You have no more treasures left!") 
    print("Continuing game: ")

def updateGrid():
    global gridMap
    createGrid(len(gridMap))
    for player in players:
        gridMap[player.getY()][player.getX()] = str(player.id + 1)
    for t in treasure:
        gridMap[t.getTY()][t.getTX()] = "T"
    for trap in traps:
        gridMap[trap.getTrY()][trap.getTrX()] = "X"
    displayGrid()

# Main Code
mapSize = int(input("Please enter a number for how big the grid shall be (Entering 5 will create a 5x5 grid): "))
createGrid(mapSize)

amount_of_players = int(input("Enter the amount of players you would like: "))
playerCreation(amount_of_players, mapSize)

amount_of_treasure = int(input("Enter the amount of treasure you would like in your game: "))
treasureCreation(amount_of_treasure, mapSize)

amount_of_traps = int(input("Please enter a number of how many traps you would like in your game: "))
trapCreation(amount_of_traps, mapSize)

while playerHealth > 0:
    for player in players:
        print(f"Player {player.id + 1}'s Turn") 
        updateGrid()
        time.sleep(2)
        print("\n")
        displayGrid()
        direction = input("Please enter the direction you would like to go: 'Up', 'Down', 'Left' & 'Right' ").lower()
        player.movePlayer(direction)
        checkTreasures(player.getX(), player.getY(), player)