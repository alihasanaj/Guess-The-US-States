import turtle
import pandas
import numpy

# Create Screen 
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get data frame for 50 states csv
state_data = pandas.read_csv("50_states.csv")

# Create a turtle to write the names of the states
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Game information
guessed_states = []

while True:
    
    if len(guessed_states) < 50:
        user_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")
        
        if user_state != None:
            user_state = user_state.title()
        
        if user_state == "Exit":
            break
        
        check = state_data.loc[state_data["state"] == user_state]
        
        # Check in the input is a us state that not already guessed 
        if len(check) and user_state not in guessed_states:
            
            state_name = check.state.to_string(index=False)
            # Get the x and y 
            state_x = int(check.x.iloc[0])
            state_y = int(check.y.iloc[0])
            
            # Write the name of the state
            writer.setpos(state_x, state_y)
            writer.write(state_name)
            guessed_states.append(user_state)
            
    else:
        screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="You Win. You've guessed all the states")
        break



# states_to_learn.csv
all_states = state_data.state
practice_list = [state for state in all_states if state not in guessed_states]

df = pandas.DataFrame({
    "Missing" : practice_list
})

df.to_csv("states_to_learn.csv")
