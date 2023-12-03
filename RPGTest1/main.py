import pygame as pg
from function import *
from player import Player
from projectile import Projectile

width, height = 1500, 750
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Elemental RPG")
run = True
clock = pg.time.Clock()

# player initialisation
player_width = 20
player_height = 20
player = Player((width - player_width) // 2, (height - player_height) // 2, player_width, player_height, 0.1)


# projectile initialisation
projectile_width = 30
projectile_height = 30
projectile = 0

while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player.x > 0:
        player.x -= player.speed
    if keys[pg.K_RIGHT] and player.x < player.width + width:
        player.x += player.speed
    if keys[pg.K_UP] and player.y > 0:
        player.y -= player.speed
    if keys[pg.K_DOWN] and player.y < player.height + height:
        player.y += player.speed

    if keys[pg.K_SPACE]:
        projectile = player.shoot_projectile()
    

    

    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (255, 24, 12), (player.x, player.y, player.width, player.height))

    if not projectile == 0:
        pg.draw.rect(screen, (12, 24, 255), (projectile[0].x, projectile[0].y, projectile[0].width, projectile[0].height))
        projectile[0].height -= projectile[0].speed








    update()
    