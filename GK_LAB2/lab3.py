import pygame as pg
import sys
import math

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption("Siedmiokąt i Figury")

# Kolory
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255, 255, 255)

# Parametry wielokąta
CENTER = (300, 300)
RADIUS = 150
NUM_SIDES = 7

# Funkcja do tworzenia wierzchołków wielokąta foremnego
def create_polygon(center, radius, sides):
    cx, cy = center
    points = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append([x, y])
    return points

# Przekształcenia
def rotate(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    cx, cy = CENTER
    new_points = []
    for x, y in points:
        x -= cx
        y -= cy
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def scale(points, sx, sy):
    cx, cy = CENTER
    return [[(x - cx) * sx + cx, (y - cy) * sy + cy] for x, y in points]

def flip_vertical(points):
    cx, _ = CENTER
    return [[2 * cx - x, y] for x, y in points]

def flip_horizontal(points):
    _, cy = CENTER
    return [[x, 2 * cy - y] for x, y in points]

# Inicjalizacja wielokąta
polygon_points = create_polygon(CENTER, RADIUS, NUM_SIDES)

# Główna pętla
run = True
while run:
    win.fill((255, 255, 100))  # Jasnożółte tło

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                polygon_points = create_polygon(CENTER, RADIUS, NUM_SIDES)
            elif event.key == pg.K_2:
                polygon_points = rotate(polygon_points, 45)
            elif event.key == pg.K_3:
                polygon_points = rotate(polygon_points, 180)
            elif event.key == pg.K_4:
                polygon_points = rotate(polygon_points, -30)
            elif event.key == pg.K_5:
                polygon_points = scale(polygon_points, 2, 0.5)
            elif event.key == pg.K_6:
                polygon_points = flip_vertical(rotate(polygon_points, 60))
            elif event.key == pg.K_7:
                polygon_points = flip_vertical(polygon_points)
            elif event.key == pg.K_8:
                polygon_points = rotate(polygon_points, -45)
            elif event.key == pg.K_9:
                polygon_points = flip_horizontal(rotate(polygon_points, 45))

    # Rysuj siedmiokąt
    pg.draw.polygon(win, NIEBIESKI, polygon_points)

    # Rysuj Figurę z Zadania 2 (trójkąt-prostokąt-trójkąt)
    # Środek na lewo od środka ekranu
    center_x = 100
    center_y = 450

    # Prostokąt
    rect_width = 60
    rect_height = 30
    pg.draw.rect(win, NIEBIESKI, (center_x - rect_width // 2, center_y - rect_height // 2, rect_width, rect_height))

    # Górny trójkąt
    triangle_top = [
        (center_x, center_y - rect_height // 2 - 30),
        (center_x - 20, center_y - rect_height // 2),
        (center_x + 20, center_y - rect_height // 2)
    ]
    pg.draw.polygon(win, NIEBIESKI, triangle_top)

    # Dolny trójkąt
    triangle_bottom = [
        (center_x, center_y + rect_height // 2 + 30),
        (center_x - 20, center_y + rect_height // 2),
        (center_x + 20, center_y + rect_height // 2)
    ]
    pg.draw.polygon(win, NIEBIESKI, triangle_bottom)

    pg.display.update()

pg.quit()
sys.exit()