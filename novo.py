import turtle
import random

turtle.speed(2)  
turtle.bgcolor('black')  

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']

def draw_pattern():
    for i in range(500):
        turtle.pencolor(random.choice(colors))
        turtle.width(i / 100 + 1)
        turtle.forward(i)
        turtle.left(80)

draw_pattern()
turtle.done()