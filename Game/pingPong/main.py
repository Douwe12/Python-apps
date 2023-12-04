import pygame as pg
from player import Player
from sprite import Sprite
import random as r

# initialize screen
pg.init()
run = True
width, height = 800, 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()


# initialize player
player_width = 15
player_height = 80
player_speed = 4.5
player1 = Player(0, (player_height + height) // 2, player_width, player_height, player_speed)
player2 = Player(width - player_width, (player_height + height) // 2, player_width, player_height, player_speed)


# initialize
ball_radius = 25
ball = Sprite((player_width + width) // 2, (player_height + height) // 2, ball_radius, 2, 'Game/pingPong/Images/yin-yang-teken-300x300.png')
all_sprites = pg.sprite.Group()
all_sprites.add(ball)


# initialize variables
collision = False



# initialize Score
font = pg.font.Font(None, 24)

while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.QUIT()
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

    # display
    pg.draw.rect(screen, (0, 0, 255), (player1.x, player1.y, player1.width, player1.height))
    pg.draw.rect(screen, (0, 0, 255), (player2.x, player2.y, player2.width, player2.height))
    all_sprites.draw(screen)
    
    ball.move_along_vector(2.5)

    # paddle  collision
    if ball.rect.colliderect(player1) or ball.rect.colliderect(player2):
        if ball.vector[0] < 0:
            ball.vector[0] = abs(ball.vector[0])
        else:
            ball.vector[0] = -ball.vector[0]

        if ball.vector[1] < 0:
            ball.vector[1] = abs(ball.vector[1])

    
    # upper and bottom wall collision
    if ball.y == 0:
        if ball.vector[1] < 0:
            ball.vector[1] = abs(ball.vector[1])
        else:
            ball.vector[1] = -ball.vector[1]

    
    if ball.y == height - ball.radius * 2:
        ball.vector[1] = -ball.vector[1]


    # side wall collision detection
    print(ball.x)
    if ball.x < 0:
        player1.points += 1
        restart()
        print('left wall collision')
    
    if ball.x > width - ball.radius * 2:
        player2.points += 1
        restart()
        print("right wall collision")


    left_text = font.render(f'Player 1 score: {player1.points}', True, (0, 0, 0))
    left_text_rect = left_text.get_rect()
    left_text_rect.topleft = (10, 10)
    screen.blit(left_text, left_text_rect)
    right_text = font.render(f'Player 2 score: {player2.points}', True, (0, 0, 0))
    right_text_rect = right_text.get_rect()
    right_text_rect.topright = (width - 10, 10)
    screen.blit(right_text, right_text_rect)






    def restart():
        ball.x, ball.y = (player_width + width) // 2, (player_height + height) // 2
        ball.vector = (r.uniform(-1, 1), r.uniform(-1, 1))

    
    

    pg.display.flip()



