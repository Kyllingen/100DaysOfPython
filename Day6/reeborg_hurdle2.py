# look at reeborg.ca Hurdle2 challenge and use the following code
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# at_goal will check if the flag is at robots current position
while not at_goal():
    jump()