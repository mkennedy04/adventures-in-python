import turtle
length = 0
angle = 90
growth = 10

#turtle.fillcolor("blue")
#turtle.begin_fill()

while length < 200:
    turtle.forward(length)
    turtle.left(angle)
    length = length + growth

#turtle.end_fill()

turtle.done()
