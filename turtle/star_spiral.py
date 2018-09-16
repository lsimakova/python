import turtle

spiral = turtle.Turtle()
spiral.speed(30)

for i in range(100):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()