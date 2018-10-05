import turtle

# setup turtle
turtle.setup(400, 500)
wn = turtle.Screen()
tess = turtle.Turtle()

# define operations
def go_forward():
    tess.forward(30)

def turn_left_45():
    tess.left(45)

def turn_right_45():
    tess.right(45)

def quit():
    wn.bye()

# hook up handlers
wn.onkey(go_forward, "Up")
wn.onkey(turn_left_45, "Left")
wn.onkey(turn_right_45, "Right")
wn.onkey(quit, "q")
wn.listen()

# run
wn.mainloop()