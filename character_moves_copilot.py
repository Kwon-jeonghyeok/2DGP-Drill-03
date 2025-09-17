from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()

def move_rectangle():
    # 사각형 꼭짓점
    points = [(400, 90), (700, 90), (700, 510), (100, 510), (100, 90), (400, 90)]
    for i in range(len(points) - 1):
        sx, sy = points[i]
        ex, ey = points[i + 1]
        for t in range(0, 100 + 1, 2):
            x = sx + (ex - sx) * t / 100
            y = sy + (ey - sy) * t / 100
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)
            handle_events()
    return points[-1]

def move_triangle(start_x, start_y):
    # 더 크게, 끝점이 (400, 90)인 정삼각형 (꼭짓점이 위)
    # 아래 두 꼭짓점 y=90, x=400±300, 위 꼭짓점 y=90+height, x=400
    base_y = 90
    base_x = 400
    side = 600  # 훨씬 크게
    half_base = side // 2  # 300
    height = int(side * math.sin(math.radians(60)))  # 약 519
    left = (base_x - half_base, base_y)
    right = (base_x + half_base, base_y)
    top = (base_x, base_y + height)
    # 경로: 시작점(400,90) -> 오른쪽 아래 -> 위 -> 왼쪽 아래 -> 시작점(400,90) (반시계방향)
    path = [right, top, left, (base_x, base_y)]
    # 시작점에서 오른쪽 아래로 이동
    for t in range(0, 101, 2):
        x = start_x + (right[0] - start_x) * t / 100
        y = start_y + (right[1] - start_y) * t / 100
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
        handle_events()
    # 삼각형 경로 이동
    for i in range(len(path) - 1):
        sx, sy = path[i]
        ex, ey = path[i + 1]
        for t in range(0, 101, 2):
            x = sx + (ex - sx) * t / 100
            y = sy + (ey - sy) * t / 100
            clear_canvas()
            grass.draw(400, 30)
            character.draw(x, y)
            update_canvas()
            delay(0.01)
            handle_events()
    return (base_x, base_y)

def move_circle(start_x, start_y):
    # 원 중심 (400, 300), 반지름은 시작점과 중심의 거리, 시작점에서 시계방향
    cx, cy = 400, 300
    r = math.sqrt((start_x - cx) ** 2 + (start_y - cy) ** 2)
    # 시작 각도 계산
    start_angle = math.degrees(math.atan2(start_y - cy, start_x - cx))
    for deg in range(0, 360 + 2, 2):
        rad = math.radians(start_angle - deg)  # 시계방향
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
        handle_events()
    # 마지막에 시작점으로 이동 (자연스럽게)
    last_x = cx + r * math.cos(math.radians(start_angle - 360))
    last_y = cy + r * math.sin(math.radians(start_angle - 360))
    for t in range(0, 100 + 1, 2):
        x = last_x + (start_x - last_x) * t / 100
        y = last_y + (start_y - last_y) * t / 100
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
        handle_events()
    return (start_x, start_y)

while True:
    end_rect = move_rectangle()
    end_tri = move_triangle(*end_rect)
    end_circ = move_circle(*end_tri)
