from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

def move_rectangle():
    print("move rectangle")
    clear_canvas_now()

    pass

def move_circle():
    print("move circle")
    r =200
    for deg in range(0,360):
        x = r*math.cos(math.radians(deg)) + 400
        y = r*math.sin(math.radians(deg))+300
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)

    pass


while True:
    move_circle()

    move_rectangle()
    pass






close_canvas()
