from tkinter import *
import random
import time
root = Tk()
canvas = Canvas(root, width = 400, height = 400)
canvas.pack()

#canvas.create_polygon(10,10,10,50,50,50,fill = "black",outline = "red")
#root.update()
#time.sleep(0.5)
#canvas.move(1,50,0)
#root.update()
#time.sleep(0.5)
#canvas.move(1,0,50)
#root.update()
#time.sleep(0.5)
#canvas.move(1,-50,0)
#root.update()
#time.sleep(0.5)
#canvas.move(1,0,-50)
my_image = PhotoImage(file = 'C:\\Users\\admin\\Pictures\\Camera Roll\\wtf.gif')
canvas.create_image(0,0,anchor=NW, image=my_image)
root.update()
time.sleep(0.5)
canvas.move(1,50,0)
root.update()


def random_triangles(width, height, length, fill_color):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	z1 = random.randrange(length)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(width)
	z2 = z1 + random.randrange(width)
	canvas.create_polygon(x1,y1,z1,x2,y2,z2,fill = fill_color, outline = "black")

#for x in range(100):
#	random_triangles(400,400,400, "red")
#	random_triangles(400,400,400, "blue")

