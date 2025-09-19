from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')

def move_top():
    for x in range(780,20,-5):
        draw_boy(x,550)
    pass

def move_right():
    for y in range(50,550,5):
        draw_boy(780,y)

    pass

def move_left():
    for y in range(550,50,-5):
        draw_boy(20,y)
    pass

def move_bottom1():
    for x in range(400,780,5):
        draw_boy(x,50)
    pass

def move_bottom2():
    for x in range(20,400,5):
        draw_boy(x,50)
    pass
def move_rectangle():
    print("move rectangle")
    move_bottom1()
    move_right()
    move_top()
    move_left()
    move_bottom2()

    clear_canvas_now()

    pass

def move_circle():
    print("move circle")
    r =250
    for deg in range(-90,-450,-1):
        x = r*math.cos(math.radians(deg)) + 400
        y = r*math.sin(math.radians(deg)) + 300
        draw_boy(x, y)

    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_rectangle()
    move_circle()
    pass






close_canvas()
