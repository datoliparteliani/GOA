from turtle import *

def triangles():
    speed(0)
    hideturtle()

    for i in range(1, 121, 2):
        if (i // 2) % 2 == 0:
            fillcolor("green")
        else:
            fillcolor("blue")
        begin_fill()

        x = (i % 10) * 30 - 150
        y = -(i // 10) * 40 + 200
        penup()
        goto(x, y)
        pendown()

        for j in range(3):
            forward(20)
            left(120)

        end_fill()

triangles()
exitonclick()