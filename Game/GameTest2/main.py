import sys
import pygame as pg
from function import update
from button import Button

pg.init()

width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Tower defense")
button = Button(300, 200, 100, 100, (255, 0, 0), "create")
mouse_x, mouse_y = pg.mouse.get_pos()
tower = Button(mouse_x, mouse_y, 100, 100, (0, 0, 255), "tower")
drag_tower = False
placed = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if drag_tower:
                    drag_tower = False
                    placed = True
                x, y = pg.mouse.get_pos()
                if button.rect.collidepoint(event.pos):
                    drag_tower = True

    screen.fill((0, 0, 0))
    button.draw(screen)

    if drag_tower or placed:
        tower.draw(screen)
    update()

    