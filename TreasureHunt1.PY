# --// Libraries, Variables & Services \\--

import time # Importing the time library so I can pause the program at certain points to give the user enough time to read what is being outputted to them
import random # Importing the random library so I can have dynamic variables and find the range or have a random position entered for the objects to be inputted into the grid in random positions
import math # Importing the math library so I can find the difference between the players position with the treasure whilst doing the binary search

gridMap = [] # List used to store the size of the map 
players = [] # List used to store the amount of players in the game
treasure = [] # List used to store the amount of treasure in the game
traps = [] # List used to store the amount of traps in the game
powerup = [] # List used to store the amount of powerups a player has
winLocation = [] # List used to store the win location once all treasure has been collected
playerHealth = 3 # Variable used to store how much health each player starts with. This is static 


# --// Object Oriented Programming - Classes & Methods, Attributes & Constructor Methods \\--
class Player: # Class defining the object player
    def __init__(self, id, health, x, y): # Initialising the player class and setting the attributes
        self.id = id # Setting the ID
        self.health = health # Setting the player health
        self.x = x # Setting the player x coordinate
        self.y = y # Setting the player y coordinate

    def getX(self): # Function getting the x coordinate
        return self.x # Returning the player coordinate 

    def getY(self): # Function getting the y coordinate
        return self.y # Returning the player coordinate

    def getHealth(self): # Function getting the player health
        return self.health # Returning the players health

    def movePlayer(self, direction): # Function setting the players new coordinate when moving
        if direction == "up" and self.y > 0: # Checking if the player wanted to move up
            self.y -= 1 # Moving the player up by 1
        elif direction == "down" and self.y < len(gridMap) - 1: # Checking if the player wanted to move down
            self.y += 1 # Moving the player down by 1
        elif direction == "left" and self.x > 0: # Checking if the player wanted to move left
            self.x -= 1 # Moving the player left by 1
        elif direction == "right" and self.x < len(gridMap[0]) - 1: # Checking if the player wanted to move right
            self.x += 1 # Moving the player right by 1
        else: # Checking that the data is a valid entry if not
            print("Invalid move") # Telling the user they did not enter the right direction: Will move to the next player as this is a race between players
        updateGrid() # Updating the grid with the players new coordinates

class Treasure: # Class defining the object Treasure
    def __init__(self, id, treasure_x, treasure_y): # Initialisng the treasure class and settings its new attributes
        self.id = id # Setting the treasures id (only neded for locating in given statements for specific treasures)
        self.treasure_x = treasure_x # Setting the treasues x position
        self.treasure_y = treasure_y # Setting the treasures y position

    def getTX(self): # Function getting the x position
        return self.treasure_x # Returning the x position

    def getTY(self): # Function getting the y position
        return self.treasure_y # Returning the y position

class Traps: # Class defining the trap object
    def __init__(self, id, traps_x, traps_y): # Initialisng the class with its attributes
        self.id = id # Setting the trap id (only needed for locating in given statements for specific traps)
        self.traps_x = traps_x # Setting the x position of the trap
        self.traps_y = traps_y # Setting the y position of the trap

    def getTrX(self): # Function getting the x position of the trap
        return self.traps_x # Returning the x position

    def getTrY(self): # Function getting the y position of the trap
        return self.traps_y # Returning the y position 

class Win: # Class defnining the object Win and settings its attributes
    def __init__(self, id, win_x, win_y): # Initialising the win class
        self.id = id # Setting the ID of the win (Only needed for lcoating in given statements forthe specific win location)
        self.win_x = win_x # Setting the x position of the win location
        self.win_y = win_y # Setting the y position of the win location

    def getWX(self): # Getting the x position of the win location
        return self.win_x # Returning the x position 

    def getWY(self): # Getting the y position of the win location
        return self.win_y # Returning the y position
    
# --// Procedures, Paramaters & Functions \\--

def distancebetweenPlayerandTreasure(p1, p2): # Function to support the binary search with finding the nearest treasure
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) # Returning the algorithm to find the difference between each treasure and the players location to get the closest treasure

def binarySearchT(player): # Function to start the binary search
    treasures = [[t.getTX(), t.getTY()] for t in treasure] # Getting the location of each treasure available on the map
    treasures.sort(key=lambda t: distancebetweenPlayerandTreasure([player.getX(), player.getY()], t)) # Sorting the treasure in order of the one closest to the player
    return treasures[0] if treasures else None # Returning the treasure stored in the position 0 as thats the one closest to the player, if there are none close by it will return None

def createGrid(mapSize): # Function creating the grid based on the size the user inputs
    global gridMap # Making the variable global so that the list can be accessed everywhere as it needs to be
    gridMap = [[" "] * mapSize for _ in range(mapSize)] # Setting the grids format Number x Number depending on the user input
    displayGrid() # Calling the display function to print the map

def displayGrid(): # Function printing the map to the user
    for row in gridMap: # Checking how many rows are in the grid
        print("|".join(row)) # Printing the grid format with | seperating the columns per row

def playerCreation(amount_of_players, mapSize): # Function creating the players based on how many the user inputted
    for i in range(amount_of_players): # Checking how many players have been inputted
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Randomly generating an x and y coordinate for each player
        while gridMap[y][x] != " ": # Chcking the empty slots in the grid to see where the players can spawn in
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Setting the coordinates based on the empty slots available
        players.append(Player(i, playerHealth, x, y)) # Adding the new player to the player list through the class to have its own attributes
        gridMap[y][x] = str(i + 1) # Setting the player by number e.g. player 1 and player 2 if 2 players have been selected
        print(f"Player {i + 1} created at ({x}, {y})") # Telling the user that the player has been created and telling them the position they will start at

def treasureCreation(amount_of_treasure, mapSize): # Function creating the treasure based on how many the user has inputted
    for i in range(amount_of_treasure): # Checking how much treasure the user wants on the map
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Randomly generating the x and y position for each treasure
        while gridMap[y][x] != " ": # Checking the empty slots in the game and if the slot is not empty it will generate a new coordinate until its found an empty place for the treasure to be craeted at
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Generating a new position for the treasure to be created at
        treasure.append(Treasure(i, x, y)) # Storing the treasure in a list through the class so that each treasure has its own unique ID, x and y position
        gridMap[y][x] = "T" # Setting all treasure to be displayed as T on the map
        print(f"Treasure {i + 1} created at ({x}, {y})") # Telling the user that the number of treasures they have enetered has been created and place in the random position

def winninglocationCreation(mapSize): # Function creating the winning location
    if len(winLocation) != 1: # Checking that the win location has not already been created. Maximum of 1 only.
        amount_of_winlocations = 1 # Setting the win location value to 1 so that it can be checked within a loop
        for i in range(amount_of_winlocations): # Checking the one win location to see if its active and stored in the list
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Randomly placing the win location in the values available.
            while gridMap[y][x] != " ": # Checking if the given position above is in a free space in the column and row
                x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Giving the win a new location until its a suitable place
            winLocation.append(Win(i, x, y)) # Putting the win location in the list through the class so it has its own x and y location
            gridMap[y][x] = "W" # Putting a W in the position given above to show the user where the win location is stored.
            print(f"Win Location {i + 1} created at ({x}, {y})") # Telling the user that the win location has been created and placed in the set position.
        time.sleep(2) # Pausing the game so the user can understand whats happening with the win lcoation
        updateGrid() # Updating the grid to display the new grid
    else: # If there is already a win location do:
        print("You already have a win location, get there now!") # Telling the user they already have a win lcoation and to continue with their next move

def trapCreation(amount_of_traps, mapSize): # Function creating the traps
    for i in range(amount_of_traps): # Checking how many traps the user has wanted in their game
        x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # Giving the traps a random location to be placed at
        while gridMap[y][x] != " ": # Checking if the current position is empty and suitable to place the trap
            x, y = random.randrange(0, mapSize), random.randrange(0, mapSize) # If the position is not available the program will loop giving it a new location until it is correct
        traps.append(Traps(i, x, y)) # Adding the amount of traps into the trap list and giving each trap their own identity, x and y coordinate
        gridMap[y][x] = "X" # Setting all traps to display as X on the grid
        print(f"Traps {i + 1} created at ({x}, {y})") # Telling the user that each trap has been created in the location provided by the algorithm
        
def depthfirstSearch(grid, start, goal): # Function creating the depth first search
    stack = [(start, [start])] # Creating the stack array and putting the start position inside it
    visited = set() # Checking if the current position has been visited or not

    while stack: # Looping the search whilst the stack has the positions stored in it to check if it has been visited or not
        (vertex, path) = stack.pop() # Removing current contents from the stack for a new input
        if vertex not in visited: # Checking if the current position has been visited or not
            if vertex == goal: # Checking if the position is the shortest and safest path 
                return path # Returning the shortest and safest path back to the user
            visited.add(vertex) # If the position has been visited it will set it as visited so that it is not checked again.
            x, y = vertex # Setting the x,y coordinates to the vertex
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Checking if the player has moved up, down, left or right
                next_vertex = (x + dx, y + dy) # Setting the new vertex to the new position
                if 0 <= next_vertex[0] < len(grid) and 0 <= next_vertex[1] < len(grid[0]): # Checking all positions stored in the grid
                    if grid[next_vertex[0]][next_vertex[1]] not in ('X', 'T', 'W'):  # Ignoring all traps, treasures and win location as they will only show if the player has not visited that location
                        stack.append((next_vertex, path + [next_vertex])) # adding the path to the stack
    return None # Returning void as the path will be displayed through a print further down once called upon.



def checkTreasures(x, y, player): # Procedure checking if the user collected a treasure
    global treasure # Making the treasure list global so that it can be accessed everywhere for checking (Only appended or deleted in this function)
    for t in treasure: # Collecting all the treasures stored in the list
        if x == t.getTX() and y == t.getTY(): # Checking if the users x,y position is the same as any of the treasures stored in the treasure list
            treasure.remove(t) # If the user is on the treasures coordinate it will remove that specific treasure from the list so that it the specific one cannot be collected again
            print("You have found some treasure! \n You can now choose the following items to obtain: \n 1. Health - Gain an extra life \n 2. Powerup - Immunity to a trap \n 3. Clues - Choice of search to find the treasure and complete the game.") # Giving the user positive options for colelcting the treasure
            time.sleep(3) # Pausing the game so that the user has time to read and make a decision of which positive item they would like
            userChoice = input("Please choose from 'health', 'powerup', 'clues': ").lower() # Giving the user options between a extra health, a power up or a clue to the next treasure by using various types of searches
            if userChoice == "health": # Checking if the user entered health
                print("You have gained 1 more life") # Telling the user they have gained an extra health point
                player.health += 1 # Setting the specific players health to the current + 1
                print("Your new health score is: ", player.health) # Outputting the users health to them so they know how many lives they have
            elif userChoice == "powerup": # Checking if the user entered powerup
                print("You have gained a powerup. You have immunity to one trap.") # Telling them that they are immune to a trap and will not lose health whilst they are immune
                powerup.append(1) # adding 1 power up to the list so that they are immune to 1 trap per powerup collected
                print(f"Your current immunities: {len(powerup)}") # Displaying amount the powerups to the user
            elif userChoice == "clues": # Checking if the user has entered clues
                userChoice2 = input("You now have a clue. Please choose between Binary Search, Depth first search or Breadth first search (BS, DFS, BFS)").lower() # Giving the user options between which clues they can have, different various searches.
                if userChoice2 == "bs": # Checking if the user has chosen the binary search clue
                    print("Loading Binary Search") # Telling the user that they have chosen binary search
                    if len(treasure) > 0: # Checking if there are treasures on the map 
                        nearestTreasure = binarySearchT(player)
                        if nearestTreasure:
                            print(f"The nearest treasure is at {nearestTreasure} for player {player.id + 1}")
                            time.sleep(2)
                        else:
                            print("There is no treasure close enough to you!")
                    else:
                        print("There is no more treasure for you to search for!")
                        time.sleep(2)
                if userChoice2 == "dfs":
                    print("Loading Depth-First Search")
                    start_pos = (player.getX(), player.getY())
                    if len(treasure) > 0:
                        end_pos = (treasure[0].getTX(), treasure[0].getTY())  # Assuming single treasure for simplicity
                        shortestPath = depthfirstSearch(gridMap, start_pos, end_pos)
                        if shortestPath:
                            print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}")
                        else:
                            print(f"No safe path to treasure for Player {player.id + 1}")
                    else:
                        print("There are no treasues left for you to search for!")      

                if userChoice2 == "bfs":
                    print("Loading Breadth-First Search")
                else:
                    print("ERROR - Please enter the correct input.")
            else:
                print("ERROR - You have miss inputted the data please try again.")
            #treasure.remove(t)
            break
    if len(treasure) != 0:
        print(f"You have {len(treasure)} treasures left!")
    else:
        print("You have no more treasures left!")
        print("The exit/winning location will be revealed shortly. You may now get to that location to win!")
        time.sleep(3)
        winninglocationCreation(len(gridMap))
        print("Continuing game: ")

def checkTraps(x, y, player):
    global traps
    for i in traps:
        if x == i.getTrX() and y == i.getTrY():
            if len(powerup) == 0:
                print("You have now landed on a trap! You will now lose a life. Be careful!")
                player.health -= 1
                print(f"Your current lives: {player.health}")
                time.sleep(3)
                traps.remove(i)
            elif len(powerup) != 0:
                print("You have a powerup. This means you are immune to this trap and you have not lost a life.")
                powerup.pop()
                traps.remove(i)
                print(f"You have {len(powerup)} powerups left. Your health is currently on {player.health}")
    if len(traps) != 0:
        print(f"There is {len(traps)} trap(s) left in the game. Make sure you do not lose all your lives.")
    else:
        print("There are no more traps left in the game! Winning may be easier now!")
    print("Continuing the game!")

def checkWin(x, y, player):
    global winLocation
    for i in winLocation:
        if x == i.getWX() and y == i.getWY():
            for player in players:
                print("Congratulations, you have completed the game. You have collected all the treasure, not lost all your lives, and got to the exit.")
                print("\n Game Over")
                if len(treasure) > 0:
                    nearestTreasure = binarySearchT(player)
                    if nearestTreasure:
                        print(f"The nearest treasure is at {nearestTreasure} for player {player.id + 1}")
                        time.sleep(2)
                    else:
                        print("There is no treasure close enough to you!")
                else:
                    print(" Binary Search - There is no more treasure for you to search for!")
                start_pos = (player.getX(), player.getY())
                if len(treasure) > 0:
                    end_pos = (treasure[0].getTX(), treasure[0].getTY())  # Assuming single treasure for simplicity
                    shortestPath = depthfirstSearch(gridMap, start_pos, end_pos)
                    if shortestPath:
                        print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}")
                    else:
                        print(f"No safe path to treasure for Player {player.id + 1}")
                else:
                    print(" Depth First Search - There are no treasues left for you to search for!") 
                print(f"Player {player.id + 1}'s game stats: \n Treasures left: {len(treasure)} \n Traps left: {len(traps)}, \n Players in-game: {len(players)} \n Health: {player.health}")
                time.sleep(2)
                print("\n")

                time.sleep(2)
                winLocation.remove(i)
                print("Thank you for playing!")
                quit()
    print("Continuing game")

def updateGrid():

    global gridMap
    gridMap = [[" "] * len(gridMap) for _ in range(len(gridMap))]
    for player in players:
        gridMap[player.getY()][player.getX()] = str(player.id + 1)
    for t in treasure:
        gridMap[t.getTY()][t.getTX()] = "T"
    for trap in traps:
        gridMap[trap.getTrY()][trap.getTrX()] = "X"
    for winLoc in winLocation:
        gridMap[winLoc.getWY()][winLoc.getWX()] = "W"
    displayGrid()
    

# --// Main Code \\--

mapSize = int(input("Please enter a number for how big the grid shall be (Entering 5 will create a 5x5 grid): "))
createGrid(mapSize)

amount_of_players = int(input("Enter the amount of players you would like: "))
playerCreation(amount_of_players, mapSize)

amount_of_treasure = int(input("Enter the amount of treasure you would like in your game: "))
treasureCreation(amount_of_treasure, mapSize)

amount_of_traps = int(input("Please enter a number of how many traps you would like in your game: "))
trapCreation(amount_of_traps, mapSize)


while all(player.health > 0 for player in players):
    for player in players:
        if player.health <= 0:
            continue
        print(f"Player {player.id + 1}'s Turn") 
        updateGrid()
        time.sleep(2)
        print("\n")
        direction = input("Please enter the direction you would like to go: 'Up', 'Down', 'Left' & 'Right' ").lower()
        player.movePlayer(direction)
        checkTreasures(player.getX(), player.getY(), player)
        checkTraps(player.getX(), player.getY(), player)
        checkWin(player.getX(), player.getY(), player)

print("\n Game Over")
for player in players:
    nearestTreasure = binarySearchT(player)
    if nearestTreasure:
        print(f"The shortest path to find the treasure is at {nearestTreasure} for player {player.id + 1}")
    else:
        print(f" Binary Search - There was no short path to get treasure for player {player.id + 1}")
    start_pos = (player.getX(), player.getY())
    end_pos = (treasure[0].getTX(), treasure[0].getTY()) 
    shortestPath = depthfirstSearch(gridMap, start_pos, end_pos)
    if shortestPath:
        print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}")
    else:
        print(f"Depth First Search - There was no safe path for player {player.id + 1}")
    print(f"Player {player.id + 1}'s game stats: \n Treasures left: {len(treasure)} \n Traps left: {len(traps)}, \n Players in-game: {len(players)} \n Health: {player.health}")
    time.sleep(2)
    print("\n")
