import turtle
t = turtle.Pen()
t.color(1,0,0)

def octagon(size, red, green, blue, outline):
    t.color(red, green, blue)
    t.begin_fill()
    for x in range(0, 8):
        t.forward(size)
        t.right(45)
    t.end_fill()
    if outline == True:
        t.color(0,0,0)
        for x in range(0, 8):
            t.forward(size)
            t.right(45)
octagon(100, 1,0,1, True)

