from turtle import *

def walk():
    forward(200)
    left(90)
    forward(200)
def fall_back():
    left(180)
    forward(200)
def combinited():
    walk()
    fall_back()

combinited()
exitonclick()