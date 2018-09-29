#
# Look for help here:
#     https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions
#


import time
from turtle import *
import random


def draw_circle(nikki, i):
    nikki.penup()
    nikki.sety(-i)
    nikki.pendown()

    nikki.begin_fill()
    nikki.circle(i)
    nikki.end_fill()



def draw_box(nikki, i):
    nikki.penup()
    nikki.setx(-i / 2)
    nikki.sety(-i / 2)
    nikki.pendown()

    nikki.begin_fill()
    nikki.forward(i)
    nikki.left(90)
    nikki.forward(i)
    nikki.left(90)
    nikki.forward(i)
    nikki.left(90)
    nikki.forward(i)
    nikki.left(90)
    nikki.end_fill()


size = 300
step = 7

screen = Screen()
screen.tracer(0)

nikki = Turtle(visible=False)
nikki.speed(5)
nikki.pensize(8)
nikki.color('red', 'green')

while True:

    # pick shape to animate
    number = random.randint(1, 2)
    if number == 1:
        draw_shape = draw_box
    else:
        draw_shape = draw_circle

    # fly box towards us
    for i in range(1, size, step):
        nikki.clear()
        draw_shape(nikki, i)
        screen.update()
        time.sleep(0.01)

    # fly box away from us
    for i in range(1, size, step):
        j = size - i
        nikki.clear()
        draw_shape(nikki, j)
        screen.update()
        time.sleep(0.01)