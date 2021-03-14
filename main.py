from turtle import Turtle, Screen
import random


def play():
    race_on = False
    screen = Screen()
    screen.setup(width=500,height=400)
    user_bet = screen.textinput(title="Make your bet....",prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red","green","blue","orange","purple","black"]
    y_cor = [-150,-100,-50,0,50,100,-150]
    turtles = []
    for i in range(len(colors)) :
        temp = Turtle(shape="turtle")
        temp.penup()
        temp.color(colors[i])
        temp.goto(x=-200,y=y_cor[i])
        turtles.append(temp)

    if user_bet:
        race_on = True

    while (race_on):
        for i in range(len(turtles)):
            if turtles[i].xcor()>200:
                winning = turtles[i].pencolor()
                if winning.lower()==user_bet.lower():
                    print("")
                    play_again = screen.textinput(title="Game over, Your turtle has won the race!!!!!",
                                                  prompt="Do you want to play again? Type yes or no.")

                else:
                    print("Your turtle lost, consider betting on a rabbit next time.")
                    play_again = screen.textinput(title="Game over, Your turtle lost.",
                                                  prompt="Consider betting on a rabbit next time. Do you want to play again? Type yes or no.")


                if play_again.lower() == "yes":
                    screen.clear()
                    play()


                race_on = False
            rand_dist = random.randint(0, 10)
            turtles[i].forward(rand_dist)






    screen.exitonclick()

play()