#from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

r = [255, 0, 0]
w = [255, 255, 255]



stage_one = [
w, w, w, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, r, r, r, r, w, w, w,
w, r, w, r, w, r, r, w,
w, w, w, r, r, w, w, w,
w, w, r, r, w, r, w, w,
w, r, w, w, r, w, w, w,
r, w, w, w, w, w, w, w,
]
stage_two = [
w, w, w, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, r, w, w, w,
]
##stage_three = [
##w, w, w, w, r, w, w, w,
##w, w, r, r, r, r, w, w,
##w, w, w, w, r, w, r, w,
##w, w, w, w, r, w, w, w,
##w, w, w, r, r, w, w, w,
##w, w, w, r, w, r, r, w,
##w, r, r, w, w, w, r, w,
##w, w, w, w, w, w, r, r,
##]

sense.clear()

while True:
    sense.set_pixels(stage_one)
    sleep(0.5)
    sense.set_pixels(stage_two)
    sleep(0.5)
    #sense.set_pixels(stage_three)
    #sleep(0.5)
    
