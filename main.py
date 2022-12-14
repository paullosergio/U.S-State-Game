import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(title= f"{len(guessed_states)}/50 Guess State Game", 
    prompt="What's another state's name? ").title()
  
    # Writing the name of the state on screen
    if answer in all_states: 
        guessed_states.append(answer )
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data["state"] == answer]
        t.goto(int(state.x),int(state.y))
        t.write(answer)
    
    # Create a csv with missing states
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break



