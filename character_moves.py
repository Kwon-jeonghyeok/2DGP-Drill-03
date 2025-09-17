from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while True:

    xy_circle = 0

    while x < 780:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

    while y < 560:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)

    while x > 20:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while x<800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while y < 590:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x-8/5
        y += 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x-8/5
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while xy_circle >= -360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x= 400 + 210*math.cos(math.radians(xy_circle) + 3*math.pi/2)
        y= 300+ 210*math.sin(math.radians(xy_circle) + 3*math.pi/2)
        xy_circle -= 1
        delay(0.01)




close_canvas()
