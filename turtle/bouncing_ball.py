# from: https://trinket.io/python/8e8fb5d9d5

from turtle import *

radius = 15


def rectangle(turtle, x, y, width, height, color):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


screen = Screen()

board = Turtle()
board.speed(0)

rectangle(board, 0, 0, 200, 5, "black")
rectangle(board, 0, 0, 5, 200, "black")
rectangle(board, 0, 195, 200, 5, "black")
rectangle(board, 195, 0, 5, 200, "black")

board.ht()

ball = Turtle()
ball.speed(0)
screen.register_shape("ball", (
    (-radius // 2, -radius // 2), (-radius // 2, radius // 2),
    (radius // 2, radius // 2), (radius // 2, -radius // 2)))
ball.shape("ball")
ball.penup()
ball.setx(100)
ball.sety(100)


def collisionCheck(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    return (r1x < r2x + r2w) and (r1x + r2w > r2x) and (r1y < r2y + r2h) and (r1h + r1y > r2y)


dx = 1
dy = 1.5

while True:
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if collisionCheck(ball.xcor(), ball.ycor(), - radius // 2, radius // 2,
                      0, 0, 5, 200):
        dx = dx * -1

    if collisionCheck(ball.xcor(), ball.ycor(), - radius // 2, radius // 2,
                      195, 0, 5, 200):
        dx = dx * -1

    if collisionCheck(ball.xcor(), ball.ycor(), radius // 2, radius // 2,
                      0, 0, 200, 5):
        dy = dy * -1

    if collisionCheck(ball.xcor(), ball.ycor(), radius // 2, radius // 2,
                      0, 195, 200, 5):
        dy = dy * -1

