import pygame as pg
import sys
import random
from player import Player
from star import Star
from function import *

run = True
hit = False
width, height = 800, 600
screen = pg.display.set_mode((width, height))
background = pg.image.load("FallingStarGame\download.jpeg").convert()
pg.display.set_caption("Movement")


game_speed = 100

player_size = 20
player_speed = 1
player = Player((width + player_size) // 2, height - player_size, player_size, player_speed)

stars = []
clock = pg.time.Clock()
cooldown = game_speed * 5

star_speed = game_speed * 0.01
star_size = 1

star_count = 0
count = 0

while run:
    star_count += clock.tick(60)

    if star_count > cooldown:
        random_int = random.randint(0, 10)
        star_width = star_size * 5
        star_height = star_size * 10
        multiplier = 1.5
        if random_int < 1:
            star_to_spawn = Star(random.randint(0, width), 0, star_width * multiplier, star_height * multiplier, star_speed * multiplier, True)
        else:
            star_to_spawn = Star(random.randint(0, width), 0, star_width, star_height, star_speed, False)
        stars.append(star_to_spawn)
        star_count = 0



    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.blit(background, (0, 0))

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player.x > 0:
        player.move_left()
    if keys[pg.K_RIGHT] and player.x < width - player.size[0] // 2:
        player.move_right()

    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.size[0], player.size[0]))
    for star in stars:
        pg.draw.rect(screen, (0, 0, 255), (star.x, star.y, star.width, star.height))
        star.move_down()
        if star.y > height:
            stars.remove(star)
            if cooldown > 50:
                cooldown -= game_speed * 0.005
                count += 1
                if count == 25:
                    for star in stars:
                        if not star.special:
                            star_speed += 0.001
                            star.speed = star_speed
                    count = 0
                    multiplier += 0.2
                    star_size += 0.1
        elif star.colliderect(player):
            stars.remove(star)
            hit = True
            break

    if hit:
        run = False
        print("game over")
    update()

    