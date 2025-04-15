import pygame as pg
import sys

pg.init()
win = pg.display.set_mode((600, 600))
pg.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # rysowanie kwadratów
    pg.draw.rect(win, CZERWONY , (10, 30, 100, 100))
    pg.draw.rect(win, ZOLTY, (160, 30, 100, 100))
    pg.draw.rect(win, ZIELONY, (310, 30, 100, 100))
    # rysowanie kół
    pg.draw.circle(win, FIOLETOWY, (60, 200), 50, 0)
    pg.draw.circle(win, JASNY_NIEBIESKI, (210, 200), 50, 25)
    pg.draw.circle(win, POMARANCZOWY, (360, 200), 50, 5)
    # linia pozioma
    pg.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
    # linia pionowa
    pg.draw.line(win, SZARY, (210, 275), (210, 375), 5)
    # rysowanie plusa
    pg.draw.line(win, NIEBIESKI, (310, 325), (410, 325), 10)
    pg.draw.line(win, SZARY, (360, 275), (360, 375), 10)
    # wypisywanie tekstu
    font = pg.font.SysFont('comicsans', 30)
    label = font.render('Tekst do wyświetlania ', 1, (255, 255, 255))
    win.blit(label, (100, 425))

    pg.display.update()