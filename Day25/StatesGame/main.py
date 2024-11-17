import turtle
import pandas

#setup of screen and background image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()

#game variables
game_over = False
score = 0
states_found = []

#read csv
states_data = pandas.read_csv("50_states.csv")
max_states = states_data.shape[0]

def correct_state(state):
    '''adds correct state to map'''
    states_found.append(answer_row.state.values[0])
    
    x_pos = state.x.values[0]
    y_pos = state.y.values[0]
    
    writer.penup()
    writer.setposition(x_pos, y_pos)
    writer.pendown()
    writer.write(answer_row.state.values[0])

    


while( not game_over):
    answer_state = screen.textinput(title=f"{score}/{max_states} States Correct", prompt="What'state's name?")
    answer_row = states_data.loc[states_data["state"].str.lower() == answer_state.lower()]

    if not answer_row.empty and answer_row.state.values[0] not in states_found:
        score += 1
        correct_state(answer_row)
        
    
