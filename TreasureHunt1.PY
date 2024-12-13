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
                        nearestTreasure = binarySearchT(player) # Running the binary search function and passing the players information through for their coordinates
                        if nearestTreasure: # Checking if there is a nearest treasure
                            print(f"The nearest treasure is at {nearestTreasure} for player {player.id + 1}") # Printing the nearest treasure to the players coordinates.
                            time.sleep(2) # Pausing the program for 2 seconds so the user can read and work out where the next treasure is
                        else: # If the first condition is not met do:
                            print("There is no treasure close enough to you!") # Telling the user there is no treasure close to them
                    else: # If there is no treasure left in the game
                        print("There is no more treasure for you to search for!") # Telling the user there is no more treasure left
                        time.sleep(2) # Pausing the game for 2 seconds
                if userChoice2 == "dfs": # Checking if the user requested for the depth-first search
                    print("Loading Depth-First Search") # Telling the user that the depth first search is loading
                    start_pos = (player.getX(), player.getY()) # Getting the players position to get the starting position
                    if len(treasure) > 0: # Checking if there is treasure in the game
                        end_pos = (treasure[0].getTX(), treasure[0].getTY())  # Getting the treasure stored in position 0 for the end point
                        shortestPath = depthfirstSearch(gridMap, start_pos, end_pos) # Running the function to find the shortest path to the available treasures
                        if shortestPath: # Checking if the shortest path has been found
                            print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}") # Telling the player which path is the shortest to them
                        else: # If the condition is not met do:
                            print(f"No safe path to treasure for Player {player.id + 1}") # Telling the player that there is no safe path without landing in a trap
                    else: # If the first condition has not been met do:
                        print("There are no treasues left for you to search for!") # Telling the user that there is no more treasure left in the game so they cant use the clues 

                if userChoice2 == "bfs": # Checking if the user requested the bredth first search
                    print("Loading Breadth-First Search") # Alerting the user that the bredth first search is loading
                else: # If a different input was entered do:
                    print("ERROR - Please enter the correct input.") # Telling the user they have entered the wrong information
            else: # If any error at all occurs do:
                print("ERROR - You have miss inputted the data please try again.") # Telling the user the program did not understand their input
            #treasure.remove(t)
            break # Force ending the loop so the program will continue
    if len(treasure) != 0: # Checking if there is any treasure in the game
        print(f"You have {len(treasure)} treasures left!") # Alerting the user how much treasure is left for them to find
    else: # If there is no treasure do:
        print("You have no more treasures left!") # Telling the user they have no treasure left in the game
        print("The exit/winning location will be revealed shortly. You may now get to that location to win!") # Alerting the user that the winning location will now be displayed
        time.sleep(3) # Pausing the game for 2 seconds so that the user can read whats happening next
        winninglocationCreation(len(gridMap)) # Running the function to create the the winning location
        print("Continuing game: ") # Telling the user that the game is continuing

def checkTraps(x, y, player): # Procedure to check if the user has stepped on a trap or not
    global traps # Making the trap lsit global so that it can be accessed everywhere (Only appended or removed in this function only)
    for i in traps: # Gathering all the different traps stored in the list
        if x == i.getTrX() and y == i.getTrY(): # Checking if the users x,y coordinates are the same as any of the coordinates that the traps are on
            if len(powerup) == 0: # Checking if the user has any powerups if not then:
                print("You have now landed on a trap! You will now lose a life. Be careful!") # Alerting the user that they have landed on a trap
                player.health -= 1 # Removing 1 life from the player which stood on the on the trap
                print(f"Your current lives: {player.health}") # Telling the user how many lifes they have left
                time.sleep(3) # Pausing the game for 3 seconds so the user can read their health levels
                traps.remove(i) # Removing the specific trap which the player stood on so that it cannot be used again
            elif len(powerup) != 0: # Checking if the players have any powerups at all if so then: (Users share powerups so that they can save eachothers lifes espeically if a player is on their final life)
                print("You have a powerup. This means you are immune to this trap and you have not lost a life.") # Telling the user they have a powerup
                powerup.pop() # Removing the powerup once used
                traps.remove(i) # Removing the trap so that it cannot be used again
                print(f"You have {len(powerup)} powerups left. Your health is currently on {player.health}") # Telling the user how many powerups are left and displaying their current health status
    if len(traps) != 0: # Checking if there are any traps left if so do:
        print(f"There is {len(traps)} trap(s) left in the game. Make sure you do not lose all your lives.") # Outputting to the user how many traps are left in the game
    else: # If there are no traps then do:
        print("There are no more traps left in the game! Winning may be easier now!") # Printing to the user that they have no more traps left so they are able to win
    print("Continuing the game!") # Telling the user that the game is continuing

def checkWin(x, y, player): # Function checking if a player has stood on the winning location
    global winLocation # Setting the winlocation list to global so it can be accessed anywhere (Only appended and deleted in this function)
    for i in winLocation: # Gathering the data of the win location
        if x == i.getWX() and y == i.getWY(): # Checking if a players coordinates are the same as the win locations coordinates
            for player in players: # Getting the details of each individual player
                print(f"Congratulations player {player.id + 1}, you have completed the game. You have collected all the treasure, you have also beat your opponents, not lost all your lives, and got to the exit.") # Alerting the user which player won the game
                print("\n Game Over") # Telling the user that the game is over
                if len(treasure) > 0: # Checking the amount of treasures (Should always be 0)
                    nearestTreasure = binarySearchT(player) # Collecting the nearest treasure (Should not return)
                    if nearestTreasure: # Checking if there is near by treasure
                        print(f"The nearest treasure is at {nearestTreasure} for player {player.id + 1}") # Telling the user which treasure is near them
                        time.sleep(2) # Pausing the game for 2 seconds
                    else: # If no treasure is near them then do:
                        print("There is no treasure close enough to you!") # Telling the user there is no treasure near by
                else: # If there is no treasure left then:
                    print(" Binary Search - There is no more treasure for you to search for!") # Telling the user that the binary seach cannot find any treasure (This is always the output once the user has won)
                start_pos = (player.getX(), player.getY()) # Getting the players location for the starting position of the DFS search
                if len(treasure) > 0: # Checking if there is any treasure in the game (Should be 0)
                    end_pos = (treasure[0].getTX(), treasure[0].getTY())  # Getting the end position by using the first position in the treasure list
                    shortestPath = depthfirstSearch(gridMap, start_pos, end_pos) # Finding the shortest path to each treasure
                    if shortestPath: # If there is a safe and short path then do:
                        print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}") # Telling the user the shortest and safest path to them
                    else: # If not then:
                        print(f"No safe path to treasure for Player {player.id + 1}") # Telling the user there is no safe path and there is likely a trap on their route
                else: # If no treasure do:
                    print(" Depth First Search - There are no treasues left for you to search for!") # Telling the user that there is no treasure left in the game for the DFS search (Should always be the output as the user has won) 
                print(f"Player {player.id + 1}'s game stats: \n Treasures left: {len(treasure)} \n Traps left: {len(traps)}, \n Players in-game: {len(players)} \n Health: {player.health}") # Telling the user the statistics of each player
                time.sleep(2) # Pausing the game for 2 seconds
                print("\n") # Printing a gap

                time.sleep(2) # Pausing the game for 2 more seconds
                winLocation.remove(i) # Removing the win lcoation from the grid
                print("The game is over, We hope you enjoyed it!")
                quit() # Ending the game
    print("Continuing game") # If the user is not stood on the win location it will alert them that the game is continuing

def updateGrid(): # Function to update the grid with the latest movements

    global gridMap # Setting the grid map to global so that in can be accessed by all the functions as it needs to for the game to work
    gridMap = [[" "] * len(gridMap) for _ in range(len(gridMap))] # Setting the grid and making the empty spaces display an empty space
    for player in players: # Checking the player list for the amount of players
        gridMap[player.getY()][player.getX()] = str(player.id + 1) # Placing each player to their given coordinates from the class and setting the display as the players ID
    for t in treasure: # Checking the treasure list for the amount of treasures
        gridMap[t.getTY()][t.getTX()] = "T" # Placing each treasure to their given coordinates from the class and setting the display as a T
    for trap in traps: # Checking the trap list for the amount of traps
        gridMap[trap.getTrY()][trap.getTrX()] = "X" # Placing each trap to their given coordinates from the class and setting the dispkay as X
    for winLoc in winLocation: # Checking the win list for the 1 win location
        gridMap[winLoc.getWY()][winLoc.getWX()] = "W" # Placing the win location to its given coordinates from the class and setting the display as W
    displayGrid() # Function to print the grid out with the latest information
    

# --// Main Code \\--

print("----**** Treasure Hunt ****---- \n Welcome to the treasure hunt game, you are stranded on an island with various treasures, powerups and clues you can find to escape the island. \n However there are multiple traps which will damage your health. \n If you have more than one player then the game because a race and it is the first player to escape. \n Good luck and have fun! ") # Displaying the game introduction to the player
time.sleep(3) # Pausing the game for 3 seconds
mapSize = int(input("Please enter a number for how big the grid shall be (Entering 5 will create a 5x5 grid): ")) # Asking the user to input the grid size
createGrid(mapSize) # Fucntion creating the grid size by the user input

amount_of_players = int(input("Enter the amount of players you would like: ")) # Asking the user to input the amount of players they want in the game
playerCreation(amount_of_players, mapSize) # Function creating the players and passing the mapsize

amount_of_treasure = int(input("Enter the amount of treasure you would like in your game: ")) # Asking the user to input the amount of treasure they want in the game
treasureCreation(amount_of_treasure, mapSize) # Function creating the treasures and passing the mapsize

amount_of_traps = int(input("Please enter a number of how many traps you would like in your game: ")) # Asking the user to input the amount of traps they want in the game
trapCreation(amount_of_traps, mapSize) # Function creating the traps and passing the mapsize


while all(player.health > 0 for player in players): # Continous loop running the game until a player loses all their health
    for player in players: # Checking the playerlist to see how many players are in the game and gatehring their details
        if player.health <= 0: # Checking if any of the players does not have enough health
            continue # Continuing the game so that each player gets a go before it ends as someone has lost all their lifes
        print(f"Player {player.id + 1}'s Turn") # Alerting the user whose turn it is to move
        updateGrid() # Function used to update the grid and re display it with the latest moves
        time.sleep(2) # Pausing th game for 2 seconds
        print("\n") # Printing a gap in the output
        direction = input("Please enter the direction you would like to go: 'Up', 'Down', 'Left' & 'Right' ").lower() # Asking the user to decide what direction they want to move within the game
        player.movePlayer(direction) # Moving the player the direction they chose based on whose go it is, this is ran through a function in the class
        checkTreasures(player.getX(), player.getY(), player) # Checking if a player has collected any treasures by passing the players coordinates
        checkTraps(player.getX(), player.getY(), player) # Checking if a player has stood on any traps by passing the players coordinates
        checkWin(player.getX(), player.getY(), player) # Checking if a player has stood on the win location by passing the players coordinates

print("\n Game Over, You lost! Thank you for playing") # Telling the user that they have lost the game as one of the players health is 0
for player in players: # Checking all the players in the game to output their statistics
    nearestTreasure = binarySearchT(player) # Function used to check the nearest treasure to each player
    if nearestTreasure: # If there was a nearest treasure then:
        print(f"The shortest path to find the treasure is at {nearestTreasure} for player {player.id + 1}") # Outputting the nearest treasure to each player
    else: # If there eas no short path available do:
        print(f" Binary Search - There was no short path to get treasure for player {player.id + 1}") # Telling each user that there was no treasure close enough to them
    start_pos = (player.getX(), player.getY()) # Getting the players coordinates to use as a starting position for the DFS search
    end_pos = (treasure[0].getTX(), treasure[0].getTY()) # Getting the coordinates of the treasure to use as the end point
    shortestPath = depthfirstSearch(gridMap, start_pos, end_pos) # Running the function with the suitable paramaters to find the shortest and safest path
    if shortestPath: # Checking if there is a safe and short path
        print(f"The safest and shortest path to the treasure is at {shortestPath} for player {player.id + 1}") # Telling each user that the safest and shortest path available to the treasure
    else: # If there is not a safe path do:
        print(f"Depth First Search - There was no safe path for player {player.id + 1}") # Telling each user that there was no safe path and there may be a trap on the route
    print(f"Player {player.id + 1}'s game stats: \n Treasures left: {len(treasure)} \n Traps left: {len(traps)}, \n Players in-game: {len(players)} \n Health: {player.health}") # Outputting to the user each players statistics at the end of the game