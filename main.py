from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("US State Game")
screen.addshape('blank_states_img.gif')
screen.bgpic('blank_states_img.gif')
screen.screensize(canvwidth=400, canvheight=200)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
data = pandas.read_csv("50_states.csv")
state_name = data.state
state_name_list = state_name.to_list()
guessed_list = []
game_is_on = True
while game_is_on:
    #create a separate window where to input to guess the state
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50", prompt="Guess a State name").title()
    if answer_state in state_name_list and answer_state not in guessed_list:
        answer_state_data = data[state_name == answer_state]
        answer_state_data_x = int(answer_state_data.x)
        answer_state_data_y = int(answer_state_data.y)
        turtle.goto(answer_state_data_x, answer_state_data_y)
        turtle.write(answer_state, align="center")
        guessed_list.append(answer_state)
    elif answer_state == "Exit":
        for state in guessed_list:
            #removing the guessed state form the list of all states
            state_name_list.remove(state)
        #create a dataframe
        data_to_learn = pandas.DataFrame(state_name_list)
        #save it to csv file
        data_to_learn.to_csv("state_to_learn.csv")
        break
turtle.mainloop()




