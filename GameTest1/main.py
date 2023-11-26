import pygame as pg
import sys
import time
from functions import update
from player import Player
from enemies import Enemy
from vector import Vector
 
pg.init()

width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Movement")

player_size = 20
player = Player((width - player_size) // 2, (height - player_size) // 2, 50, 0.03)
enemy = Enemy(player.x - (50 + player.size), player.y + (50 - player.size), 20, 0.01)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    # player control movement
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player.x > 0:
        player.move_left()
    if keys[pg.K_RIGHT] and player.x < width - player_size:
        player.move_right()
    if keys[pg.K_DOWN] and player.y > 0:
        player.move_down()
    if keys[pg.K_UP] and player.y < height - player_size:
        player.move_up()
    
    
    # enemy control
    vector = Vector.get_vector(enemy.get_location(), player.get_location())
    enemy.move_along_vector(vector)
    if enemy.check_collide(player):
        print("you lost")
        player.set_location((width - player_size) // 2, (height - player_size) // 2)

    screen.fill((255, 255, 255))
    pg.draw.rect(screen, (0, 128, 255), (player.x, player.y, player.size, player.size))
    pg.draw.circle(screen, (255, 0, 0), (enemy.x, enemy.y), enemy.size)
    update()





