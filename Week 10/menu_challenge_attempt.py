from pylab import *

# We need to use the random library to randomly choose a treasure position, and get the detector reading
import random

# this function returns a randomly chosen position for the buried treasure
def makeTreasureCoords():
    # choose a random number from 0 to 9 for the x and y coordinates
    return(random.randrange(10),random.randrange(10))

# this function returns the reading from the broken treasure detector
def detect(position_x, position_y, treasure_x, treasure_y):
    # calculates the actual distance, and adds 1, 0 or -1 to get the 'broken' reading (but with a minimum of 0)
    return(max(abs(position_x - treasure_x)+abs(position_y - treasure_y)+random.randrange(-1,2),0))

# this function moves the player to the other side of the island, when necessary
def newPosition(x, y):
    # if the coordinate is not within the range of 0 to 9, then adjust it using %
    return(x%10, y%10)

# the treasure coordinates are randomly generated
treasure_x, treasure_y = makeTreasureCoords()

# the player starts at this position
position_x = 0 # this signifies the horizontal (x) coordinate
position_y = 0 # this signifies the vertical (y) coordinate

# found is set to 1 if the player has found the treasure, 0 otherwise
found = 0
# the player starts with 3 lives
lives = 3

# this while loop runs as long as the treasure has not been found, and the player is not out of lives
while found==0 and lives>0:
    
    # prints the position and detector reading for the player (Adding 1 so it goes from 1 to 10, instead of 0 to 9)
    print("Your position is", position_x+1, position_y+1)
    print("Your detector says the treasure is", detect(position_x, position_y, treasure_x, treasure_y), "moves away.")
    
    # prints the options and asks for input
    print("Options: 1 - left, 2 - up, 3 - right, 4 - down, 5 - dig, any other number - stay.")
    move = float(input("Enter your choice: "))
    
 
    # if the player has chosen to go left, update the new position
    if move==1:
        # calculate new x and y, and then pass it into new Position to account for the edge of the island
        position_x, position_y = newPosition(position_x-1, position_y)
    # --- YOUR CODE HERE ---
    # you need a condition for each movement option
    # and a condition for the digging option
    # remember to update the found and/or lives variables when appropriate
    
    # print messages for your use:
    # "You found the treasure!"
    # "Sorry, there is no treasure here."
    # "You have", lives, "of your lives remaining."
    
    
# if the player has no lives left, let them know they lost
if lives==0:
    print("You are out of lives, better luck next time!")
