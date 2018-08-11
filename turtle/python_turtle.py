# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 06:01:01 2018

@author: admin
"""
import turtle


def star(size, points):
    
    if points % 2 == 0:
        angle = (360 / points) + 180
    else:
        angle = (180 / points) + 180
        
    for x in range(0, points):
        t.forward(size)
        t.left(angle)

        

t = turtle.Pen()
t.speed(0)
t.reset()

t.up()
t.goto(-200,200)
t.down()


star(200, 9)

t.up()
t.goto(100,0)
t.down()


star(200, 11)

t.up()
t.goto(-200,-100)
t.down()

star(200, 7)


t.up()
t.goto(100,-150)
t.down()

star(200, 8)

#t.goto(100,200)
