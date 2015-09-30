import turtle
repeats = 0

turtle.fillcolor("blue")
turtle.begin_fill()

while repeats < 360:
    turtle.forward(3.5)
    turtle.left(1)
    repeats = repeats + 1

repeats = 0
turtle.fillcolor("green")

while repeats < 360:
    turtle.forward(1.5)
    turtle.left(1)
    repeats = repeats + 1
    
turtle.end_fill()
turtle.done()