# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 04:34:54 2018

@author: Leo
"""

import turtle
import random
import math


# mathematical function we want to plot
def f(x):
    
    #return 8*math.sin(x*x) - 4
    return 0.5 * x -2

# Logical cartesian X needs to be mapped to an actual 'dx' Diagram X index
def mapX(x,w):

    if x < startX or x > endX:
        raise ValueError('X coordinate out of Boundary')

    return round(w * x / (endX - startX))

# Logical cartesian Y needs to be mapped to an actual 'dy' Diagram Y index
def mapY(y,h):

    return round(h * y / (endY - startY))


t = turtle.Pen()

width,height = turtle.screensize()

startX = -20
endX = 35
startY = -10
endY = 10

#test: plotting with Turtle
#coords = [(x,f(x)) for x in range(-round(length/2), round(length/2))]
#
#t.up()
#t.goto(coords[0])
#t.down()
#for cs in coords:
#    t.goto(cs)

#draw coordinates
#let's draw the X and Y axes
t.up()
t.goto(mapX(startX,width),mapY(0,height))
t.down()
t.forward(width)


t.up()
t.goto(mapX(0,width),mapY(startY,height))
t.down()
t.left(90)
t.forward(height)


#initialize turtl pen in the right position
t.up()
t.goto(mapX(startX,width),mapY(f(startX),height))
t.down()

#let's plot
for x in range(startX,endX+1):
    t.goto(mapX(x,width),mapY(f(x),height))





