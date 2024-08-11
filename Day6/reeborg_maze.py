# look at reeborg.ca Maze challenge and use the following code
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# avoid looping with no walls
while front_is_clear():
    move()
turn_left()
    
# at_goal will check if the flag is at robots current position
# keep hugging the right wall to reach the flag
while not at_goal():
    if wall_in_front():
        if not wall_on_right():
            turn_right()
            move()
        else:
            turn_left()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        move()
 
