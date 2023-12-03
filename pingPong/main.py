import pygame as pg
from player import Player
from ball import Ball

# initialize screen
pg.init()
run = True
width, height = 800, 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()


# initialize player
player_width = 15
player_height = 40
player_speed = 4.5
player1 = Player(0, (player_height + height) // 2, player_width, player_height, player_speed)
player2 = Player(width - player_width, (player_height + height) // 2, player_width, player_height, player_speed)


# initialize
ball_radius = 20
ball = Ball((player_width + width) // 2, (player_height + height) // 2, ball_radius, 2)

while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break 

    screen.fill((255, 255, 255))

    keys = pg.key.get_pressed()
    # player1
    if keys[pg.K_UP] and player1.y > 0:
        player1.y -= player1.speed
    if keys[pg.K_DOWN] and player1.y < height - player_height:
        player1.y += player1.speed

    # player2
    if keys[pg.K_w] and player2.y > 0:
        player2.y -= player2.speed
    if keys[pg.K_s] and player2.y < height - player_height:
        player2.y += player2.speed

    pg.draw.rect(screen, (0, 0, 255), (player1.x, player1.y, player1.width, player1.height))
    pg.draw.rect(screen, (0, 0, 255), (player2.x, player2.y, player2.width, player2.height))
    pg.draw.circle(screen, (0, 0, 0), (ball.x, ball.y), ball.radius)

    if ball.x - ball.radius > 0:
        ball.move_left()

    pg.display.flip()