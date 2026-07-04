import turtle 
import random as rd 
WIDTH = 800
HEIGHT = 600
COLOURS = ["red","black","green","yellow","pink","orange","white"]
screen = turtle.Screen()
screen.title("turtle race page ")
screen.setup(WIDTH,HEIGHT)
try :
    number_of_racingturtle = int(screen.textinput(title="number of turtle",prompt="enter the number of racing turtles [2-7]"))
except ValueError:
    print("invalid input")

race_list = []
spacing = WIDTH/ (number_of_racingturtle + 1)
for i in range(number_of_racingturtle):
    race = turtle.Turtle()
    race.color(COLOURS[i])
    race.shape("turtle")
    race.penup()
    race.goto(-WIDTH/2 + spacing * (i+1) , -HEIGHT/2 + 20 )
    race.pendown()
    race.left(90)
    race_list.append(race)


index = -1
while True :
    for race in race_list:
        distance = rd.randrange(start=1,stop=20)
        race.forward(distance)
        x_cur,y_cur = race.position()
        if y_cur >= HEIGHT/2 -20:
            index = race_list.index(race)
            break
    if y_cur >= HEIGHT/2 -20:
        break

winner = COLOURS(index)

                 

screen.mainloop()