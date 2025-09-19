from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0,800,5):
        draw_boy(x,550)
    pass

def move_right():
    pass

def move_left():
    pass

def move_bottom():
    pass

def move_rectangle():
    print("move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    clear_canvas_now()

    pass

def move_circle():
    print("move circle")
    r =200
    for deg in range(0,360):
        x = r*math.cos(math.radians(deg)) + 400
        y = r*math.sin(math.radians(deg)) + 300
        draw_boy(x, y)

    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_circle()
    move_rectangle()
    pass






close_canvas()
