# look at reeborg.ca Hurdle2 challenge and use the following code
def turnRight():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    
# at_goal will check if the flag is at robots current position
while not at_goal():
    jump()