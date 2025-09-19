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

def move_triangle():
    # 삼각형의 시작점과 끝점이 (400, 50) (사각형, 원과 동일)
    # 꼭짓점: 오른쪽 아래(700, 50), 위(400, 550), 왼쪽 아래(100, 50)
    start = (400, 50)
    right = (780, 50)
    top = (400, 550)
    left = (20, 50)
    # 시작점에서 오른쪽 아래로 이동
    steps = 200
    for t in range(steps + 1):
        x = start[0] + (right[0] - start[0]) * t / steps
        y = start[1] + (right[1] - start[1]) * t / steps
        draw_boy(x, y)
    # 오른쪽 아래 -> 위
    for t in range(steps + 1):
        x = right[0] + (top[0] - right[0]) * t / steps
        y = right[1] + (top[1] - right[1]) * t / steps
        draw_boy(x, y)
    # 위 -> 왼쪽 아래
    for t in range(steps + 1):
        x = top[0] + (left[0] - top[0]) * t / steps
        y = top[1] + (left[1] - top[1]) * t / steps
        draw_boy(x, y)
    # 왼쪽 아래 -> 시작점(400, 50)
    for t in range(steps + 1):
        x = left[0] + (start[0] - left[0]) * t / steps
        y = left[1] + (start[1] - left[1]) * t / steps
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_rectangle()
    move_triangle()
    move_circle()

    pass






close_canvas()
