import pygame as pg
import random as r
from function import update
from player import Player
from star import Star
from vector import Vector
from bullet import Bullet

# initialize screen
pg.init()
run = True
width, height = 800, 600
screen = pg.display.set_mode((width, height))


# initialize Player
player_height = 10
player_width = 10
player_speed = 1
player = Player((width - player_width) // 2, (height - player_height) // 4, player_width, player_height, player_speed)

# initialize clock
clock = pg.time.Clock()

# initalize Star
star_count = 0
stars = []
shooting_stars = []
cooldown = 1000

star_width = 10
star_height = 10
star_speed = 1

# initialize bullet
bullets = []
bullet_interval = 600
shooting_timer = 0

bullet_height = 10
bullet_width = 4
bullet_speed = 3


while run:
    timer = clock.tick(60)
    star_count += timer
    if star_count > cooldown:
        star = Star(r.randint(5, width -5), 0, star_width, star_height, star_speed, bullet_interval)
        stars.append((star, (r.randint(10, width - 10), r.randint(20, height // 1.5))))
        star_count = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
    screen.fill((255, 255, 255))
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and player.y > 0 + player_height:
        player.y -= player.speed
    if keys[pg.K_DOWN] and player.y < height - player_height:
        player.y += player.speed
    if keys[pg.K_LEFT] and player.x > 0 + player_width:
        player.x -= player.speed
    if keys[pg.K_RIGHT] and player.x < width - player_width:
        player.x += player.speed

    # render player
    pg.draw.rect(screen, (0, 0, 255), (player.x, player.y, player.width, player.height))

    # render star
    for star in stars:
        pg.draw.rect(screen, (100, 200, 24), (star[0].x, star[0].y, star[0].width, star[0].height))
        vector = Vector.get_vector((star[0].x, star[0].y), star[1])
        star[0].move_along_vector(vector)
        if (star[0].x, star[0].y) == star[1]:
            stars.pop(stars.index((star[0], star[1])))
            shooting_stars.append(star)

        if star[0].colliderect(player):
            run = False
            print("Player died")
            break


    # render shooting stars + shooting
    for star in shooting_stars:
        star = star[0]
        pg.draw.rect(screen, (100, 200, 24), (star.x, star.y, star.width, star.height))

        star.shoot_timer += timer
        star.shoot_bullet(star.x, star.y, bullet_width, bullet_height, bullet_speed, bullets)
        star.shoot_bullet(star.x + star.width, star.y, bullet_width,  bullet_height, bullet_speed, bullets)


        if star.colliderect(player):
            run = False
            print("Player died")
            break

        
    for bullet in bullets:
        pg.draw.rect(screen, (0, 0, 0), (bullet[0].x, bullet[0].y, bullet[0].width, bullet[0].height))
        if bullet[0].y < height + bullet[0].height:
            bullet[0].move_down()


        if bullet[0].colliderect(player):
            run = False
            print("Player died")
            break















    update()
