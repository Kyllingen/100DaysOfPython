# look at reeborg.ca Hurdle3 challenge and use the following code
def turnRight():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    
# at_goal will check if the flag is at robots current position
# check if wall is in front to jump or clear to move
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
 
