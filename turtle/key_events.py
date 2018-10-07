import turtle

# setup turtle
turtle.setup(400, 500)
wn = turtle.Screen()

dima = turtle.Turtle()
dima.shape('turtle')

# define operations
def go_forward():
    dima.forward(30)

def turn_left_45():
    dima.left(45)

def turn_right_45():
    dima.right(45)

def quit():
    wn.bye()

# hook up handlers
wn.onkey(go_forward, "Up")
wn.onkey(turn_left_45, "Left")
wn.onkey(turn_right_45, "Right")
wn.onkey(quit, "q")
wn.listen()

# run
turtle.mainloop()