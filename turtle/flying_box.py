#
# Look for help here:
#     https://docs.python.org/3/library/turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions
#


import time
from turtle import *

size = 300
step = 7

screen = Screen()
screen.tracer(0)

nikki = Turtle(visible=False)
nikki.speed(0)
nikki.color('purple', 'purple')

while True:

    # fly box towards us
    for i in range(1, size, step):
        nikki.clear()
        nikki.setx(-i / 2)
        nikki.sety(-i / 2)

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

        screen.update()
        time.sleep(0.01)

    # fly box away from us
    for i in range(1, size, step):
        j = size - i

        nikki.clear()
        nikki.setx(-j / 2)
        nikki.sety(-j / 2)

        nikki.begin_fill()
        nikki.forward(j)
        nikki.left(90)
        nikki.forward(j)
        nikki.left(90)
        nikki.forward(j)
        nikki.left(90)
        nikki.forward(j)
        nikki.left(90)
        nikki.end_fill()

        screen.update()
        time.sleep(0.01)