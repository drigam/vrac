"""
See also -https://trinket.io/python/a1e26a3ea867
"""

import turtle
# import math
# import random

wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
# rotate = int(360)


def drawCircles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Albert, 100, 10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
# rotate = int(90)


def drawCircles_2(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def drawSpecial_2(t, size, repeat):
    for i in range(repeat):
        drawCircles_2(t, size)
        t.right(360 / repeat)


drawSpecial_2(Steve, 100, 10)

def drawCircles_3(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def drawSpecial_3(t, size, repeat):
    for i in range(repeat):
        drawCircles_3(t, size)
        t.right(360 / repeat)


Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
# rotate = int(80)
drawSpecial_3(Barry, 100, 10)


def drawCircles_4(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def drawSpecial_4(t, size, repeat):
    for i in range(repeat):
        drawCircles_4(t, size)
        t.right(360 / repeat)


Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
# rotate = int(90)
drawSpecial_4(Terry, 100, 10)


def drawCircles_5(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 20


def drawSpecial_5(t, size, repeat):
    for i in range(repeat):
        drawCircles_5(t, size)
        t.right(360 / repeat)


Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
# rotate = int(90)
drawSpecial_5(Will, 100, 10)

turtle.Screen().exitonclick()
